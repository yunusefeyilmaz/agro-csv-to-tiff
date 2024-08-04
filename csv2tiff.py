import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

file = "test.csv"

# CSV dosyasını oku, veri türlerini belirle
df = pd.read_csv(file, header=None, names=['idx', 'classId'], dtype={'idx': 'str', 'classId': 'str'})

# Veriyi sayılara dönüştür
df['idx'] = pd.to_numeric(df['idx'], errors='coerce')
df['classId'] = pd.to_numeric(df['classId'], errors='coerce')

# NaN değerleri kaldır
df.dropna(inplace=True)

# Verileri numpy dizilerine dönüştür
idx = df['idx'].values.astype(int)
classId = df['classId'].values.astype(int)

# Maksimum idx değeri ile grid boyutlarını hesapla
max_idx = idx.max()
width = 12671  # Genişlik
height = 9981  # Yükseklik

# Boş bir grid oluştur
raster_data = np.zeros((height, width), dtype=np.uint8)

# Verileri grid'e dönüştür
for i in range(len(idx)):
    x = idx[i] % width
    y = idx[i] // width
    if y < height and x < width:
        raster_data[y, x] = classId[i]

# Görüntü oluştur ve kaydet
fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)  # DPI ve figure size ayarları ile boyutu koru
cmap = plt.get_cmap('viridis')
norm = mcolors.Normalize(vmin=raster_data.min(), vmax=raster_data.max())
img = ax.imshow(raster_data, cmap=cmap, norm=norm)
plt.axis('off')  # Eksenleri kapat
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Alt ve üst boşlukları kaldır
plt.savefig('test_colored_viridis.tiff', format='tiff', dpi=100)  # DPI parametresi ile kaydet
plt.close()
