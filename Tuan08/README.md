# NHẬP MÔN PHÂN TÍCH DỮ LIỆU VÀ HỌC SÂU

- **Sinh Viên Thực Hiên:** Phạm Thế Hùng
- **MSSV:** 2374802010164
- **Môn Học:** Nhập môn phân tích dữ liệu và học sâu
- **Giảng viên:** Nguyễn Thái Anh

## Tuần 8

## 1. Công nghệ và Thư viện sử dụng

- **Ngôn ngữ lập trình:** Python
-  **PyTorch** (`torch`, `torch.nn`, `torchvision`, `torchvision.transforms`)
- **NumPy**, **PIL**
- **Matplotlib** (`matplotlib.pyplot`, `matplotlib.ticker`)
- **Môi trường tính toán:** Mô hình có xử lý trên tính toán đồ hoạ phân luồng CUDA qua GPU 

## 2. Cách hoạt động của Code

### Chuẩn bị dữ liệu và Tiền xử lý (Preprocessing)
- Dữ liệu hình ảnh ban đầu được chuẩn hóa và thu phóng (Resize) về kích thước `128x128` pixel.
- Đối với tập huấn luyện (Train), luồng dữ liệu truyền vào được thực hiện Data Augmentation nhằm giảm thiểu hiện tượng quá khớp (overfitting) và tăng dung lượng tính tổng quát hóa gồm:
  - Lật ngang và lật dọc hình ảnh ngẫu nhiên (`RandomHorizontalFlip`, `RandomVerticalFlip`).
  - Xoay ngẫu nhiên tới biên độ 20 độ (`RandomRotation(20)`).
  - Thay đổi ngẫu nhiên các khía cạnh quang học như độ sáng, độ tương phản và độ bão hòa (`ColorJitter`).
- Về chuẩn định dạng, toàn bộ ảnh chuyển sang kiểu mảng `ToTensor` của torch và Normalize theo các giá trị mean mặc định `[0.485, 0.456, 0.406]` cùng std `[0.229, 0.224, 0.225]`. Các thao tác preprocessing tương tự (ngoại trừ Data Augmentation) cũng được áp dụng cho tập Validation và Test.

```python
train_preprocess = transforms.Compose([
    transforms.Resize((img_size, img_size)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(), 
    transforms.RandomRotation(20),   
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2), 
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) 
])
```

### Custom Dataset và Dataloader
- Tạo một lớp `PLR` kế thừa từ module `Dataset` dùng để trực tiếp đọc cả ảnh vào và tìm các file định dạng nhãn (`.txt`).
- Nhằm tránh ảnh hưởng bởi việc mất cân bằng dữ liệu của các nhãn (imbalanced dataset), quá trình đã tính toán trọng số `class_weights` và sử dụng bộ phân phối `WeightedRandomSampler` trong khai báo của `DataLoader` đối với tập học (Train DataLoader). Việc này giúp các nhãn ít xuất hiện cũng có cơ hội được lấy ngang bằng nhau.

```python
class_weights = 1. / (np.array(class_counts) + 1e-6) 
sample_weights = [class_weights[y] for y in train.labels]
sampler = WeightedRandomSampler(weights=sample_weights, num_samples=len(sample_weights), replacement=True)

trn_dl = DataLoader(train, batch_size=128, sampler=sampler, num_workers=0, pin_memory=True) 
```

### Xây dựng kiến trúc mô hình Model CNN
Hệ thống CNN được thiết kế trên một dãy tuần tự `nn.Sequential` với 5 khối chập liên tiếp thực thi chức năng rút trích đặc trưng hình ảnh:
1. `Conv2d` (3 channels -> 32 filters) -> `BatchNorm2d` -> `ReLU` -> `MaxPool2d(2)`
2. `Conv2d` (32 -> 64 filters) -> `BatchNorm2d` -> `ReLU` -> `MaxPool2d(2)`
3. `Conv2d` (64 -> 128 filters) -> `BatchNorm2d` -> `ReLU` -> `MaxPool2d(2)`
4. `Conv2d` (128 -> 256 filters) -> `BatchNorm2d` -> `ReLU` -> `MaxPool2d(2)`
5. `Conv2d` (256 -> 512 filters) -> `BatchNorm2d` -> `ReLU` -> `MaxPool2d(2)`

