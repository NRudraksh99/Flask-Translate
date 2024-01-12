from flask import Flask,Blueprint,render_template, request
from translate import ChangeLang

v=Blueprint('v',__name__)
app=Flask(__name__,static_url_path="/static",static_folder="static")

@app.route("/")
@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route("/translate.html", methods=['GET','POST'])
def translate():
    if request.method=="POST":
        og=request.form['og_text']
        i_lang=request.form['language']
        t_lang=request.form['target']
        return render_template("result.html",data=ChangeLang(og,i_lang,t_lang))
    else:
        return render_template("translate.html")

@app.route("/result.html")
def result():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=False)