
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("report.html")

@app.route("/report", methods=["POST"])
def report():
    waste_type = request.form.get("waste_type")
    location = request.form.get("location")
    description = request.form.get("description")

    return f"""
    <h1>Complaint Submitted Successfully!</h1>
    <p>Waste Type: {waste_type}</p>
    <p>Location: {location}</p>
    <p>Description: {description}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
