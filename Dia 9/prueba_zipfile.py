import zipfile

# zip_comprimir = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# zip_comprimir.write('texto_A.txt')
# zip_comprimir.write('texto_B.txt')

# print(zip_comprimir.open('texto_A.txt'))

# zip_comprimir.close()

descomprimir_zip = zipfile.ZipFile('archivo_comprimido.zip', 'r')

descomprimir_zip.extractall()

descomprimir_zip.close()
