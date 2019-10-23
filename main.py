from flask import Flask, render_template, url_for 
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def homepage():
    return render_template("index copy.html")

if __name__ == '__main__':
    app.run()
