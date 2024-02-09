from flask import Flask, jsonify,render_template, request
from routes.comparar_routes import comparar_bp

app = Flask(__name__)

# Registrar las rutas del paquete comparar
app.register_blueprint(comparar_bp, url_prefix='/comparar')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)