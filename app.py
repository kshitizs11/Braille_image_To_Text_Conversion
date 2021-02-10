from flask import Flask,render_template,redirect,request
import Flask_Braille

app = Flask(__name__)

@app.route("/")
def speech():
	return render_template("index.html")


@app.route("/",methods=["POST"])
def image():
	if request.method=="POST":
		f = request.files["userfile"]
		path = "./static/{}".format(f.filename)
		f.save(path)
		text = Flask_Braille.braille_text(path)
		result_dic = {"image":path,"text":text}
	return render_template("index.html",your_result=result_dic)

if __name__ == "__main__":
	app.run(threaded=False)
