from flask import Flask
from routes import bp as sales_bp

app = Flask(__name__)
app.register_blueprint(sales_bp)

if __name__ == '__main__':
    app.run(debug=True)
