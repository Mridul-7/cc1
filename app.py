from flask import Flask, render_template, request

app = Flask(__name)

# Replace this with a secure way to store your usernames and passwords
users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return 'Login Successfully'
    else:
        return 'Login failed due to incorrect username and password'

if __name__ == '__main__':
    app.run()
