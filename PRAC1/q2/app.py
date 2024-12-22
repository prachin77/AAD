from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve the input data from the request
    data = request.json

    try:
        l = data['numbers']
        if len(l) != 5:
            return jsonify({"error": "Please provide exactly 5 numbers."}), 400
    except KeyError:
        return jsonify({"error": "No numbers provided in the request."}), 400
    except TypeError:
        return jsonify({"error": "Invalid input format. Ensure you're sending a JSON array."}), 400

    result_list = []
    pair_list = []

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            result = abs(l[i] + l[j])
            result_list.append(result)
            pair_list.append([l[i], l[j]])

    min_result = min(result_list)

    response = {
        "min_result": min_result,
        "result_list": result_list,
        "pair_list": pair_list
    }

    # Filter pairs with the minimum result
    min_pairs = [pair_list[i] for i in range(len(result_list)) if result_list[i] == min_result]

    return jsonify({
        "min_result": min_result,
        "result_list": result_list,
        "pairs_with_min_result": min_pairs
    })

if __name__ == '__main__':
    app.run(debug=True)
    