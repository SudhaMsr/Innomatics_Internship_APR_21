from flask import Flask, session, redirect, url_for, escape, request,render_template,flash

app = Flask(__name__)
app.secret_key = 'hello world'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
           "click here to log in</b></a>"


notes=[]
@app.route('/',methods=['POST'])
def note_making():
    n = request.form.get("note")
    notes.append(n)
    return render_template('home.html', notes=notes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    notes.clear()
    if request.method == 'POST':
        session['username'] = request.form['username']

        return render_template('home.html')

    return "<form action = '' method = 'post'> " + \
           "<p><input type = text name = username></p> " + \
           "<p><input type = submit value = Login></p> " + \
           "</form>"



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)