import flask
import peecaptcha as captcha


app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "PUTYOURSECRETKEYHERE" #change this in production, dont be an idiot

@app.route("/")
def index():
    return flask.render_template("index.html")

#important: initialize the captcha route
@app.route("/captcha.png")
def captcha_image():
    image_buffer, text = captcha.create_captcha()
    flask.session["captcha_answer"] = text
    return flask.send_file(image_buffer, mimetype="image/png")

#route name can be anything this is an example, make sure you update it in your form action to reflect the route name
@app.route("/api/v1/login", methods=["POST"])
def api_login():
    user_captcha = flask.request.form.get("captcha_input", "").strip().upper()
    actual_captcha = flask.session.pop("captcha_answer", "")

    if not user_captcha or user_captcha != actual_captcha:
        return flask.render_template(
            "index.html", error="Invalid CAPTCHA. Please try again."
        )
    else:
        return flask.render_template("index.html", success="CAPTCHA validated successfully!")

app.run(host="0.0.0.0", port=5000, debug=True)