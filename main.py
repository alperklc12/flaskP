from flask import (Flask, redirect, render_template, 
escape, url_for, request)
import csv


app = Flask(__name__)


def write_to_csv(data):
    with open("database.csv", "a", newline="") as fl:
        username = data['username']
        subject =  data['subject']

        csv_writer = csv.writer(fl, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([username, subject])

def write_to_txt(data):
    with open("database.txt", "a") as fl:
        current_data = f"{data['username']},{data['subject']}"
        fl.write(data + "\n")

@app.route("/")
def home_fn():
    return render_template("index.html")


@app.route("/<page_name>")
def pages_fn(page_name):
    return render_template("{}.html".format(page_name))


@app.route("/submit_form", methods=["POST", "GET"])
def submit_fn():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thanks")
        except:
            return "error!!!"
    else:
        return "somethin went to wrong!"


if __name__ == "__main__":
    app.run(debug=True)

