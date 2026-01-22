# NHẬP MÔN PHÂN TÍCH DỮ LIỆU VÀ HỌC SÂU

- **Sinh Viên Thực Hiên:** Phạm Thế Hùng
- **MSSV:** 2374802010164
- **Môn Học:** Nhập môn phân tích dữ liệu và học sâu
- **Giảng viên:** Nguyễn Thái Anh

## Lab 02

## Công nghệ sử dụng
- **pandas**: Xử lý và phân tích dữ liệu dạng bảng
- **numpy**: Tính toán số học và thống kê
- **matplotlib**: Vẽ biểu đồ cơ bản (bar, pie, line, scatter)
- **seaborn**: Trực quan hóa dữ liệu nâng cao (boxplot, pairplot, lmplot)
- **scipy.stats**: Phân tích thống kê và kiểm định phân phối

## Cách hoạt động

### Phần 1: Thống kê dữ liệu
- Sắp xếp dữ liệu: Sắp xếp điểm DH1 tăng dần và điểm DH2 theo nhóm giới tính
- Pivot Table: Tạo bảng tổng hợp thống kê (count, sum, mean, median, min, max, std, Q1, Q2, Q3) của điểm DH1 theo:
   - Khối thi (KT)
   - Khối thi và Khu vực (KT, KV)
   - Khối thi, Khu vực và Dân tộc (KT, KV, DT)

### Phần 2: Trình bày dữ liệu
- Biến GT: Trực quan hóa bằng bar chart, pie chart và area chart
- Biến US_TBM: Thống kê mô tả cho US_TBM1, US_TBM2, US_TBM3
- Lọc dữ liệu: 
   - Học sinh nam theo dân tộc
   - Học sinh nam dân tộc Kinh với điều kiện điểm (DH1 >= 5.0, DH2 >= 4.0, DH3 >= 4.0) theo khu vực

### Phần 3: Trực quan hóa dữ liệu theo nhóm phân loại
- Trực quan dữ liệu học sinh nữ theo nhóm xếp loại (XL1, XL2, XL3)
- Biểu đồ kết quả xét tuyển (KQXT) theo khối thi và khu vực
- Biểu đồ số lượng thí sinh theo khu vực và khối thi (stacked bar)
- Biểu đồ đậu/rớt theo khối thi, khu vực, dân tộc và giới tính

### Phần 4: Trực quan hóa dữ liệu nâng cao
- Biểu đồ đường đơn giản cho biến T1
- Phân loại T1 thành 4 nhóm: kém (k), trung bình (tb), khá (kh), giỏi (g)
- Biểu đồ đường đa nhóm và biểu đồ drop-line cho T1 theo phân loại

### Phần 5: Mô tả dữ liệu và khảo sát phân phối
- Phân phối biến T1: 
   - Box plot và Histogram
   - QQ-Plot để kiểm tra phân phối chuẩn
- Phân phối T1 theo nhóm: Histogram cho từng nhóm phân loại
- Tương quan:
   - Scatter plot giữa DH1 và T1
   - Tương quan DH1 vs T1 theo khu vực (lmplot)
   - Pair plot giữa các biến DH1, DH2, DH3

## Kết quả

### Phần 1: Thống kê dữ liệu

**Kết quả sắp xếp:**
- Dữ liệu được sắp xếp điểm DH1 từ thấp đến cao
- Dữ liệu được sắp xếp điểm DH2 tăng dần theo từng nhóm giới tính (M/F)

**Kết quả Pivot Table:**
- **Tổng điểm DH1**: 374.0 điểm
- **Pivot theo KT và DT**: 
  - Dân tộc Kinh (0.0) có điểm trung bình cao nhất ở khối C (5.66), thấp nhất ở khối A1 (2.92)
  - Các chỉ số thống kê (Q1, Q2, Q3, mean, median, std) được tính toán cho từng nhóm
- **Pivot theo KT, KV**: Bảng tổng hợp chi tiết theo khối thi và khu vực
- **Pivot theo KT, KV, DT**: Bảng tổng hợp đầy đủ nhất với 3 tiêu chí phân loại

### Phần 2: Trình bày dữ liệu

