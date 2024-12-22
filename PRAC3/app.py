# import time
# import random
# import matplotlib.pyplot as plt

# def BubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break

# def SelectionSort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# def InsertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# def MeasureTime(sort_function, arr):
#     start_time = time.time()
#     sort_function(arr)
#     end_time = time.time()
#     return end_time - start_time

# def plot_performance(sizes, bubble_times, selection_times, insertion_times):
#     plt.figure(figsize=(12, 8))
#     plt.plot(sizes, bubble_times, label="Bubble Sort", marker='o')
#     plt.plot(sizes, selection_times, label="Selection Sort", marker='o')
#     plt.plot(sizes, insertion_times, label="Insertion Sort", marker='o')
#     plt.xlabel('List Size (n)')
#     plt.ylabel('Time (seconds)')
#     plt.title('Sorting Algorithm Performance')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# def main():
#     sizes = [100, 200, 300, 400, 500]
#     bubble_times = []
#     selection_times = []
#     insertion_times = []

#     for size in sizes:
#         arr = [random.randint(0, 10000) for _ in range(size)]
        
#         # Measure Bubble Sort time
#         arr_copy = arr.copy()
#         bubble_times.append(MeasureTime(BubbleSort, arr_copy))

#         # Measure Selection Sort time
#         arr_copy = arr.copy()
#         selection_times.append(MeasureTime(SelectionSort, arr_copy))

#         # Measure Insertion Sort time
#         arr_copy = arr.copy()
#         insertion_times.append(MeasureTime(InsertionSort, arr_copy))

#     plot_performance(sizes, bubble_times, selection_times, insertion_times)

# if __name__ == "__main__":
#     main()




# FLASK CODE 
from flask import Flask, render_template, request
import time
import random
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)


def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def MeasureTime(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

def generate_plot(sizes, bubble_times, selection_times, insertion_times):
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, bubble_times, label="Bubble Sort", marker='o')
    plt.plot(sizes, selection_times, label="Selection Sort", marker='o')
    plt.plot(sizes, insertion_times, label="Insertion Sort", marker='o')
    plt.xlabel('List Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)

    # Save plot to a BytesIO object and encode it as base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    if request.method == 'POST':
        sizes_str = request.form.get('sizes', '100,200,300,400,500')
        sizes = [int(size) for size in sizes_str.split(',')]

        bubble_times = []
        selection_times = []
        insertion_times = []

        for size in sizes:
            arr = [random.randint(0, 10000) for _ in range(size)]

            # Measure Bubble Sort time
            arr_copy = arr.copy()
            bubble_times.append(MeasureTime(BubbleSort, arr_copy))

            # Measure Selection Sort time
            arr_copy = arr.copy()
            selection_times.append(MeasureTime(SelectionSort, arr_copy))

            # Measure Insertion Sort time
            arr_copy = arr.copy()
            insertion_times.append(MeasureTime(InsertionSort, arr_copy))

        plot_url = generate_plot(sizes, bubble_times, selection_times, insertion_times)

    return render_template('index.html', plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)
