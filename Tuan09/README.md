# NHẬP MÔN PHÂN TÍCH DỮ LIỆU VÀ HỌC SÂU

- **Sinh Viên Thực Hiên:** Phạm Thế Hùng
- **MSSV:** 2374802010164
- **Môn Học:** Nhập môn phân tích dữ liệu và học sâu
- **Giảng viên:** Nguyễn Thái Anh

## Lab 07 Tuần 9

## 1. Công Nghệ Được Sử Dụng
- **Python** 
- **NLTK (Natural Language Toolkit):** 
- **BeautifulSoup (bs4):** 
- **Urllib:** 
- **Bộ dữ liệu áp dụng:** 

## 2. Chi Tiết Hoạt Động & Code Từng Phần

### Phần 1: Giới thiệu thư viện NLTK
- **Cách hoạt động:** Cài đặt, import và tải các gói dữ liệu cơ bản. Sau đó, tải về tác phẩm `shakespeare-macbeth.txt` từ bộ dữ liệu có sẵn `gutenberg`.
- **Code:**
```python
import nltk
gb = nltk.corpus.gutenberg  
print("Gutenberg files : ", gb.fileids())
macbeth = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
len(macbeth)
```
- **Kết quả:** Hiển thị 18 file có trong Gutenberg corpus. Tác phẩm Macbeth có tổng số từ/dấu câu là `23140`. Kịch bản bắt đầu bằng `['[', 'The', 'Tragedie', 'of', 'Macbeth', 'by', 'William', 'Shakespeare', '1603', ']']`.

### Phần 2: Tìm 1 cụm từ với NLTK (Search)
- **Cách hoạt động:** Cho phép tra tìm văn cảnh mà một từ vựng xác định xuất hiện. Thử với từ khóa "Stage" ta dùng các hàm `concordance()` (ngữ cảnh), `common_contexts()` (bối cảnh chung) và `similar()` (tương đồng từ loại). 
- **Code:**
```python
text = nltk.Text(macbeth) 
text.concordance('Stage')
text.similar('Stage') 
```
- **Kết quả:** Máy báo `Displaying 3 of 3 matches:` cho từ "Stage" nằm trong 3 đoạn văn. Các từ giống cấu trúc cũng được liệt kê: `day time face warre ayre king bleeding man reuolt serieant like...`

### Phần 3: Phân tích tần số từ và Loại bỏ Stopwords
- **Cách hoạt động:** Khởi tạo lớp `FreqDist` để đếm số lượng. Sau đó, import thư viện Stopwords (những từ ít sắc thái nghĩa như is, the, are) và bộ dấu câu gỡ bỏ đi để văn bản thực sự sạch phục vụ bước tìm keyword.
- **Code:**
```python
# Lấy ra bộ 198 từ vô nghĩa (stopwords) tiếng Anh
sw = set(nltk.corpus.stopwords.words('english'))  

import string 
punctuation = set(string.punctuation)  
macbeth_filtered2 = [w.lower() for w in macbeth if w.lower() not in sw and w.lower() not in punctuation]  
fd = nltk.FreqDist(macbeth_filtered2)  
fd.most_common(10) 
```
- **Kết quả:** Quá trình lọc từ bộ phim `23140` phần tử thu hẹp văn bản lại chỉ còn `14946`. Kết quả sau cùng chỉ ra 10 keyword xuất hiện nhiều nhất là: `[('macb', 137), ('haue', 122), ('thou', 90), ('enter', 81), ('shall', 68), ('macbeth', 62), ('vpon', 62), ('thee', 61), ('macd', 58), ('vs', 57)]`.

### Phần 4: Lựa chọn từ theo điều kiện
- **Cách hoạt động:** Dùng logic của List Comprehension trong Python để lẩy ra các từ rất dài (>12 kí tự) hoặc từ chứa đuôi tính từ 'ious'.
- **Code:**
```python
long_words = [w for w in macbeth if len(w)> 12] 
ious_words = set([w for w in macbeth if 'ious' in w]) 
```
- **Kết quả:** Lục được chính xác các từ vượt quá 12 kí tự: `['Assassination', 'Chamberlaines', 'Distinguishes', 'Gallowgrosses', 'Metaphysicall'...]`. Tìm được các từ đuôi ious: `['Auaricious', 'Gracious', 'Industrious', 'Iudicious'...]`.

### Phần 5: Phân tích cụm (Bigrams và Trigrams)
- **Cách hoạt động:** Tìm xem những cặp 2 từ (bigrams) và 3 từ (trigrams) nào hay đi liền nhau theo xác suất. Thường dùng trong dự đoán hành vi.
- **Code:**
```python
tgrms = nltk.FreqDist(nltk.trigrams (macbeth_filtered2)) 
tgrms.most_common(5) 
```
- **Kết quả:** Cụm 3 từ đi cùng nhau top 1 là gõ cửa 3 lần `(('knock', 'knock', 'knock'), 6)`, theo sau là `(('enter', 'macbeth', 'macb'), 5)` và `(('enter', 'three', 'witches'), 4)`.

### Phần 6 và 7: Đọc văn bản trên mạng và trích xuất HTML
- **Cách hoạt động:** NLTK thường đi chung với Urllib để tải raw data từ internet, kết hợp BeautifulSoup phân giải HTML sang đoạn string sạch bỏ đi các thẻ code rối rắm.
- **Code:**
```python
# Tải tài liệu
url = "http://www.gutenberg.org/files/2554/2554-0.txt" 
response = request.urlopen(url) 
raw = response.read().decode('utf-8-sig')

# Cào web
from bs4 import BeautifulSoup 
raw_html = BeautifulSoup(html, "lxml").get_text() 
```
- **Kết quả:** Đã tải và decode thành công đầu text quyển sách "`*** START OF THE PROJECT GUTENBERG EBOOK 2554 ***\n\n\n\n\nCRIME AND PUNISHMENT\n`"

