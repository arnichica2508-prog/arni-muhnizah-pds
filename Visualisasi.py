#matplotlib inline

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as np

import matplotlib.pyplot as plt
import numpy as np  # Pastikan baris ini sudah ditambahkan

# Menggunakan style bawaan matplotlib
plt.style.use('fivethirtyeight')

# Buat grafik seperti biasa
x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.plot(x, y)
plt.title("Contoh Grafik Dengan Style")
plt.show()

# numpy.random
import numpy as np
import matplotlib.pyplot as plt # Pastikan matplotlib juga di-import
from numpy.random import rand

# Solusi: Buat data x dan y secara terpisah dengan jumlah elemen yang sama (misal: 1000 data)
x = rand(1000)
y = rand(1000)

plt.scatter(x, y)
plt.show()

# Data
bulan = ['januari', 'februari', 'maret', 'april', 'mei']
penjualan = [150, 200, 180, 250, 125]

# 6x4 inci adalah ukuran kecil yang tidak full screen
plt.figure(figsize=(8, 5))

plt.bar(bulan, penjualan, color='purple')
plt.title('penjualan per bulan')
plt.xlabel('bulan')
plt.ylabel('jumlah')

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Data
Bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Juni', 'Juli']
penjualan = [150, 200, 180, 250, 125, 220, 130]

plt.figure(figsize=(6, 4)) #inci

# Membuat grafik dengan palette warna yang lebih modern
sns.barplot(x=Bulan, y=penjualan, palette='colorblind')

plt.title('Penjualan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Penjualan')

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Data
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Juni', 'Juli']
penjualan = [150, 200, 180, 250, 125, 220, 130]

plt.figure(figsize=(8, 4)) # Diperlebar sedikit agar 7 bulan muat dengan rapi

# 1. Buat Grafik Batang
sns.barplot(x=bulan, y=penjualan, palette='muted')

# 2. Tambahkan Garis Tren (Menghubungkan puncak batang)
# range(len(bulan)) menghasilkan [0, 1, 2, 3, 4, 5, 6] sebagai posisi sumbu X
plt.plot(
    range(len(bulan)), # Posisi X (tengah setiap batang)
    penjualan,         # Posisi Y (nilai penjualan)
    color='red',       # Warna garis
    marker='o',        # Tambahkan titik bulat di setiap persimpangan
    linestyle='-',     # Gaya garis (solid)
    linewidth=2,       # Ketebalan garis
    label='Garis Tren' # Nama untuk legenda
)

# 3. Kustomisasi Tampilan
plt.title("Penjualan per Bulan dengan Garis Tren", fontsize=12, fontweight='bold')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')
plt.legend() # Menampilkan kotak legenda

plt.tight_layout()
plt.show()

import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Bulan' : ('jan', 'Feb', 'Mar', 'Apr', 'Mei'),
    'Penjualan' : (150, 200, 180, 250, 300)

})

fig = px.bar(df, x='Bulan', y='Penjualan', title='Penjualan per Bulan')
fig.update_layout(width=700, height=400)
fig.show()
