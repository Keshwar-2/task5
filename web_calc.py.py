from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        # Safety check - only allow basic math operations
        allowed_chars = set('0123456789+-*/.() ')
        if not all(c in allowed_chars for c in expression):
            return jsonify({'error': 'Invalid characters in expression'})
        
        result = eval(expression)
        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'error': 'Invalid expression'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
