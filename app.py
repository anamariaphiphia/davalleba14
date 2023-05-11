
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    list = [{ 12,21,222,202}]
    return render_template('index.html', list = list)

@app.route('/<name>,<int:age>')
def user(name,age):
    return render_template('user.html',user_name=name,user_age=age)


if __name__ == '__main__':
    app.run(debug=True)