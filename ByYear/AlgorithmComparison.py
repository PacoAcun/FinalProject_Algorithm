import pandas as pd
import time
import matplotlib.pyplot as plt
import random
import InsertionSort as ins
import BubbleSort as bub
import QuickSort as qck
import MergeSort as mrg

insertion_times = []
bubble_times = []
quick_times = []
merge_times = []

df = pd.read_csv("Netflix DB.csv")

print("By year :")
print()

years = df["Year"].fillna(0).astype(int).tolist()

reverse_years = sorted(years, reverse=True)

random_years = random.sample(years, len(years))

sorted_years = sorted(years)

# Normal
start_time = time.time()
ins.insertion_sort(years.copy())  
end_time = time.time()

insertion_sort_time_normal = end_time - start_time
insertion_times.append(time.time() - start_time)

# Revertido
start_time = time.time()
ins.insertion_sort(reverse_years.copy())  
end_time = time.time()

insertion_sort_time_reverse = end_time - start_time
insertion_times.append(time.time() - start_time)

# Aleatorio
start_time = time.time()
ins.insertion_sort(random_years.copy())  
end_time = time.time()

insertion_sort_time_random = end_time - start_time
insertion_times.append(time.time() - start_time)

# Ordenado
start_time = time.time()
ins.insertion_sort(sorted_years.copy())  
end_time = time.time()

insertion_sort_time_sorted = end_time - start_time
insertion_times.append(time.time() - start_time)

print(f"--------Tiempo de ejecución de Insertion Sort normal: {insertion_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort revertido: {insertion_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort aleatorio: {insertion_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort ordenado: {insertion_sort_time_sorted} segundos-----------")
print()

df = pd.read_csv("Netflix DB.csv")

years = df["Year"].fillna(0).astype(int).tolist()

reverse_years = sorted(years, reverse=True)

random_years = random.sample(years, len(years))

sorted_years = sorted(years)

# Normal
start_time = time.time()
bub.bubble_sort(years.copy())  
end_time = time.time()

bubble_sort_time_normal = end_time - start_time
bubble_times.append(time.time() - start_time)

# Revertido
start_time = time.time()
bub.bubble_sort(reverse_years.copy())  
end_time = time.time()

bubble_sort_time_reverse = end_time - start_time
bubble_times.append(time.time() - start_time)

# Aleatorio
start_time = time.time()
bub.bubble_sort(random_years.copy())  
end_time = time.time()

bubble_sort_time_random = end_time - start_time
bubble_times.append(time.time() - start_time)

# Ordenado
start_time = time.time()
bub.bubble_sort(sorted_years.copy())  
end_time = time.time()

bubble_sort_time_sorted = end_time - start_time
bubble_times.append(time.time() - start_time)

print(f"--------Tiempo de ejecución de Bubble Sort normal: {bubble_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort revertido: {bubble_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort aleatorio: {bubble_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort ordenado: {bubble_sort_time_sorted} segundos-----------")
print()

df = pd.read_csv("Netflix DB.csv")

years = df["Year"].fillna(0).astype(int).tolist()

reverse_years = sorted(years, reverse=True)

random_years = random.sample(years, len(years))

sorted_years = sorted(years)

# Normal
start_time = time.time()
qck.quick_sort(years.copy(), 0, len(years) - 1)  
end_time = time.time()

quick_sort_time_normal = end_time - start_time
quick_times.append(time.time() - start_time)

# Revertido
start_time = time.time()
qck.quick_sort(reverse_years.copy(), 0, len(reverse_years) - 1)  
end_time = time.time()

quick_sort_time_reverse = end_time - start_time
quick_times.append(time.time() - start_time)

# Aleatorio
start_time = time.time()
qck.quick_sort(random_years.copy(), 0, len(random_years) - 1)  
end_time = time.time()

quick_sort_time_random = end_time - start_time
quick_times.append(time.time() - start_time)

# Ordenado
start_time = time.time()
qck.quick_sort(sorted_years.copy(), 0, len(sorted_years) - 1)  
end_time = time.time()

quick_sort_time_sorted = end_time - start_time
quick_times.append(time.time() - start_time)

print(f"--------Tiempo de ejecución de Quick Sort normal: {quick_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort revertido: {quick_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort aleatorio: {quick_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort ordenado: {quick_sort_time_sorted} segundos-----------")
print()

df = pd.read_csv("Netflix DB.csv")

years = df["Year"].fillna(0).astype(int).tolist()

reverse_years = sorted(years, reverse=True)

random_years = random.sample(years, len(years))

sorted_years = sorted(years)

# Normal
start_time = time.time()
mrg.merge_sort(years.copy()) 
end_time = time.time()

merge_sort_time_normal = end_time - start_time
merge_times.append(time.time() - start_time)

# Revertido
start_time = time.time()
mrg.merge_sort(reverse_years.copy()) 
end_time = time.time()

merge_sort_time_reverse = end_time - start_time
merge_times.append(time.time() - start_time)

# Aleatorio
start_time = time.time()
mrg.merge_sort(random_years.copy()) 
end_time = time.time()

merge_sort_time_random = end_time - start_time
merge_times.append(time.time() - start_time)

# Ordenado
start_time = time.time()
mrg.merge_sort(sorted_years.copy()) 
end_time = time.time()

merge_sort_time_sorted = end_time - start_time
merge_times.append(time.time() - start_time)

# DataFrame ordenada por Insertion Sort
year_df_ins = pd.DataFrame(years, columns=["Year"])
year_df_ins.to_csv("ByYear/Insertion.csv", index=False)

# DataFrame ordenada por Bubble Sort
year_df_bub = pd.DataFrame(years, columns=["Year"])
year_df_bub.to_csv("ByYear/Bubble.csv", index=False)

# DataFrame ordenada por Quick Sort
year_df_qck = pd.DataFrame(years, columns=["Year"])
year_df_qck.to_csv("ByYear/QuickSort.csv", index=False)

# DataFrame ordenada por Merge Sort
year_df_mrg = pd.DataFrame(years, columns=["Year"])
year_df_mrg.to_csv("ByYear/MergeSort.csv", index=False)

print(f"--------Tiempo de ejecución de Merge Sort normal: {merge_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort revertido: {merge_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort aleatorio: {merge_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort ordenado: {merge_sort_time_sorted} segundos-----------")

# Graficar los resultados
labels = ['Normal', 'Revertido', 'Aleatorio', 'Ordenado']
width = 0.2  # Ancho de las barras

fig, ax = plt.subplots(figsize=(10, 6))

bar1 = ax.bar(
    [i - 1.5 * width for i in range(1, 5)],
    insertion_times,
    width,
    label='Insertion Sort',
    align='center',
)

bar2 = ax.bar(
    [i - 0.5 * width for i in range(1, 5)],
    bubble_times,
    width,
    label='Bubble Sort',
    align='center',
)

bar3 = ax.bar(
    [i + 0.5 * width for i in range(1, 5)],
    quick_times,
    width,
    label='Quick Sort',
    align='center',
)

bar4 = ax.bar(
    [i + 1.5 * width for i in range(1, 5)],
    merge_times,
    width,
    label='Merge Sort',
    align='center',
)

ax.set_xlabel('Tipo de Datos')
ax.set_ylabel('Tiempo de Ejecución (segundos)')
ax.set_title('Comparación de Tiempos de Ejecución de Algoritmos de Ordenación')
ax.set_xticks([i for i in range(1, 5)])
ax.set_xticklabels(labels)
ax.legend()

plt.show()
