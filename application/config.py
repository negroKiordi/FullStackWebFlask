import os

class config(object):
    SECRET_KY = os.environ.get('SECRET-KY') or "secret_string"