from openpyxl import load_workbook
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
#использование библиотек для кластеризации данных,а так же работы с файлам иксель(в том числе парсинг значений)

wb = load_workbook('data.xlsx')#открываем файл,ниже открывает нужный лист книги
sheet = wb.get_sheet_by_name('data')
data = []#объявляем массив,для заполнения его данными из нашего файла
for cellObj in sheet['B5':'C240']:
    data.append([cell.value for cell in cellObj])


lock = []

for cl_n in range(1, 10):
    kmeans = KMeans(n_clusters=cl_n)
    y_kmeans = kmeans.fit_predict(data)
#использование функций библиотеки для kmeans
    data = np.array(data)

    lock.append(sum(np.min(cdist(data, kmeans.cluster_centers_, 'euclidean'), axis=1)) / data.shape[0])

plt.subplot(111)
plt.plot(range(1, 10), lock, 'o-')
plt.show()
#демонастрация графика в окне
cl_n = int(input("Введіть бажану кулькість кластерів"))
kmeans = KMeans(n_clusters=cl_n)
y_kmeans = kmeans.fit_predict(data)
#ввод количества кластеров
colors = np.array(['orange', 'magenta', 'green', 'blue', 'purple', 'brown', 'black', 'gray'])
plt.scatter([i[0] for i in data], [i[1] for i in data], c=colors[y_kmeans])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='r', s=100)
plt.show()
#демонастрация графика согласно введённым данным