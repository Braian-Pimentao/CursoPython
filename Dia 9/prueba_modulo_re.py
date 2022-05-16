import re

texto = "llama al 666666666 ya mismo"

patron = re.compile('(\d{6})(\d{3})')

resultado = re.search(patron,texto)
print(resultado.group(2))