from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html"
    # , the_date = today
    )
    
@app.route("/about")
def about_me():
    return render_template("about_me.html")
    
# def todays_date():
#     today = date.today()
#     str_date = today.strftime("%B %d %Y")
#     return "Today's date is " + str_date
    
# @app.route("/education")
# def education():
#     return render_template("education.html")
    
# @app.route("/work")
# def work():
#     return render_template("work.html")
    
    # update Public IPv4 DNS address from EC2 instance for SSH server connection settings