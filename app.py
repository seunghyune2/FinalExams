from werkzeug.utils import redirect
import ddb
from flask import Flask,render_template ,request, redirect, session, sessions
from hello import money_pung,idpw_check
app = Flask(__name__)

#로그인 처리(세션에 필요)
app.secret_key = b'aaa!111/' ## 임의로 이름 설정

@app.route('/')
def hello():
    return render_template("main.html")

@app.route('/signup', methods = ['GET' , 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        email = request.form['email']
        pswd = request.form['pswd']
        username = request.form['username']
        # 위 데이터들을 어딘가에 저장해서 로그인할때
        # 사용해야하는데...
        ddb.insert_member(email, pswd, username)
        return redirect('/') ## 메인으로 보내기
        #return "{}</br>{}</br>{}</br> 회원정보".format(email,pswd,username)

@app.route('/signin', methods = ['GET' , 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html")
    else:
        email = request.form['email']
        pswd = request.form['pswd']
        #이메일 패스워드 체크
        ## msg = idpw_check(email,pswd)
        ret = ddb.select_member(email, pswd)
        if ret != None :
            session['email'] = email
            return redirect('/')
        else :
            return redirect('/signin')
        # return "{}</br>{}</br>{}</br>".format(email,pswd,msg)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/') # 메인으로

@app.route('/money')
def money():
    # 로그인된 사용자들만 돈뻥 페이지가 보이게
    # 세션 체크
    if 'email' in session:
        return render_template("money.html")
    else:
        return redirect('/signin')

@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        return "GET 으로 들어온 페이지"
    else:
        # form 으로 전달된 데이터를 받아서 뻥튀기 해줘야 함
        money = request.form['money']
        #money 의 값이 문자열 이기 때문에 숫자로 변경
        print("전달된 값은? ",int(money)*3)
        im = money_pung(int(money)) #뻥튀기 함수 사용
        return render_template("show.html",money=im)
        #return "당신의 능력을 보여줘~ 얍<br><b>{}</b>원 드립니다".format(im)
        #return "당신의 능력을 보여줘~ 얍<br><b>{}</b>원 드립니다".format(money_pung(int(money)))

@app.route('/showmoney')
def showmoney():
    return render_template("smoney.html")

@app.route('/hello/')
def hellohtml():
    return render_template("hello.html")

#if __name__ == '__main__':
#   app.run()