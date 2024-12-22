from flask import Flask, render_template, request, jsonify
import heapq

app = Flask(__name__)

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Function to generate Huffman codes
def generate_huffman_codes(root, current_code="", codes={}):
    if not root:
        return

    if root.char is not None:
        codes[root.char] = current_code

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

# Function to encode text
def encode_text(text, codes):
    return "".join(codes[char] for char in text)

# Function to decode text
def decode_text(encoded_text, root):
    decoded_text = []
    current_node = root

    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right
        if current_node.char:
            decoded_text.append(current_node.char)
            current_node = root

    return "".join(decoded_text)

# Frequencies as provided in the problem
frequencies = {
    'A': 0.5,
    'B': 0.35,
    'C': 0.5,
    'D': 0.1,
    'E': 0.4,
    '-': 0.2
}

# Build the Huffman Tree and codes
huffman_tree = build_huffman_tree(frequencies)
huffman_codes = generate_huffman_codes(huffman_tree)

@app.route("/")
def index():
    return render_template("index.html", codes=huffman_codes)

@app.route("/encode", methods=["POST"])
def encode():
    text = request.json.get("text", "")
    encoded = encode_text(text, huffman_codes)
    return jsonify({"encoded": encoded})

@app.route("/decode", methods=["POST"])
def decode():
    encoded_text = request.json.get("text", "")
    decoded = decode_text(encoded_text, huffman_tree)
    return jsonify({"decoded": decoded})

if __name__ == "__main__":
    app.run(debug=True)