- Khối phân loại đa lớp (Classification) được nối liền với cấu trúc:
  - Lớp `Flatten()` để kéo phẳng tensor n chiều về một vector kích thước `512 * 4 * 4`.
  - Lớp tuyến tính `Linear` với số chiều từ (8192) về cấu trúc (512 neuron) -> kích hoạt `ReLU`.
  - Lớp `Dropout(0.5)` loại bỏ ngẫu nhiên 50% tham số để chặn điểm quá khớp.
  - Lớp Linear xuất ra (Output) tùy thuộc số lớp cấu hình của file config (tương ứng biến `num_classes`).

```python
model = nn.Sequential( 
    nn.Conv2d(3, 32, kernel_size=3, padding=1),
    nn.BatchNorm2d(32),
    nn.ReLU(inplace=True),
    nn.MaxPool2d(2),
    # ... (Các lớp Conv2d, BatchNorm, ReLU, MaxPool lặp lại) ...
    nn.Conv2d(256, 512, kernel_size=3, padding=1),
    nn.BatchNorm2d(512),
    nn.ReLU(inplace=True),
    nn.MaxPool2d(2),

    nn.Flatten(),
    nn.Linear(512 * 4 * 4, 512), 
    nn.ReLU(inplace=True),
    nn.Dropout(0.5),
    nn.Linear(512, num_classes)
).to(device) 
```

### Logic Huấn luyện (Training)
- Thời gian đào tạo: **80 Epochs** cùng quá trình tải nhóm `batch_size` là **128**.
- **Hàm mất mát (Loss Function):** Sử dụng `CrossEntropyLoss` với cơ chế làm mịn hạn chế sai số nhãn (Label smoothing = 0.1).
- **Trình tối ưu hóa (Optimizer):** Hàm `Adam` với learning rate ban đầu r = 1e-3, weight decay = 1e-4 để chuẩn hóa regularization.
- **Trình điều chỉnh learning rate (Scheduler):** Dùng `ReduceLROnPlateau` với hệ số suy giảm (factor) là 0.5. Nếu trong khoảng 5 vòng liền (patience=5) mà hàm validation loss không có sự cải thiện thì LR tự được hạ xuống đi một nửa.
- Trong suốt vòng lặp, ở điểm kết thúc mỗi epoch mô hình tự động cập nhật hệ số của độ chính xác cao nhất (Best Validation Accuracy) và nếu phát hiện sự tối ưu mới sẽ lưu bộ trọng số (weights) lại theo phương thức `state_dict` vào cấu hình tệp `best_cnn_model.pth`.

```python
loss_fn = nn.CrossEntropyLoss(label_smoothing=0.1)
optimizer = Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5)

# Lưu model tốt nhất trong quá trình vòng lặp training
if val_epoch_accuracy > best_val_acc:
    best_val_acc = val_epoch_accuracy
    torch.save(model.state_dict(), best_model_path)
```

## 3. Kết quả đánh giá (Độ chính xác theo con số) 

Sau quá trình xử lý, bản báo cáo logging lấy trực tiếp từ `PLR.ipynb` cho thấy những dữ liệu cấu tạo và độ chính xác thực tế như sau:

**Số lượng kho ảnh phân bổ trong Data:**
- Tập huấn luyện (Train): **18.649** ảnh và nhãn.
- Tập kiểm định (Validation): **2.113** ảnh và nhãn.
- Tập kiểm tra thực tế (Test): **2.246** ảnh và nhãn.

**Quá trình phát triển Model và thông số điểm dừng (Epoch 80/80):**
- Độ chính xác tập huấn luyện (Train Accuracy): **97.52%** (Train Loss: 0.5399)
- Độ chính xác tập kiểm định (Validation Accuracy): **90.58%** (Val Loss: 0.6511)

Do sự biến thiên qua từng Epochs, quá trình học sâu đã phát hiện đỉnh tổng quát hóa trơn tru tại giai đoạn **Epoch 70**. Đây cũng là khoảng thời gian ghi lại trạng thái tốt nhất:
- Mức tiêu hao kiểm định (Validation Loss): **0.6565**
- Độ chính xác tập kiểm định đỉnh cao (Validation Accuracy): **90.77%**

**Kết quả đánh giá trên tập Kiểm tra (Test):**
Sau khi tải lại model mang đặc điểm tốt nhất (file save lưu được từ Epoch 70), quá trình đưa hình ảnh hoàn toàn trong tập test qua thuật toán để mang đi tiên đoán (inference) mang lại độ chính xác đáng kỳ vọng. Dựa trên 2.246 hình được chấm điểm:
* Độ chính xác trên tập kiểm tra độc lập (Test Accuracy): **92.88%**
