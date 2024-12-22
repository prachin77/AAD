from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def calculate_lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    lcs_sequence = []

    # Initialize matrices
    matrix = np.zeros((m+1, n+1), dtype=int)
    arrow_matrix = np.zeros((m+1, n+1), dtype=object)

    # Fill in the matrix and arrow_matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                matrix[i, j] = matrix[i-1, j-1] + 1
                arrow_matrix[i, j] = "↖"
            elif matrix[i-1, j] >= matrix[i, j-1]:
                matrix[i, j] = matrix[i-1, j]
                arrow_matrix[i, j] = "↑"
            else:
                matrix[i, j] = matrix[i, j-1]
                arrow_matrix[i, j] = "←"

    # Backtrack to find the LCS sequence
    i, j = m, n
    while i > 0 and j > 0:
        if arrow_matrix[i, j] == "↖":
            lcs_sequence.append(s1[i-1])
            i -= 1
            j -= 1
        elif arrow_matrix[i, j] == "↑":
            i -= 1
        elif arrow_matrix[i, j] == "←":
            j -= 1

    lcs_sequence.reverse()
    return matrix, arrow_matrix, lcs_sequence

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        s1 = request.form["sequence1"].split(",")
        s2 = request.form["sequence2"].split(",")
        matrix, arrow_matrix, lcs_sequence = calculate_lcs(s1, s2)
        return render_template("index.html", s1=s1, s2=s2, matrix=matrix, arrow_matrix=arrow_matrix, lcs_sequence=lcs_sequence)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
