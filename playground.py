from flask import Flask, render_template
app = Flask(__name__)

# 1
@app.route('/play')          
def hello():
    print("in the hello funciton")
    return render_template("index.html")  


# 2
@app.route('/play/<x>')          
def boxes_times(x):
    return render_template("index.html",times=int(x))

#3
@app.route('/play/<x>/<color>')          
def boxes_color(x,color):
    return render_template("index.html", num_times=int(x),num_color=color)




if __name__=="__main__":   
    app.run(debug=True)