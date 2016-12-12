from flask import Flask,render_template,redirect,request


app = Flask(__name__)
app.secret_key = "ABC"

@app.route('/')
def homepage():
    """Register page."""
    # return "Welcome to Kindness"
    return render_template("homepage.html")


@app.route('/homepage',methods=['GET'])
def get_form():
    return render_template("homepage.html")

@app.route('/process_card',methods=['POST'])
def process():
    # sender_name = request.form.get("sender_name")
    # sender_phone = request.form.get("sender_phone")
    # recipient_name = request.form.get("recipient_name")
    # recipient_phone = request.form.get("recipient_phone")
    # message = request.form.get("message")
    # background = request.form.get("value")
    # background = "whitecard"
    return render_template('/cardpreview',background=background)

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)



# from flask import Flask
# from twilio import twiml

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"



# @app.route('/sms',methods=['GET','POST'])
# def sms():
#     """Responds to incoming text messages"""
#     response = twiml.Response()
#     response.message("Hello from Lori!")
#     return str(response)


# if __name__ == "__main__":
#     # app.run()
#     app.run(host="0.0.0.0", port=5000)