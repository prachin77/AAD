import time
import matplotlib.pyplot as plt

def loop(n):
    total = 0
    client_income = 10000
    for i in range(1,n+1):
        total += client_income
    return total

def equation(n):
    client_income = 10000
    total_income = n * client_income
    return total_income

def recursion(n):
    client_income = 10000
    # if n == 1:
    #     return client_income
    # else:
    #     return client_income + recursion(n-1)
    total_income = 0
    while n>0:
        total_income += client_income
        n = n-1
    return total_income
def measure_time(func, n):
    # start_time = time.time()
    start_time = time.perf_counter()
    func(n)
    # end_time = time.time()
    end_time = time.perf_counter()
    return end_time - start_time

def plot_graph(n_values):
    loop_times = []
    equation_times = []
    recursion_times = []

    for n in n_values:
        print(f"Measuring for N = {n}")

        # Measure time for each method
        loop_time = measure_time(loop, n)
        equation_time = measure_time(equation, n)
        recursion_time = measure_time(recursion, n)

        loop_times.append(loop_time)
        equation_times.append(equation_time)
        recursion_times.append(recursion_time)

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(n_values, loop_times, label='Loop Method', marker='o')
    plt.plot(n_values, equation_times, label='Equation Method', marker='o')
    plt.plot(n_values, recursion_times, label='Recursion Method', marker='o')
    plt.xlabel('Number of Clients (N)')
    plt.ylabel('Time (seconds)')
    plt.title('Comparative Analysis of Different Methods')
    plt.legend()
    plt.grid(True)
    plt.show()


print("1. LOOP")
print("2. EQUATION")
print("3. RECURSION")

def main():
    choice = int(input("enter number : "))
    if choice == 1:
        n = int(input("enter number of clients : "))    
        loop_result = loop(n)

        print("TOTAL MONTHLY INCOME OF ALL CLIENTS CALCULATED THROUGH LOOP")
        print(loop_result)

        time_taken = measure_time(loop,n)
        print(f"{time_taken:.6f} seconds")

        n_values = [10, 100, 1000, 5000, 10000]
        plot_graph(n_values)
    elif choice == 2:
        n = int(input("enter number of clients : "))    
        equation_result = equation(n)

        print("TOTAL MONTHLY INCOME OF ALL CLIENTS CALCULATED THROUGH EQUATION")
        print(equation_result)

        time_taken = measure_time(equation,n)
        print(f"{time_taken:.6f} seconds")

        n_values = [10, 100, 1000, 5000, 10000]
        plot_graph(n_values)
    elif choice == 3:
        n = int(input("enter number of clients : "))    
        recursion_result = recursion(n)

        print("TOTAL MONTHLY INCOME OF ALL CLIENTS CALCULATED THROUGH RECURSION")
        print(recursion_result)

        time_taken = measure_time(recursion,n)
        print(f"{time_taken:.6f} seconds")

        n_values = [10, 100, 1000, 5000, 10000]
        plot_graph(n_values)
    else:
        print("wrong number entered")



if __name__ == "__main__":
    main()





# FLASK CODE 
# import os
# from flask import Flask, request, jsonify, render_template
# import time
# import matplotlib.pyplot as plt
# import io
# import base64

# app = Flask(__name__)

# client_income = 10000

# def loop(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += client_income
#     return total

# def equation(n):
#     total_income = n * client_income
#     return total_income

# def recursion(n):
#     total_income = 0
#     while n > 0:
#         total_income += client_income
#         n = n - 1
#     return total_income

# def measure_time(func, n):
#     start_time = time.perf_counter()
#     func(n)
#     end_time = time.perf_counter()
#     return end_time - start_time

# def generate_plot(n_values, loop_times, equation_times, recursion_times):
#     plt.figure(figsize=(12, 6))
#     plt.plot(n_values, loop_times, label='Loop Method', marker='o')
#     plt.plot(n_values, equation_times, label='Equation Method', marker='o')
#     plt.plot(n_values, recursion_times, label='Recursion Method', marker='o')
#     plt.xlabel('Number of Clients (N)')
#     plt.ylabel('Time (seconds)')
#     plt.title('Comparative Analysis of Different Methods')
#     plt.legend()
#     plt.grid(True)
    
#     # Save plot to a BytesIO object
#     img = io.BytesIO()
#     plt.savefig(img, format='png')
#     plt.close()
#     img.seek(0)
    
#     # Encode image to base64
#     img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
#     return img_base64

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     result = None
#     time_taken = None
#     if request.method == 'POST':
#         method = request.form.get('method')
#         n = int(request.form.get('n'))

#         if method == 'loop':
#             result = loop(n)
#             time_taken = measure_time(loop, n)
#         elif method == 'equation':
#             result = equation(n)
#             time_taken = measure_time(equation, n)
#         elif method == 'recursion':
#             result = recursion(n)
#             time_taken = measure_time(recursion, n)
#         else:
#             return jsonify({'error': 'Invalid method'}), 400

#     return render_template('index.html', result=result, time_taken=time_taken)

# @app.route('/plot', methods=['GET'])
# def plot():
#     n_values = [10, 100, 1000, 5000, 10000]
    
#     loop_times = [measure_time(loop, n) for n in n_values]
#     equation_times = [measure_time(equation, n) for n in n_values]
#     recursion_times = [measure_time(recursion, n) for n in n_values]
    
#     img_base64 = generate_plot(n_values, loop_times, equation_times, recursion_times)
    
#     return jsonify({'message': "Plot generated", 'plot': img_base64})

# if __name__ == "__main__":
#     app.run(debug=True)
