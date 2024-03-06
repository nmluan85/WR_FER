import pandas as pd
import re

# Đọc file Excel
df = pd.read_csv('AffectNet.csv')

# Hàm để loại bỏ các ký tự không mong muốn và chuyển đổi chuỗi
def clean_pixels(value):
    # Đảm bảo giá trị đầu vào là một chuỗi
    value = str(value)
    # Loại bỏ các ký tự '[' và ']' và ','
    cleaned_value = re.sub(r'[\[\],]', '', value)
    return cleaned_value

# Áp dụng hàm clean_pixels cho cột 'pixels'
df['pixels'] = df['pixels'].apply(clean_pixels)

# Ghi đè lên file gốc
df.to_csv('AffectNet.csv', index=False)