**Kết quả biến GT (Giới tính):**
- Biểu đồ bar, pie và area chart thể hiện phân bố giới tính trong dữ liệu

**Kết quả biến US_TBM:**
- Thống kê mô tả (count, mean, std, min, 25%, 50%, 75%, max) cho 3 biến US_TBM1, US_TBM2, US_TBM3

**Kết quả lọc dữ liệu:**
- **Học sinh nam theo dân tộc**: Thống kê số lượng học sinh nam theo từng dân tộc
- **Học sinh nam dân tộc Kinh đạt điều kiện**:
  - Khu vực 1: 2 học sinh
  - Khu vực 2: 2 học sinh  
  - Khu vực 2NT: 2 học sinh
  - **Tổng**: 6 học sinh nam dân tộc Kinh đạt điều kiện (DH1 >= 5.0, DH2 >= 4.0, DH3 >= 4.0)

### Phần 3: Trực quan hóa dữ liệu theo nhóm phân loại

**Kết quả:**
- **Học sinh nữ theo xếp loại**: Bảng unstacked thể hiện phân bố học sinh nữ theo các nhóm xếp loại XL1, XL2, XL3
- **KQXT theo khối thi và khu vực**: Biểu đồ bar so sánh kết quả xét tuyển của các khối A, A1, B ở khu vực 1 và 2
- **Số lượng thí sinh theo KV và KT**: Biểu đồ stacked bar cho thấy phân bố thí sinh theo khu vực trong từng khối thi
- **Đậu/Rớt theo khối thi**: Biểu đồ so sánh tỷ lệ đậu/rớt giữa các khối thi (A, A1, B, C, D1)
- **Đậu/Rớt theo khu vực**: Biểu đồ so sánh tỷ lệ đậu/rớt giữa các khu vực (1, 2, 2NT)
- **Đậu/Rớt theo dân tộc**: Biểu đồ so sánh tỷ lệ đậu/rớt theo các nhóm dân tộc
- **Đậu/Rớt theo giới tính**: Biểu đồ so sánh tỷ lệ đậu/rớt giữa nam và nữ

### Phần 4: Trực quan hóa dữ liệu nâng cao

**Kết quả:**
- **Biểu đồ đường T1**: Biểu đồ đường đơn giản thể hiện phân bố số lượng thí sinh theo điểm T1
- **Phân loại T1**: 
  - Kém (k): T1 < 5
  - Trung bình (tb): 5 ≤ T1 < 7
  - Khá (kh): 7 ≤ T1 < 8
  - Giỏi (g): T1 ≥ 8
- **Tần số phân loại**: Thống kê số lượng thí sinh trong từng nhóm phân loại
- **Biểu đồ đường đa nhóm**: Biểu đồ đường với nhiều đường cho từng nhóm phân loại
- **Biểu đồ drop-line**: Biểu đồ drop-line với scatter points thể hiện phân bố T1 theo từng nhóm phân loại

### Phần 5: Mô tả dữ liệu và khảo sát phân phối

**Kết quả phân phối T1:**
- **Box plot**: Xác định được các giá trị outliers và phân bố của điểm T1
- **Histogram**: Thể hiện hình dạng phân phối của điểm T1
- **QQ-Plot**: Kiểm tra tính chuẩn của phân phối điểm T1 (so sánh với phân phối chuẩn)

**Kết quả phân phối T1 theo nhóm:**
- Histogram riêng biệt cho từng nhóm phân loại (k, tb, kh, g) cho thấy sự khác biệt trong phân phối điểm

**Kết quả tương quan:**
- **Tương quan DH1 vs T1**: 
  - Scatter plot thể hiện mối quan hệ giữa điểm DH1 và T1
  - Hệ số tương quan được tính toán và hiển thị trên biểu đồ
- **Tương quan theo khu vực**: 
  - Lmplot với đường hồi quy cho từng khu vực
  - So sánh mối quan hệ DH1-T1 giữa các khu vực khác nhau
- **Tương quan giữa DH1, DH2, DH3**: 
  - Pair plot ma trận 3x3 thể hiện:
    - Histogram phân phối của từng biến (đường chéo)
    - Scatter plot tương quan giữa các cặp biến (ngoài đường chéo)
    - Hệ số tương quan giữa các biến điểm thi


