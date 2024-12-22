# def loop():
#     total_pairs = 0
#     months = 12
#     for i in range(1,months+1):
#         formula = 2**i
#         total_pairs = formula
#         print(f"for month {i} pairs produced = {formula}")

#     print("total no. of pairs : ",total_pairs)


# def recursion(month, current=1):
#     if current > month:
#         return 0
    
#     formula = 2 ** current
#     print(f"for month {current} pairs produced = {formula}")
    
#     total_pairs = recursion(month, current + 1)
    
    
#     if current == month:  
#         total_pairs += formula
#         print("total no. of pairs : ", total_pairs)
    
#     return total_pairs

# def main():
#     print("1. FOR LOOP")
#     print("2. FOR RECURSION")

#     choice = int(input("enter above choice = "))

#     if choice == 1:
#         loop()
#     elif choice == 2:
#         recursion(12,1)
#     else:
#         print("wrong choice")

# if __name__ == "__main__":
#     main()





# FLASK CODE 
from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def calculate_pairs_loop():
    total_pairs = 0
    months = 12
    results = []
    for i in range(1, months + 1):
        formula = 2 ** i
        total_pairs = formula
        results.append((i, formula))
    return results, total_pairs

def calculate_pairs_recursion(month, current=1):
    if current > month:
        return [], 0

    formula = 2 ** current
    results = [(current, formula)]
    
    next_results, total_pairs = calculate_pairs_recursion(month, current + 1)
    
    results.extend(next_results)
    
    if current == month:
        total_pairs += formula

    return results, total_pairs

def generate_plot(results):
    months, pairs = zip(*results)  # Unzip the results into two lists
    plt.figure(figsize=(10, 6))
    plt.plot(months, pairs, marker='o', linestyle='-', color='b')
    plt.xlabel('Month')
    plt.ylabel('Pairs Produced')
    plt.title('Pairs Produced Over Months')
    plt.grid(True)
    
    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Rewind the BytesIO object
    plt.close()
    
    # Encode the image to base64
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    return img_base64

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    choice = request.form.get('choice')
    if choice == '1':
        results, total_pairs = calculate_pairs_loop()
    elif choice == '2':
        results, total_pairs = calculate_pairs_recursion(12, 1)
    else:
        return "Invalid choice", 400

    # Generate the plot and encode it to base64
    img_base64 = generate_plot(results)
    return render_template('result.html', method='FOR LOOP' if choice == '1' else 'FOR RECURSION', results=results, total_pairs=total_pairs, img_data=img_base64)

@app.route('/plot')
def plot():
    img_base64 = generate_plot(calculate_pairs_loop()[0])
    return send_file(io.BytesIO(base64.b64decode(img_base64)), mimetype='image/png', as_attachment=False, attachment_filename='plot.png')

if __name__ == '__main__':
    app.run(debug=True)
