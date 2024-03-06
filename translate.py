import pandas as pd
from PIL import Image
import numpy as np

# Đọc file CSV chứa đường dẫn ảnh và label
df = pd.read_csv('datasets/AffectNet/labels.csv')

# Tạo một từ điển để ánh xạ nhãn cảm xúc thành số
emotion_mapping = {'anger': 0, 'disgust': 1, 'fear': 2, 'happy': 3, 'sad': 4, 'surprise': 5, 'neutral': 6}

# Hàm chuyển đổi ảnh thành chuỗi pixel
def convert_image_to_pixels(image_path):
    image_path = 'datasets/AffectNet/' + image_path
    with Image.open(image_path) as img:
        img_resized = img.convert('L').resize((48, 48), Image.Resampling.LANCZOS)
        return np.array(img_resized).flatten()

# Sử dụng hàm để chuyển đổi ảnh
df['pixels'] = df['pth'].apply(lambda x: convert_image_to_pixels(x).tolist())

# Ánh xạ nhãn cảm xúc thành số
df['emotion'] = df['label'].map(emotion_mapping)

df['Usage'] = 'Training'

# Chọn các cột cần thiết để lưu vào CSV mới
df_output = df[['emotion', 'pixels', 'Usage']]

# Lưu kết quả vào file CSV mới
df_output.to_csv('AffectNet.csv', index=False)
