from flask import Flask
import logging

app = Flask(__name__)

# Configure logging to log to stdout for CloudWatch
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Homepage accessed")
    return "Cloud Monitoring NOC Project - Home Page"

@app.route("/error")
def error():
    app.logger.error("🔥 Test Error: Something went wrong in Flask App!")
    return "Error generated and logged!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
