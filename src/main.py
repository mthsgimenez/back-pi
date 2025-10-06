from flask import Flask
from controllers.recommendations import recommendations_bp
from controllers.weather import weather_bp

app = Flask(__name__)

app.register_blueprint(recommendations_bp, url_prefix = '/recommendations')
app.register_blueprint(weather_bp, url_prefix = '/weather')
    
if __name__ == '__main__':
    app.run(debug=True)