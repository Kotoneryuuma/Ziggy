from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')          
def index():
    return render_template("index.html",times=int(6))

@app.route('/<x>')          
def index2(x):
    return render_template("index.html",times=int(x)) 

if __name__=="__main__":   
    app.run(debug=True)


