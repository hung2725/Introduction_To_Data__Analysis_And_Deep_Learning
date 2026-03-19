# DEEP LEARNING

- **Sinh viên thực hiện:** Phạm Thế Hùng  
- **MSSV:** 2374802010164  
- **Môn học:** Giới Thiệu Học Sâu  
- **Giảng viên:** Nguyễn Thái Anh


## Phân Loại Chó & Mèo bằng CNN

### Công nghệ sử dụng
- **Python 3**
- **PyTorch**  xây dựng và huấn luyện CNN
- **Torchvision**  tải và tiền xử lý dữ liệu ảnh
- **NumPy**  tính toán độ chính xác
- **Matplotlib** — vẽ biểu đồ Loss và Accuracy

- **Link dataset**: https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset

### Cách hoạt động

- **Tiền xử lý**: resize ảnh về `128×128`,lật ngang, xoay ±10°, chuẩn hóa, batch size `128`
- **Kiến trúc CNN**: 4 khối `Conv2D → BatchNorm → ReLU → MaxPool`, sau đó `Flatten → Linear(512) → Dropout(0.5) → Linear(2)`
- **Huấn luyện**: Adam optimizer (`lr=1e-3`, `weight_decay=5e-4`), CrossEntropyLoss, 50 epochs

### Kết quả
> **Độ chính xác cuối cùng trên tập test: 90.11%**
