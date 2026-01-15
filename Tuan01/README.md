# NHẬP MÔN PHÂN TÍCH DỮ LIỆU VÀ HỌC SÂU

- **Sinh Viên Thực Hiên:** Phạm Thế Hùng
- **MSSV:** 2374802010164
- **Môn Học:** Nhập môn phân tích dữ liệu và học sâu
- **Giảng viên:** Nguyễn Thái Anh

## Lab 01

## Công nghệ sử dụng

- **Python 3**: Ngôn ngữ dùng để code chính
- **Pandas**: Thư viện xử lý và phân tích dữ liệu
- **NumPy**: Thư viện tính toán số học
- **Jupyter Notebook**: Môi trường phát triển và chạy code

## Cách hoạt động

### 1. Tải dữ liệu
- Đọc file CSV `dulieuxettuyendaihoc.csv` chứa thông tin điểm số của 100 học sinh
- Dữ liệu bao gồm điểm các môn học từ lớp 10, 11, 12 và thông tin xét tuyển

### 2. Xử lý dữ liệu thiếu
- **Cột DT**: Điền giá trị 0 cho các ô trống
- **Các cột điểm số**: Điền giá trị trung bình (mean) của cột đó cho các ô trống

### 3. Tính toán điểm trung bình môn
- Tạo 3 biến: **TBM1**, **TBM2**, **TBM3** tương ứng với lớp 10, 11, 12
- Công thức tính: 
  ```
  TBM = (T*2 + L + H + S + V*2 + X + D + N) / 10
  ```

### 4. Xếp loại học lực
- Tạo các biến **XL1**, **XL2**, **XL3** dựa trên TBM
- Thang điểm:
  - **Y** (Yếu): < 5.0
  - **TB** (Trung bình): 5.0 - 6.5
  - **K** (Khá): 6.5 - 8.0
  - **G** (Giỏi): 8.0 - 9.0
  - **XS** (Xuất sắc): ≥ 9.0

### 5. Chuyển đổi thang điểm
- Tạo các biến **US_TBM1**, **US_TBM2**, **US_TBM3** 
- Chuyển từ thang điểm 10 (Việt Nam) sang thang điểm 4 (Mỹ)
- Công thức: `US_TBM = (TBM / 10) * 4`

### 6. Xác định kết quả xét tuyển
- Tạo biến **KQXT** (Kết quả xét tuyển)
- **1** = Đậu, **0** = Rớt
- Công thức tính điểm xét tuyển tùy theo khối:
  - Khối A, A1: `(DH1*2 + DH2 + DH3) / 4`
  - Khối B: `(DH1 + DH2*2 + DH3) / 4`
  - Khối khác: `(DH1 + DH2 + DH3) / 3`
- Điều kiện đậu: Điểm xét tuyển ≥ 5.0

### 7. Lưu kết quả
- xuất ra file mới đẫ được xư lý `processed_dulieuxettuyendaihoc.csv`

## Kết quả

### 1. Tải dữ liệu
- **Kết quả**: Đã tải thành công 100 rows × 55 columns
- Hiển thị được 10 dòng đầu (STT 1-10) và 10 dòng cuối (STT 91-100) của dataset
- **Ví dụ dữ liệu đầu vào**:
  - STT = 1: T1 = 7.2, L1 = 7.3, H1 = 6.3, S1 = 7.3, V1 = 7.0, X1 =7.9, D1 = 7.3, N1 = 5.5, GT = F, DT = NaN, KV = 2NT, DH1 = 3.25, DH2 = 3.25, DH3 = 4.50, KT = A1
  - STT=100: T1=4.1, L1=5.2, H1=4.9, S1=5.3, V1=5.5, X1=5.4, D1=7.2, N1=5.4, GT=M, DT=NaN, KV=2NT, DH1=5.25, DH2=2.50, DH3=4.25, KT=C

### 2. Xử lý dữ liệu thiếu
- **Kết quả**: 
  - Tất cả giá trị NaN trong cột **DT** (100 giá trị) đã được thay bằng **0.0**
  - Tất cả giá trị NaN trong các cột điểm số đã được điền bằng giá trị trung bình (mean) của từng cột
  - Dataset sau xử lý: **100 rows × 55 columns**, không còn dữ liệu thiếu
- **Ví dụ sau xử lý**: STT=1 có DT=0.0 (thay vì NaN)

