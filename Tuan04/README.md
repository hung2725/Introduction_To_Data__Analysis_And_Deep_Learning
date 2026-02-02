# NHẬP MÔN PHÂN TÍCH DỮ LIỆU VÀ HỌC SÂU

- **Sinh Viên Thực Hiên:** Phạm Thế Hùng
- **MSSV:** 2374802010164
- **Môn Học:** Nhập môn phân tích dữ liệu và học sâu
- **Giảng viên:** Nguyễn Thái Anh

## Lab 04

## Công nghệ sử dụng
- **Thư viện**:
  - `pandas`: đọc, biến đổi dữ liệu dạng bảng
  - `numpy`: hỗ trợ xử lý giá trị thiếu và tính toán 
  - `seaborn`, `matplotlib`: trực quan hóa

## Cách hoạt động
1. **Đọc dữ liệu**
   - Đọc `titanic_disaster.csv` bằng `pd.read_csv(r"D:\Hoc_Tap\HK252\Phân Tích Dữ Liệu Và Học Sâu\Tuan04\titanic_disaster.csv", on_bad_lines='skip')`.

2. **Khảo sát dữ liệu thiếu**
   - Vẽ **heatmap** để quan sát missing values  `Age`, `Cabin`, `Embarked`

3. **Xử lý cột tên (Name)**
   - Tách `Name` thành 2 cột:
     - `firstName`: phần trước dấu phẩy
     - `secondName`: phần sau dấu phẩy
   - Xóa cột `Name` sau khi tách

4. **Chuẩn hóa cột giới tính**
   - Đổi `male -> M`, `female -> F`

5. **Điền giá trị thiếu cho Age**
   - Vẽ **boxplot** phân phối tuổi theo `Pclass`
   - Điền `Age` bị thiếu theo nhóm hạng vé (`Pclass`):
     - `Pclass = 1` -> 38
     - `Pclass = 2` -> 30
     - `Pclass = 3` -> 25
   - Vẽ lại **heatmap** để kiểm tra thiếu dữ liệu sau xử lý

6. **Tạo nhóm tuổi (Agegroup)**
   - Tạo cột `Agegroup` theo khoảng tuổi:
     - `age <= 12` -> `Kid`
     - `(12, 18]` -> `Teen`
     - `(18, 60]` -> `Adult`
     - `age > 60` -> `Older`

7. **Tách danh xưng (namePrefix)**
   - Tạo cột `namePrefix` bằng cách lấy danh xưng từ `secondName` (`Mr`, `Mrs`, `Miss`, `Master`)

8. **Tạo đặc trưng gia đình (familySize)**
   - `familySize = 1 + SibSp + Parch`

9. **Tạo đặc trưng Alone**
   - Dựa trên `familySize`:
     - nếu `familySize == 1` thì `Alone = 1` (đi một mình)
     - ngược lại `Alone = 0`

10. **Xử lý Cabin và tạo typeCabin**
   - Điền `Cabin` bị thiếu bằng chuỗi `Unknown`.
   - Tạo cột `typeCabin` = ký tự đầu của `Cabin` (`C85` -> `C`, `Unknown` -> `U`)

## Kết quả
  - `firstName`, `secondName`, `Agegroup`, `namePrefix`, `familySize`, `Alone`, `typeCabin`
- **Dữ liệu thiếu**:
  - `Age`: các giá trị thiếu được điền theo `Pclass` hạng vé với các mốc 38/30/25 tương ứng 1/2/3, sau đó kiểm tra lại bằng heatmap
  - `Cabin`: các giá trị thiếu được thay bằng `Unknown`
  - `Embarked`: quan sát thiếu dữ liệu heatmap chưa thấy bước điền thiếu rõ ràng trong phần code hiện tại
- **Đặc trưng mới đã tạo**:
  - `Agegroup`: phân loại tuổi theo 4 nhóm `Kid/Teen/Adult/Older` từ cột `Age`
  - `namePrefix`: danh xưng tách từ `secondName` (`Mr`, `Mrs`, `Miss`, `Master`)
  - `familySize`: số người đi cùng (1 + `SibSp` + `Parch`).
  - `Alone`: xác định đi một mình hay không (1 nếu `familySize == 1`).
  - `typeCabin`: ký tự đầu của `Cabin` để rút gọn thông tin ví dụ `C85` -> `C`, `Unknown` -> `U`
- **Biểu đồ  hiển thị**:
  - Heatmap missing values trước và sau khi xử lý cột `Age`
  - Boxplot phân phối `Age` theo `Pclass`

