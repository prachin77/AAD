from flask import Flask, render_template, request
import itertools
import numpy as np

app = Flask(__name__)

def travellingSalesmanProblem(distanceMatrix):
    numCities = len(distanceMatrix)
    minCost = float('inf')
    bestPath = []
    cities = list(range(numCities))

    for perm in itertools.permutations(cities[1:]):
        currentPath = [0] + list(perm) + [0]  # Start and end at the first city
        currentCost = 0

        # Calculate the cost of the current path
        for i in range(len(currentPath) - 1):
            currentCost += distanceMatrix[currentPath[i]][currentPath[i + 1]]

        # Update minimum cost and best path if current path is cheaper
        if currentCost < minCost:
            minCost = currentCost
            bestPath = currentPath
            
    return bestPath, minCost

@app.route('/', methods=['GET', 'POST'])
def index():
    bestPath = None
    minCost = None
    path_details = None
    path_taken = None
    
    if request.method == 'POST':
        # Get the user input as a string
        matrix_input = request.form['matrix_input']
        
        # Convert the input string into a 2D numpy array
        try:
            # Convert the input string into a list of lists, replace '-1' with 'inf'
            distanceMatrix = np.array([
                [float('inf') if val == '-1' else float(val) for val in row.split()]
                for row in matrix_input.splitlines()
            ])
            
            # Ensure the matrix is square
            if distanceMatrix.shape[0] != distanceMatrix.shape[1]:
                return render_template('index.html', error="The distance matrix must be square.")
            
            bestPath, minCost = travellingSalesmanProblem(distanceMatrix)
            
            # Prepare the results for display
            path_details = []
            for i in range(len(bestPath) - 1):
                path_details.append(f"{bestPath[i] + 1}–{bestPath[i + 1] + 1} = {distanceMatrix[bestPath[i]][bestPath[i + 1]]}")
                
            path_taken = '-'.join(str(city + 1) for city in bestPath)
        
        except Exception as e:
            return render_template('index.html', error=f"Invalid input: {e}")

    return render_template('index.html', bestPath=bestPath, minCost=minCost, path_details=path_details, path_taken=path_taken)

if __name__ == '__main__':
    app.run(debug=True)