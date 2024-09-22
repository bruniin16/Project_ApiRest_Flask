DEBUG = True

USERNAME = "root"
PASSWORD = "admin"

SERVER = "localhost"
DB = "project_api_flask"

SQLALCHEMY_DATABASE_URI = f"mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}"