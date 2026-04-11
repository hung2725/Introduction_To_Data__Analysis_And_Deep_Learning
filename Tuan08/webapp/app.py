import os
import io
from flask import Flask, request, jsonify, render_template
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
CLASSES = ['Sinh Học Phân Huỷ (Biodegradable)', 'Bìa Các-tông (Cardboard)', 'Thuỷ Tinh (Glass)', 'Kim Loại (Metal)', 'Giấy (Paper)', 'Nhựa (Plastic)'] 
num_classes = len(CLASSES)

# XÂY DỰNG TRỰC TIẾP CẤU TRÚC ĐÃ TRAIN
model = nn.Sequential(
    nn.Conv2d(3, 32, kernel_size=3, padding=1),
    nn.BatchNorm2d(32),
    nn.ReLU(inplace=True),
    nn.MaxPool2d(2),
    
    nn.Conv2d(32, 64, kernel_size=3, padding=1),
    nn.BatchNorm2d(64),
    nn.ReLU(inplace=True),
    nn.MaxPool2d(2),
    
    nn.Conv2d(64, 128, kernel_size=3, padding=1),
    nn.BatchNorm2d(128),
    nn.ReLU(inplace=True),
    nn.MaxPool2d(2),
    
    nn.Conv2d(128, 256, kernel_size=3, padding=1),
    nn.BatchNorm2d(256),
    nn.ReLU(inplace=True),
    nn.MaxPool2d(2),
    
    nn.Conv2d(256, 512, kernel_size=3, padding=1),
    nn.BatchNorm2d(512),
    nn.ReLU(inplace=True),
    nn.MaxPool2d(2),

    nn.Flatten(),
    nn.Linear(512 * 4 * 4, 512), 
    nn.ReLU(inplace=True),
    nn.Dropout(0.5),
    nn.Linear(512, num_classes)
)

# Xây dựng đường dẫn tuyệt đối đến file web model để chống lỗi nếu chạy lệnh ở thư mục cha.
current_dir = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(current_dir, '../GARBAGE_CLASSIFICATION_cnn_model.pth')

try:
    print(f"Đang tiến hành load model tại: {MODEL_PATH}...")
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.to(device)
    model.eval()
    print("Load Model thành công!")
except Exception as e:
    print(f"Load model lỗi (có thể do sai khác số lượng classes hoặc cấu trúc). Đang chạy ở chế độ giả định (DUMMY MODE).\nChi tiết: {e}")

# Preprocessing cho ảnh tải lên theo chuẩn trong bài làm
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Không có file ảnh nào được tải lên.'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Vui lòng chọn ảnh.'}), 400

    try:
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        
        # Tiền xử lý
        tensor_img = transform(image).unsqueeze(0).to(device)

        # Dự đoán
        if model is not None:
            with torch.no_grad():
                outputs = model(tensor_img)
                _, predicted = torch.max(outputs, 1)
                predicted_idx = predicted.item()
                
            # Đảm bảo index không vượt quá độ dài CLASSES
            if predicted_idx < len(CLASSES):
                predicted_class = CLASSES[predicted_idx]
            else:
                predicted_class = f"Class Index: {predicted_idx}"
        else:
            predicted_class = "Chưa có Model - Mẫu Giả Định: Chai Nhựa"

        return jsonify({
            'prediction': predicted_class
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5008)
