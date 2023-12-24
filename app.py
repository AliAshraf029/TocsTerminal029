from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_cv():
    return render_template('myfile.html')

if __name__ == '__main__':
    app.run(debug=True)