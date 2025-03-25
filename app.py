# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        output_text = rot13(input_text)
        return render_template('index.html', output_text=output_text, input_text=input_text)
    return render_template('index.html', output_text='', input_text='')

if __name__ == '__main__':
    app.run(debug=True)