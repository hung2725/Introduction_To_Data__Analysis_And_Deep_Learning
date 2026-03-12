# NHẬP MÔN PHÂN TÍCH DỮ LIỆU VÀ HỌC SÂU

- **Sinh Viên Thực Hiên:** Phạm Thế Hùng
- **MSSV:** 2374802010164
- **Môn Học:** Nhập môn phân tích dữ liệu và học sâu
- **Giảng viên:** Nguyễn Thái Anh

## Lab 05

## 1. Công nghệ sử dụng

*   **Ngôn ngữ lập trình:** Python
*   **Thư viện:**
    *   `PyTorch`: Dùng để xây dựng kiến trúc mô hình mạng nơ-ron, định nghĩa hàm mất mát (loss function), và các thuật toán tối ưu hóa (optimizer).
    *   `Torchvision`: Dùng để tải bộ dữ liệu Fashion MNIST.
    *   `NumPy`: Xử lý mảng và tính toán toán học.
    *   `Matplotlib`: Trực quan hóa dữ liệu, vẽ biểu đồ hàm mất mát và độ chính xác trong quá trình huấn luyện.

## 2. Cách hoạt động

1.  **Tải và Phân tích Dữ liệu:** 
    *   Tải bộ dữ liệu Fashion MNIST bao gồm các hình ảnh kích thước 28x28 grayscale của 10 lớp quần áo khác nhau (T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot).
    *   Phân chia dữ liệu thành tập huấn luyện (training set) và tập xác thực (validation set).
2.  **Chuẩn bị Dữ liệu (Data Preprocessing):**
    *   Xây dựng lớp `FMNISTDataset` (kế thừa từ `torch.utils.data.Dataset`) để nạp dữ liệu.
    *   Dữ liệu ảnh được chuẩn hóa bằng cách chia giá trị pixel cho 255 (khoảng giá trị từ 0 đến 1) và làm phẳng (flatten) thành vector 1D kích thước 784 (28*28) để làm đầu vào cho mạng ANN.
    *   Sử dụng `DataLoader` để chia dữ liệu thành các mini-batch phục vụ cho quá trình huấn luyện.
3.  **Xây dựng Kiến trúc Mô hình:**
    *   Xây dựng một mạng nơ-ron truyền thẳng (Feed-forward Neural Network) với cấu trúc:
        *   Lớp đầu vào: Nhận vector kích thước 784.
        *   Lớp ẩn (Hidden layer): 1000 nơ-ron, sử dụng hàm kích hoạt ReLU.
        *   Lớp đầu ra: 10 nơ-ron, tương ứng với 1 lớp phân loại (không dùng Softmax ở đây vì hàm mất mát CrossEntropyLoss đã tích hợp sẵn).
4.  **Huấn luyện và Đánh giá (Training & Validation):**
    *   **Hàm mất mát (Loss Function):** Sử dụng `CrossEntropyLoss` phù hợp cho bài toán phân loại đa lớp.
    *   **Việc thử nghiệm:** Quá trình huấn luyện trải qua nhiều cấu hình khác nhau để so sánh hiệu quả:
        *   *Thử nghiệm chuẩn hóa dữ liệu:* Đánh giá tác động của việc chia giá trị pixel cho 255.
        *   *Thử nghiệm kích thước bó (Batch Size):* So sánh giữa Batch Size = 32 và Batch Size = 10,000.
        *   *Thử nghiệm thuật toán tối ưu (Optimizer):* So sánh giữa Gradient Descent ngẫu nhiên (SGD) và Adam Optimizer (cùng với Learning Rate = 0.01).
    *   Trong quá trình huấn luyện, tính toán và lưu lại giá trị mất mát (Loss) và độ chính xác (Accuracy) trên cả tập huấn luyện và tập xác thực qua từng epoch.

## 3. Kết quả

- Chuẩn hóa dữ liệu: Việc chia dữ liệu độ pixel cho 255 giúp mô hình hội tụ tốt hơn và có thể đạt độ chính xác cao hơn.
- Kích thước bó (Batch Size)
    *   Kích thước bó nhỏ (ví dụ: 32) giúp mô hình cập nhật trọng số thường xuyên hơn, dẫn đến sự hội tụ nhanh hơn về mặt số lượng epoch, tuy nhiên có thể gây ra hiện tượng dao động (noise) trong biểu đồ mất mát.
    *   Kích thước bó lớn (ví dụ: 10,000) tính toán gradient mượt mà hơn nhưng mỗi epoch tốn thời gian hơn và mất nhiều epoch hơn để đạt cùng một mức độ hội tụ.
- Trình tối ưu hóa (Optimizer)
    *   So sánh với SGD, thuật toán **Adam** cho thấy tốc độ học và khả năng hội tụ nhanh hơn, thường mang lại độ chính xác cao hơn trong cùng một số lượng epoch trên bộ dữ liệu này.
    *   Với cấu hình Adam Optimizer (lr=1e-2) và Batch Size = 32, mô hình đạt được kết quả huấn luyện (Training) và xác thực (Validation) tốt trên đồ thị, độ chính xác ổn định sau khoảng 10 epochs.
