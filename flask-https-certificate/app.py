from flask import Flask

app = Flask(__name__)


@app.route("/")
def default():
    return "<p>Hello World!<p>"



if __name__ == "__main__":
    #app.run(ssl_context="adhoc")
    app.run(ssl_context=("cert.pem", "key.pem"))
    
    
    
#TO GET SELF-SIGNED CERT: openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365