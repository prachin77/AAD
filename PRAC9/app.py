from flask import Flask, render_template, request
from collections import namedtuple

app = Flask(__name__)

# Define the Item class using namedtuple for simplicity
Item = namedtuple('Item', ['profit', 'weight'])

def fractional_knapsack(W, arr):
    max_profit = 0
    arr.sort(key=lambda item: item.profit / item.weight, reverse=True)

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            max_profit += item.profit
        else:
            max_profit += item.profit * (W / item.weight)
            break  # No more weight can be added

    return max_profit

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        W = int(request.form['capacity'])
        items = []
        for i in range(1, int(request.form['num_items']) + 1):
            profit = int(request.form[f'profit_{i}'])
            weight = int(request.form[f'weight_{i}'])
            items.append(Item(profit, weight))
        
        max_val = fractional_knapsack(W, items)
        return render_template('result.html', max_val=max_val)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)