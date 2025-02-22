from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def message():
    return render_template('base.html')

def message():
    return render_template('p1.html')

def message():
    return render_template('p2.html')
    

if __name__ == '__main__':
    app.run(debug=True)

 