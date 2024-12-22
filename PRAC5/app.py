from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Define the function to calculate minimum coins and track coins used
def min_coins(amount, coins=[1, 4, 6]):
    dp = [float('inf')] * (amount + 1)
    last_coin = [-1] * (amount + 1)  # To store the last coin used for each amount
    dp[0] = 0

    for x in range(1, amount + 1):
        for coin in coins:
            if x - coin >= 0 and dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                last_coin[x] = coin  # Store the last coin used

    # If amount is not reachable with given coins
    if dp[amount] == float('inf'):
        return -1, []

    # Backtrack to find the coins used
    result_coins = []
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        result_coins.append(coin)
        current_amount -= coin

    return dp[amount], result_coins

# Define the route for getting the minimum coins and coins used for a given amount
@app.route('/min_coins/<int:amount>', methods=['GET'])
def get_min_coins(amount):
    min_coin_count, coins_used = min_coins(amount)
    if min_coin_count == -1:
        return jsonify({"error": "Amount cannot be achieved with given coins"}), 400
    return jsonify({
        "amount": amount,
        "minimum_coins": min_coin_count,
        "coins_used": coins_used
    })

# Home route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
