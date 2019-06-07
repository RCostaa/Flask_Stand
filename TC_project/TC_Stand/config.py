import os

class Config:
    SECRET_KEY = os.environ.get("STAND_SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.environ.get("STAND_DATABASE_URI")

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_USE_SSL = True
    MAIL_PORT = 465

    #Estes campos usam um email e password definidos nas variaveis
    #de ambiente, de forma a esconder dados que não devem ser mostrados
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")