### Phần 8: Phân Tích Cảm Xúc Người Dùng (Sentiment Analysis)
- **Cách hoạt động:** Lấy tệp thư mục `movie_reviews` huấn luyện máy phân biệt nhận xét tốt xấu (Positive/Negative). Máy đọc kho văn bản 2000 bài làm vector `featuresets` => Chuyển đến thuật toán `NaiveBayesClassifier` để tự chạy học (train) tính năng. 
- **Code:**
```python
train_set, test_set = featuresets[1500:], featuresets[:500] 
classifier = nltk.NaiveBayesClassifier.train(train_set) 
print(nltk.classify.accuracy(classifier, test_set)) 
classifier.show_most_informative_features(5) 
```
- **Kết quả:** Đạt tỷ lệ chính xác (Accuracy): `0.764` (76.4%). Hệ thống in ra bằng chứng toán học cực rõ ràng để tiên đoán - VD từ "warm" (ấm áp) nhận phân loại `pos : neg = 10.4 : 1.0` (Khả năng khen gấp 10.4 lần chê bai).

---
### Phần 9: Các Bài Tập Áp Dụng Chuyên Sâu

Dưới đây là lời giải cho các bài tập bổ sung về cách áp dụng NLTK:

**1. Liệt kê tổng số kho dữ liệu (corpus):**
```python
corpus_names = [corpus for corpus in dir(nltk.corpus) if not corpus.startswith('_')]
print(f"Tổng số corpus tìm thấy: {len(corpus_names)}")
```
- **Kết quả:** `Tổng số corpus tìm thấy: 157`

**2 & 3. Thống kê độ lớn bộ Stopwords theo quốc gia:**
```python
languages = stopwords.fileids()
print(len(languages))
print("25 Stopwords tiếng Anh:", stopwords.words('english')[:25])
```
- **Kết quả:** Có `33` ngôn ngữ. Stopwords tiếng Pháp ví dụ có : `['au', 'aux', 'avec', 'ce', 'ces'...]`. Còn tiếng Anh có `['a', 'about', 'above'...]`.

**4 & 5. Loại bỏ & Tùy chỉnh danh sách Stopwords thủ công:**
```python
vb = "This is an example sentence to demonstrate the removal of stopwords using NLTK in Python."
# Giữ lại các từ is, to, the khỏi bộ tẩy xóa
tu_can_giu_lai = ['is', 'to', 'the'] 
for tu in tu_can_giu_lai:
    if tu in stop_words_tuy_chinh: stop_words_tuy_chinh.remove(tu)
```
- **Kết quả:** Từ một câu 14 từ, lệnh đã lọc câu văn gốc xuống chỉ còn: `example sentence demonstrate removal stopwords using NLTK Python .` Khi áp lệnh tùy chỉnh giữ lại chữ thì thu được câu: `is example sentence to demonstrate the removal stopwords using NLTK Python .`

**6 & 7. Sử dụng từ điển WordNet:**
Dùng nltk tự động tìm nghĩa và lấy mảng từ vựng đồng nghĩa, trái nghĩa từ siêu từ điển có trên WordNet Wikipedia.
```python
synsets = wn.synsets("computer")
print(synsets[0].definition())
print(list(dong_nghia)[:10]) # tìm từ đồng nghĩa bằng lemma()
```
- **Kết quả:** Từ khóa `computer` trả về định nghĩa chuẩn `a machine for performing calculations automatically`. Từ khóa "good" trả về từ trái nghĩa (Antonyms) là: `['bad', 'ill', 'badness', 'evil', 'evilness']`.

**8. Tra cứu bộ Tagset (Nhãn từ loại):**
```python
nltk.help.upenn_tagset('NN')
nltk.help.upenn_tagset('NN.*')
```
- **Kết quả:** Tra cứu và giải nghĩa các thẻ Part-of-Speech (Nhãn từ vựng). Chi tiết hiển thị `NN` là danh từ chung số ít (noun, common, singular or mass), `NNS` là danh từ số nhiều, `NNP` là danh từ riêng số ít...

**9 & 10. Tìm độ giống nhau của 2 biểu thức (Similarity):**
```python
do_tuong_dong_1_2 = wn.synset('cat.n.01').wup_similarity(wn.synset('dog.n.01'))
```
- **Kết quả:** Đo lường sự giống nhau qua thuật toán Wu-Palmer:
Mèo và Chó (cat vs dog): `0.8571` (Rất gần gũi ở nhãn động vật)
Mèo và Xe Ô Tô (cat vs car): `0.3200`
Chạy và Đi bộ (run vs walk): `0.2857`

**11, 12, 13. Phân biệt người dùng dựa trên corpus "Names":**
```python
ten_nam = names.words('male.txt')
danh_sach_nhan = [(ten, 'male') for ten in ten_nam] + [(ten, 'female') for ten in ten_nu]
random.shuffle(danh_sach_nhan)
mang_ky_tu_cuoi = [(ten[-1].lower(), gioi_tinh) for ten, gioi_tinh in danh_sach_nhan]
```
- **Kết quả:** Đếm được `Tổng số tên nam: 2943` và `Tổng số tên nữ: 5001`. Từ dữ liệu text, hệ thống đã trích ra thuật toán ánh xạ Ký tự cuối và Nhãn người dùng như `('e', 'female')`, `('a', 'female')`, `('k', 'male')`, `('y', 'male')` dùng phục vụ ML. 
