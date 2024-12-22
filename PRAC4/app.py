# class Employee:
#     all_Emp_Details = []

#     def __init__(self, emp_id, emp_name, emp_sal):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_sal = emp_sal

        
#         single_Emp_Detail = [emp_id, emp_name, emp_sal]
#         Employee.all_Emp_Details.append(single_Emp_Detail)

#     @staticmethod
#     def LinearSearch(all_Emp_List):
#         search_id = input("Enter ID that you want to search: ")
#         found = False
#         for emp_detail in all_Emp_List:
#             if emp_detail[0] == search_id: 
#                 print(f"Employee ID: {emp_detail[0]}")
#                 print(f"Employee Name: {emp_detail[1]}")
#                 print(f"Employee Salary: {emp_detail[2]}")
#                 found = True
#                 break
#         if not found:
#             print("Employee not found")

#     @staticmethod
#     def BinarySearch(all_Emp_List , left , right):
#         search_id = input("Enter ID that you want to search: ")
#         found = False
#         while left <= right:
#             mid = (left + right) // 2
#             mid_employee = all_Emp_List[mid]
            
#             if mid_employee[0] == search_id:
#                 print(f"Employee ID: {mid_employee[0]}")
#                 print(f"Employee Name: {mid_employee[1]}")
#                 print(f"Employee Salary: {mid_employee[2]}")
#                 return
#             elif mid_employee[0] < search_id:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         print("Employee not found")


# def main():
#     n = int(input("No. of employees = "))
#     for _ in range(n):  
#         emp_id = input("Enter employee ID: ")
#         emp_name = input("Enter employee name: ") 
#         emp_sal = input("Enter employee salary: ") 
#         emp = Employee(emp_id, emp_name, emp_sal)

#     print("1. FOR LINEAR SEARCH")
#     print("2. FOR BINARY SEARCH")
#     choice = int(input("Enter choice = "))
#     if choice == 1:
#         print("Employee Details:")
#         print(Employee.all_Emp_Details)
#         Employee.LinearSearch(Employee.all_Emp_Details)  
#     elif choice == 2:
#         print("Employee Details:")
#         print(Employee.all_Emp_Details)
#         Employee.BinarySearch(Employee.all_Emp_Details , 0 , n-1)  

#     else:
#         print("Wrong choice")

# if __name__ == "__main__":
#     main()


from flask import Flask, request, render_template, jsonify, send_from_directory
import time
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Employee data storage
all_Emp_Details = []

# Create the Employee class
class Employee:
    def __init__(self, emp_id, emp_name, emp_sal):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_sal = emp_sal

        # Add to global list
        all_Emp_Details.append([emp_id, emp_name, emp_sal])

    @staticmethod
    def LinearSearch(search_id):
        start_time = time.time()
        found = None
        for emp_detail in all_Emp_Details:
            if emp_detail[0] == search_id:
                found = emp_detail
                break
        end_time = time.time()
        search_time = end_time - start_time
        return found, search_time

    @staticmethod
    def BinarySearch(search_id):
        start_time = time.time()
        all_Emp_Details.sort(key=lambda x: x[0])  # Ensure the list is sorted for binary search
        left, right = 0, len(all_Emp_Details) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_employee = all_Emp_Details[mid]
            if mid_employee[0] == search_id:
                end_time = time.time()
                search_time = end_time - start_time
                return mid_employee, search_time
            elif mid_employee[0] < search_id:
                left = mid + 1
            else:
                right = mid - 1
        end_time = time.time()
        search_time = end_time - start_time
        return None, search_time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    emp_id = request.form['emp_id']
    emp_name = request.form['emp_name']
    emp_sal = request.form['emp_sal']
    Employee(emp_id, emp_name, emp_sal)
    return render_template('index.html', message="Employee added successfully!")

@app.route('/search', methods=['POST'])
def search():
    search_id = request.form['search_id']
    search_type = request.form['search_type']
    
    if search_type == 'linear':
        result, search_time = Employee.LinearSearch(search_id)
    elif search_type == 'binary':
        result, search_time = Employee.BinarySearch(search_id)
    else:
        result, search_time = None, 0
    
    if result:
        result_str = f"Employee ID: {result[0]}, Name: {result[1]}, Salary: {result[2]}"
    else:
        result_str = "Employee not found"
    
    return jsonify(result=result_str, time=search_time)

@app.route('/generate_plot')
def generate_plot():
    try:
        # Example data collection
        search_times_linear = [0.005, 0.004, 0.003, 0.002]
        search_times_binary = [0.002, 0.001, 0.001, 0.0005]
        input_sizes = [10, 50, 100, 500]

        plt.figure()  # Ensure a new figure is created
        plt.plot(input_sizes, search_times_linear, label='Linear Search', marker='o')
        plt.plot(input_sizes, search_times_binary, label='Binary Search', marker='o')
        plt.xlabel('Input Size')
        plt.ylabel('Search Time (seconds)')
        plt.title('Search Time Comparison')
        plt.legend()
        plt.grid(True)

        # Ensure the static directory exists
        if not os.path.exists('static'):
            os.makedirs('static')

        # Save the plot as a PNG file
        plt.savefig('static/plot.png')

        # Clear the plot to avoid overlap in future plots
        plt.clf()
        
        return render_template('plot.html')

    except Exception as e:
        return str(e)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
