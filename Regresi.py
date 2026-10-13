import pandas as pd

df = pd.read_csv('dataset_fiskal_97_hipoFull.csv')
print(df.shape)

X = df[['DBH_PAJAK', 'DAU_Grant', 'DAK_Nonfisik']]
y = df['PAD']

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model = LinearRegression()
model.fit(X, y)

b0 = model.intercept_
b1, b2, b3 = model.coef_

y_hat = model.predict(X)
r2 = r2_score(y, y_hat)

n, k = len(df), 3
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - k - 1)

print(f"Y = {b0:.4f} + {b1:.4f} X1 + {b2:.4f} X2 + {b3:.4f} X3")
print(f"R2 = {r2:.4f}")
print(f"Adjusted R2 = {adj_r2:.4f}")

baru = pd.DataFrame([[77.91, 96.98, 72.02]], columns=X.columns)
print("Prediksi Y:", model.predict(baru)[0].round(2))

import plotly.express as px

fig = px.scatter_3d(df, x='DBH_PAJAK', y='DAU_Grant', z='PAD',
                    color='DAK_Nonfisik',
                    title='Regresi Linier 3D: X1, X2, Y (warna = X3)')
fig.show()

