from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success'))
    return render_template('login.html', error=error)
 
@app.route('/success')
def success():
    return "Login Successful!"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
