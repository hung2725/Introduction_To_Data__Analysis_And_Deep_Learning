# NHẬP MÔN PHÂN TÍCH DỮ LIỆU VÀ HỌC SÂU

- **Sinh Viên Thực Hiên:** Phạm Thế Hùng
- **MSSV:** 2374802010164
- **Môn Học:** Nhập môn phân tích dữ liệu và học sâu
- **Giảng viên:** Nguyễn Thái Anh

## Lab 03

## Công nghệ sử dụng
- **pandas**: đọc dữ liệu, xử lý thiếu/dup, biến đổi dạng bảng
- **numpy**: hỗ trợ xử lý giá trị thiếu  và tính toán
- **seaborn**: import để phục vụ trực quan hóa (trong notebook có sẵn, phần chính vẫn là làm sạch dữ liệu)

## Cách hoạt động

Notebook làm sạch dữ liệu theo các bước “đi từ thô → sạch” như sau:

- **Đọc file CSV + gắn header**: dữ liệu gốc bị thiếu tiêu đề cột nên code tự đặt tên cột để dễ hiểu (`Id`, `Name`, `Age`, `Weight`, `m0006`...).
- **Tách họ tên**: cột `Name` được tách thành `Firstname` và `Lastname`, sau đó bỏ cột `Name`.
- **Chuẩn hóa cân nặng**:
  - Nếu gặp đơn vị **lbs** thì đổi sang **kgs** (xấp xỉ \(kg = lb/2.2\)).
  - Giữ format dạng chuỗi kiểu `"70kgs"`.
- **Xóa dòng rỗng hoàn toàn**: loại các dòng mà toàn bộ giá trị đều `NaN`.
- **Xóa dữ liệu trùng**: loại bản ghi bị lặp dựa trên `Firstname`, `Lastname`, `Age`, `Weight`.
- **Làm sạch ký tự lạ trong tên**: loại các ký tự không thuộc ASCII trong `Firstname`/`Lastname` (để đồng nhất dữ liệu).
- **Điền thiếu cho `Age`**: nếu `Age` bị thiếu thì thay bằng **giá trị trung bình** của cột `Age`.
- **Chuyển dữ liệu từ “rộng” sang “dài”**:
  - Các cột nhịp tim dạng `m0006`, `f0612`, ... được “melt” thành 1 cột **`PulseRate`**
  - Tách thêm 2 thông tin:
    - **`Sex`**: `m` hoặc `f`
    - **`Time`**: khoảng giờ dạng `00-06`, `06-12`, `12-18`
- **Xử lý thiếu trong `PulseRate`**:
  - Dấu `-` được xem như thiếu dữ liệu (`NaN`)
  - Sau đó điền thiếu theo thứ tự ưu tiên (ví dụ: trung bình của giá trị liền trước/liền sau cùng người, trung bình của người đó, trung bình theo giới tính, ...).
- **Sắp xếp & xuất file**: chuẩn hóa thứ tự cột và lưu kết quả ra CSV.

## Kết quả

- Tạo file dữ liệu sạch: `patient_heart_rate_clean.csv`
- Dữ liệu cuối cùng có các cột chính:
  - `Id`, `Firstname`, `Lastname`, `Age`, `Weight`, `Sex`, `Time`, `PulseRate`


