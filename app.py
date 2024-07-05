from flask import Flask,render_template,request,redirect
from helper import preprocessing , vectorizer , predict

app = Flask(__name__)

data = dict()
reviews = []
positve = 0
negative = 0

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positve
    data['negative'] = negative

    return render_template("index.html",data = data)

@app.route("/",methods=["post"])
def get_post():
    text=request.form["text"]
    preprocessed_data = preprocessing(text)
    vectorized_data = vectorizer(preprocessed_data)
    prediction = predict(vectorized_data)

    if prediction == "Negative" :
        global negative
        negative += 1
    else:
        global positve
        positve += 1
    reviews.insert(0,text)   
    return redirect(request.url)     

if __name__ == "__main__":
    app.run()
