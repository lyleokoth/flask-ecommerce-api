from ecom import app


@app.route('/api')
@app.route('/')
def api_home():
    return 'Hello from ecommerce-api! changw'
