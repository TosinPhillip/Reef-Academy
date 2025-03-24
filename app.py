from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
   

@app.route('/select_test')
def select_test():
    return render_template('select_exam.html',title='Select Test')

@app.route('/sign_in_page')
def sign_in_page():
    return render_template("sign_in_page.html")


if __name__ == '__main__':
    app.run(debug=True)