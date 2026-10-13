import numpy as np
# membuat array
nilai = np.array([85, 55, 40, 90])

# mengakses data pada array
print(nilai [3])

import numpy as np
# Membuat array
data = np.array([1, 2, 3])

# Menampilkan data
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])
a=np.array([[1,2,3,4],[5,66,7,8]])

#T2.1 menampilkan array 2 dimensi setiap dimensi memiliki 3 elemen.
a=np.array([[1,2,3],[4,5,6]])
print(a.shape)

#T2.3 Numpy main datatype is ndarray
a = np.array([1,2,3])
print(a)
import numpy as np

#T2.4
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)
b = a.reshape(3,2)
print(b)

# T3.1
a = np.arange(24)
print(a)

#T2.4
a = a.reshape(2, 4, 3)
print(a)

#T3.3
import numpy as np
res = np.arange(2, 6, 5)
print(list(res))

#T3.4
import numpy as np
# Menyimpan array ke dalam variabel dan mencetaknya
hasil = np.arange(3, 10, 3)
print(hasil)

#T4.2
urutan = np.linspace(0, 10, 4, dtype=int)
print("Urutan:", urutan)
#pembagian antar elemen matriks
A = np.array([[2, 4], [10, 12]])
B = np.array([[1, 2], [5, 6]])
C = A / B
print(C)

#CODING T10.19
arr = np.array([1, 2, 3])
arr = np.append(arr, 4)
print(arr)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
hasil = np.append(arr1, arr2)
hasil

#Perbedaannya adalah pada koding di bawah tidak ada perintah print(hasil)
#Untuk menampilkan outputnya ke layar.

#T10.20
# Membuat array NumPy
arr1 = np.array([1, 2, 3, 4, 5])
# Menyisipkan beberapa nilai sekaligus pada indeks ke-2
arr1_baru = np.insert(arr1, 2, [9, 9, 9])
print("Arr1 asli:", arr1)
print("Arr1 baru:", arr1_baru)

# T2.5 membuat array sebanyak 24, dari 0-23
import numpy as np
a = np.arange(24)
b = a.reshape(2, 3, 4)
print(b)

# CODING T13.7B
import numpy as np

# Data berkelompok
interval = np.array([20, 30, 40, 50, 60, 70]) # Batas interval
frekuensi = np.array([5, 12, 18, 10, 7]) # Frekuensi

# Menghitung midpoint dari setiap interval
midpoints = (interval[:-1] + interval[1:]) / 2

# Menghitung mean dari data berkelompok
mean = np.sum(midpoints * frekuensi) / np.sum(frekuensi)

# Menghitung variansi dari data berkelompok
varians = np.sum(((midpoints - mean) ** 2) * frekuensi) / np.sum(frekuensi)

# Menghitung standar deviasi dari data berkelompok
std_deviation = np.sqrt(varians)

print("Mean:", mean)
print("Varians:", varians)
print("Standard Deviation:", std_deviation)
