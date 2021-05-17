from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/money')
def money():
    return '돈을 입력하시오'

@app.route('/showmoney')
def showmoney():
    return render_template("smoney.html")
@app.route('/hello/')
def hellohtml():
    return render_template("hello.html")

if __name__ == '__main__':
    app.run()