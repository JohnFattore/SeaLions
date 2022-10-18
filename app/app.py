from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about/', methods=["GET","POST"])
def about():
    if request.method == "POST":
        if not request.form.get("name"):
            return render_template("apology.html")

        if not request.form.get("time"):
            return render_template("apology.html")
            
        name = request.form.get("name")
        time = request.form.get("time")        
        return render_template("aboutpost.html", name=name, time=time)
    else:
        return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)