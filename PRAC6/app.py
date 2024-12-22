from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Function to create M and S table
def create_m_s_table(dims_list):
    num_matrix = len(dims_list)
    m_matrix = np.zeros((num_matrix, num_matrix))
    s_matrix = np.zeros((num_matrix, num_matrix))
    
    for offset in range(num_matrix - 2):
        i = 1
        j = offset + i + 1
        while j < num_matrix:
            k_list = [x for x in range(i, j)]
            m_k_dict = {}
            min_m = None
            min_k = None
            for k in k_list:
                m = m_matrix[i][k] + m_matrix[k+1][j] + (dims_list[i - 1] * dims_list[k] * dims_list[j])
                m_k_dict[k] = m
                if min_m is None or min_m > m:
                    min_m = m
                    min_k = k
            m_matrix[i][j] = min_m
            s_matrix[i][j] = min_k
            i += 1
            j = offset + i + 1
            
    return m_matrix, s_matrix

# Function to find the optimal matrix multiplication bracket
optimised_cal = ""
def find_optimal_brackets(s_matrix, i, j):
    global optimised_cal
    if i == j:
        optimised_cal += f"A{i} "
    else:
        optimised_cal += "("
        find_optimal_brackets(s_matrix, i, int(s_matrix[i][j]))
        find_optimal_brackets(s_matrix, int(s_matrix[i][j]) + 1, j)
        optimised_cal += ")"

# Route to display the form and process the input
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dims_input = request.form["dims"]
        dims_list = list(map(int, dims_input.split(",")))
        
        # Generate M and S tables
        m_matrix, s_matrix = create_m_s_table(dims_list)
        
        # Find the optimal brackets
        global optimised_cal
        optimised_cal = ""
        find_optimal_brackets(s_matrix, 1, len(dims_list) - 1)
        
        # Prepare the result for display
        return render_template("result.html", dims=dims_list, m_matrix=m_matrix, s_matrix=s_matrix, optimised_cal=optimised_cal)
    
    return render_template("index.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
