from flask import Flask, request, render_template, redirect, url_for
import openai

app = Flask(__name__)
openai.api_key = '22ec84421ec24230a3638d1b51e3a7dc'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authentication logic
        return redirect(url_for('dashboard'))
    return render_template('auth.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Registration logic
        return redirect(url_for('dashboard'))
    return render_template('auth.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    user_input = request.json['user_input']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content']

if __name__ == '__main__':
    app.run(debug=True)
