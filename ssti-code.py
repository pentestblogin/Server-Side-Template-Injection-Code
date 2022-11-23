import re 
from flask import Flask, render_template_string


app = Flask(__name__)

@app.route("/insecure/<user>")

def insecure(user):

        template = f"<h1>Welcome to the  of {user}!</h1>"
        return render_template_string(template)

@app.route("/secure/<users>")
def secure(users):
         users = re.sub("^[A-Za-z0-9]", "", users)
         template = "<h1>Welcome to the profileof {{ users }}!</h1>"
         return render_template_string(template, users=users)
app.run()
