import re

def verificar_email(email):
    patron = r'\w+\@\w+\.com'
    if re.search(patron,email) is not None:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


verificar_email("vertem2o@gmail.com")
