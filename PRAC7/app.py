from flask import Flask, request, render_template, jsonify
import numpy as np

app = Flask(__name__)

def compute_knapsack_matrix(weights: list[int], values: list[int], max_weight: int):
    # Initialize weights and values with a zero at the start
    weights = [0] + weights
    values = [0] + values
    
    # Create matrix to store maximum values
    value_matrix = np.zeros((len(weights), max_weight + 1))

    # Populate the value matrix using dynamic programming
    for i in range(1, len(weights)):
        for j in range(max_weight + 1):
            if j < weights[i]:
                value_matrix[i][j] = value_matrix[i - 1][j]
            else:
                value_matrix[i][j] = max(value_matrix[i - 1][j],
                                         values[i] + value_matrix[i - 1][j - weights[i]])

    return value_matrix

def extract_optimal_items(weights: list[int], values: list[int], value_matrix: np.ndarray):
    num_items, max_weight = value_matrix.shape
    num_items -= 1
    max_weight -= 1

    selected_items = []
    weights = [0] + weights
    values = [0] + values

    # Trace back to find the items that make up the optimal solution
    while num_items > 0 and max_weight > 0:
        if value_matrix[num_items][max_weight] != value_matrix[num_items - 1][max_weight]:
            selected_items.append({
                "item": num_items,
                "weight": weights[num_items],
                "value": values[num_items]
            })
            max_weight -= weights[num_items]
        num_items -= 1

    max_value = value_matrix[-1][-1]
    return selected_items, max_value

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/knapsack', methods=['POST'])
def knapsack_api():
    data = request.form
    try:
        # Parse max weight and item weights and values from the form
        max_weight = int(data['max_weight'])
        items = {}
        
        for key in data:
            if key.startswith('weight_'):
                weight = int(data[key])
                value = int(data.get(f"value_{key.split('_')[1]}", 0))
                items[weight] = value

        weights = list(items.keys())
        values = list(items.values())
        
        # Calculate the knapsack matrix
        value_matrix = compute_knapsack_matrix(weights, values, max_weight)
        
        # Retrieve optimal items and the max value
        items_chosen, max_value = extract_optimal_items(weights, values, value_matrix)
        
        return render_template('result.html', max_value=max_value,
                               value_matrix=value_matrix.tolist(), items_chosen=items_chosen)
    except (KeyError, ValueError) as e:
        return render_template('index.html', error="Invalid input. Ensure all fields are filled correctly.")

if __name__ == '__main__':
    app.run(debug=True)
