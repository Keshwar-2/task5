from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    op = data.get('operator')
    x = data.get('x')
    y = data.get('y')
    if op == 'add':
        result = x + y
    elif op == 'subtract':
        result = x - y
    elif op == 'multiply':
        result = x * y
    elif op == 'divide':
        result = x / y if y else 'Error: Division by zero'
    else:
        result = 'Invalid operator'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
