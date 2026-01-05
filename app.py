from flask import Flask
from weather import weather_bp

app = Flask(__name__)

# подключаем blueprint
app.register_blueprint(weather_bp)

@app.route("/")
def home():
    return "Главная страница Flask"

if __name__ == "__main__":
    app.run(debug=True)
