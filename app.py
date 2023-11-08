from flask import Flask, request, render_template

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # You should replace this logic with your own user validation logic.
    if username == 'demo' and password == 'password':
        return 'Login Successfully'
    else:
        return 'Login failed due to incorrect username and password'

if __name__ == '__main__':
    app.run(debug=True)
