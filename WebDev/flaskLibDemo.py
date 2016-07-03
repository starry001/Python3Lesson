from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    return '<h1>home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action = "/signin" method = "post">
              <p><input name = "username"/></p>
              <p><input name = "password" type= "password"/></p>
              <p><button type="submit" >sign in</buton></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'pwd':
        return '<h3> Hello admin !</h3>'
    return '<h3>Bad username or password !</h3>'


if __name__ == '__main__':
    app.run()
