from flask import Flask
from twilio.twiml.voice_response import Play, Hangup, VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with '9'"""
    resp = VoiceResponse()

    resp.play('', digits='9')
    resp.hangup()

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
