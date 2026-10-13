#running pandas dan numpy
import pandas as pd
import numpy as np

#Menampilkan array 1-dimensi
ds = pd.Series([2,4,6,8,10])
print(ds)

# P2
data = pd.Series(['a','b','c']) #!sS
np1 = np.array(['x','y','z'])
data_np = pd.Series(np1)

# Menampilkan data
df.head

#P8 menampilkan tabel penjulan februari
import pandas as pd
df = pd.read_csv('penjualan.csv')
feb = df["feb"]
feb.head()

df[['feb','mar']].head(3)

#P9 Jika akan menampilkan lebih dari satu kolom (Series), gukanan double bracket [[]]
df= pd.read_csv('penjualan.csv')
df[['feb','mar']].head(3)

# 10.1
penjual = ['penjual no ' + str(i) for i in range(1, 11)]
penjual

10.2
df['urutan'] = penjual
df

## P.11 Ekstraksi Angka dari Teks
df['no'] = df['urutan'].str.extract('(\d+)').astype('int64')
df

#P.12.1 Menampilkan baris dengan indeks berlabel 0
df.loc[0]
df.iloc[0]
df[:1]

#P.12.1 Menampilkan baris dengan indeks berlabel 0
df.loc[2]
df.iloc[2]
df[:2]

#P.12.2 Menampilkan baris indeks berlabel 0 dan kolom berlabel jan
df.loc[0, 'jan']
df.iloc[0, 1]
df[['jan']][:1]

#P.12.3 Menampilkan baris berlabel 2 sampai 3 dan kolom nama, jan, mar
df.loc[2:3, ['nama', 'jan', 'mar']]

#P12.4 Menampilkan semua baris pada kolom **nama** dan **apr**
df.loc[:, ['nama', 'apr']]
df.iloc[:, [0, 4]]
df[['nama', 'apr']]


#P12.5 Menampilkan semua baris pada kolom nama sampai feb
df.loc[:, 'nama':'feb']
df.iloc[:, :3]
df[['nama', 'jan', 'feb']]

# Menampilkan semua baris dan semua kolom
df.loc[:, :]
df.loc[:,]
df.iloc[:, :]

#Jika ingin menampilkan seluruh data tabel, tanda titik dua : harus ditulis lengkap
#di kiri dan kanan koma ([:, :]). Jika hanya menulis koma tanpa pasangan titik
#dua di sebelah kanannya, program akan otomatis error.

# Cara perbaikan yang benar
df.loc[:, :]
df.iloc[:, :]

#P13.2 Memilih Memilih Teks
df[df['nama'].str.contains('Andi')]
df[df['nama'].str.contains('Jul')]

# Abaikan Huruf Besar/Kecil
df[df['nama'].str.contains('in')]
import re
df[df['nama'].str.contains('in', flags=re.IGNORECASE)]

# Memilih Data yang Berada di List/Dataframe Lain
feb_penjualan = [135, 374]
df[df['feb'].isin(feb_penjualan)]

#P13.1Memilih Angka
#1. sama dengan
df[df['jan'] == 200]
df[df.jan.eq(200)]

#2. Memilih Angka tidak sama dengan
df[df['jan'] != 200]
df[df.jan.ne(200)]
df[~(df['jan'] == 200)]

#3. Memilih Angka Lebih Dari
df[df['jan'] > 200]
df[df.jan.gt(200)]

#4. Memilih Lebih Dari atau Sama Dengan
df[df['jan'] >= 200]
df[df.jan.ge(200)]

#5. Memilih Kurang Dari atau Sama Dengan
df[df['jan'] < 200]
df[df.jan.lt(200)]

# 6. Memilih Kurang Dari atau Sama Dengan
df[df['jan'] <= 200]
df[df.jan.le(200)]

#P.12.3 menampilkan baris 0-3, kolom 0(nama), 1(jan), 3 (maret)
df.iloc[0:3, [0, 1, 3]]

#P.14 Membuat kategori tinggi dan rendah
d = {'tinggi': [320, 300], 'rendah': [95,100]}
df1 = pd.DataFrame(data=d)
df1

# Memilih Lebih dari Satu Kondisi
## Memilih Diantara Dua Rentang Nilai
df[(df['jan'] > 100) & (df['jan'] < 300)]

# Metode apply untuk menjalankan fungsi
data = [1,1,2,3,5,8,13,21]
d_int = pd.Series(data)
def kecilbesar(num):
    if num < 3:
        return "kecil"
    elif num >= 3 and num < 13:
        return "sedang"
    else:
        return "besar"

d_int.apply(kecilbesar)

import numpy as np
data = [4, 6, 9, 16, 25]
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

import numpy as np
data = [4, 6, 9, 16, 25]
var = np.var(data)
print("Varians:", var)

from statistics import multimode
data = [4, 6, 9, 16, 25]
print("Modus:", multimode(data))

data = [4, 6, 9, 16, 25]
mean = sum(data) / len(data)
print("Mean =", mean)

# --- UNTUK MAHASISWA NIM GANJIL ---
print("=== DATA PENJUALAN JANUARI (NIM GANJIL) ===")
print(df[["nama", "jan"]])

# --- UNTUK MAHASISWA NIM GENAP ---
print("=== DATA PENJUALAN FEBRUARI (NIM GENAP) ===")
print(df[["nama", "feb"]])

print("=== STATISTIK BULAN JANUARI ===")
print("Rata-rata       :", df["jan"].mean())
print("Varians         :", df["jan"].var())
print("Standar Deviasi :", df["jan"].std())

print("\n" + "="*35 + "\n")

print("=== STATISTIK BULAN FEBRUARI ===")
print("Rata-rata       :", df["feb"].mean())
print("Varians         :", df["feb"].var())
print("Standar Deviasi :", df["feb"].std())

#ARTI MASING MASING

#ARTI RATA-RATA BULAN JANUARI & FEBRUARI
# Pada bulan januari rata rata penjualannya itu 187 kemudian di bulan februari
# meningkat menjadi 220.9 berarti secara kelompok,performa penjualan mengalami
# peningkatan

#ARTI VARIANSI BULAN JANUARI & FEBRUARI
# Pada bulan januari variansinya 6584 kemudian di bulan februari 6425,mengartikan
# adanya ketimpangan performa karyawan,jarak antara sales dengan penjualan tertinggi
# (chandra&indara) dan terendah (fahri&andi) tergolong sangat jauh di kedua bulan.

#ARTI STANDAR DEVIASI BULAN JANUARI & FEBRUARI
# Di bulan januari memiliki 81.14 dan bulan februari 80.16,meskipun dibulan februari
# naik tingkat kestabilan nya masih sama dengan januari,menunjukkan tingkat konsistensi
# secara rill dalam satuan unit.

