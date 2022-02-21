habla_ingles = True
sabe_python = False
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")