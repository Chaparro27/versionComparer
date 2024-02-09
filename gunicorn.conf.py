bind = "0.0.0.0:8000"
workers = 3
timeout = 60
accesslog = "-"
errorlog = "-"

def app(environ, start_response):
    from app import app
    return app(environ, start_response)