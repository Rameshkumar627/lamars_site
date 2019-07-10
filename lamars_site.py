from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/product")
def product():
    return render_template('product.html')


@app.route("/screenshot")
def screen_shot():
    return render_template('screen_shot.html')


# @app.route("/pricing")
# def pricing():
#     return render_template('pricing.html')


@app.route("/client")
def client():
    return render_template('client.html')


@app.route("/contact")
def contact_us():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
