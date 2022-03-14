from app import app


@app.route('/api')
def api_home():
    return 'Hello from ecommerce-api!'