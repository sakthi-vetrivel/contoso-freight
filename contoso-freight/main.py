from flask import Flask, render_template, url_for 
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def homepage():
    return render_template("new_index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090, debug=True)