### 3. Tính toán điểm trung bình môn (TBM)
- **Kết quả**: Đã tạo thành công 3 cột mới cho 100 học sinh
- **Ví dụ kết quả** (5 dòng đầu):
  ```
  STT  TBM1   TBM2   TBM3
  1    7.00   7.54   7.01
  2    4.69   5.47   5.07
  3    5.77   5.38   6.04
  4    6.21   5.20   6.88
  5    6.50   6.36   6.99
  ```
- **Thống kê TBM1**: 
  - Min: 4.04, Max: 8.08
  - Std: 0.978
  - Số giá trị unique: 91

### 4. Xếp loại học lực
- **Kết quả**: Đã tạo thành công 3 cột xếp loại cho 100 học sinh
- **Ví dụ kết quả** (5 dòng đầu):
  ```
  STT  TBM1  XL1  TBM2  XL2  TBM3  XL3
  1    7.00   K   7.54   K   7.01   K
  2    4.69   Y   5.47  TB   5.07  TB
  3    5.77  TB   5.38  TB   6.04  TB
  4    6.21  TB   5.20  TB   6.88   K
  5    6.50   K   6.36  TB   6.99   K
  ```
- **Phân bố xếp loại**: Học sinh được phân loại thành **Y** (Yếu), **TB** (Trung bình), **K** (Khá), **G** (Giỏi), **XS** (Xuất sắc)
- **Ví dụ**: 
  - STT=1: XL1=K, XL2=K, XL3=K (đều xếp loại Khá)
  - STT=2: XL1=Y (Yếu), XL2=TB (Trung bình), XL3=TB (Trung bình)
  - STT=96: XL1=K, XL2=K, XL3=K
  - STT=97: XL1=Y, XL2=TB, XL3=TB
  - STT=99: XL1=Y, XL2=Y, XL3=TB

### 5. Chuyển đổi thang điểm
- **Kết quả**: Đã tạo thành công 3 cột điểm theo thang Mỹ cho 100 học sinh
- **Ví dụ kết quả** (5 dòng đầu):
  ```
  STT  TBM1   US_TBM1  TBM2   US_TBM2  TBM3   US_TBM3
  1    7.00   2.800    7.54   3.016    7.01   2.804
  2    4.69   1.876    5.47   2.188    5.07   2.028
  3    5.77   2.308    5.38   2.152    6.04   2.416
  4    6.21   2.484    5.20   2.080    6.88   2.752
  5    6.50   2.600    6.36   2.544    6.99   2.796
  ```
- **Ví dụ tính toán**: 
  - STT=1: TBM1=7.00 → US_TBM1=2.800 (7.00/10*4 = 2.8)
  - STT=1: TBM2=7.54 → US_TBM2=3.016 (7.54/10*4 = 3.016)

### 6. Xác định kết quả xét tuyển
- **Kết quả**: Đã tạo cột **KQXT** với giá trị 0 (rớt) hoặc 1 (đậu) cho 100 học sinh
- **Ví dụ kết quả** (5 dòng đầu):
  ```
  STT  KT   DH1    DH2    DH3    KQXT
  1    A1   3.25   3.25   4.50    0
  2    C    6.00   4.00   3.50    0
  3    C    5.00   6.75   4.00    1
  4    D1   4.25   4.25   5.25    0
  5    A    4.25   4.50   5.00    0
  ```
- **Giải thích ví dụ**:
  - STT=1 (khối A1): Điểm = (3.25*2 + 3.25 + 4.50)/4 = 3.5625 < 5.0 → **KQXT=0** (rớt)
  - STT=2 (khối C): Điểm = (6.00 + 4.00 + 3.50)/3 = 4.5 < 5.0 → **KQXT=0** (rớt)
  - STT=3 (khối C): Điểm = (5.00 + 6.75 + 4.00)/3 = 5.25 ≥ 5.0 → **KQXT=1** (đậu)

### 7. Lưu kết quả
- **Kết quả**: Xuất ra file mới  `processed_dulieuxettuyendaihoc.csv`
- **Dữ liệu đầu ra**: 
  - **100 rows** 100 học sinh
  - **Tổng cộng 65 cột** 55 cột gốc + 10 cột mới: TBM1, TBM2, TBM3, XL1, XL2, XL3, US_TBM1, US_TBM2, US_TBM3, KQXT
  - Không còn NaN

