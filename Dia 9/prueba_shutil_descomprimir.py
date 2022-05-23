import shutil

carpeta_origen = 'C:\\Users\\bpimentao\\OneDrive - Indra\\Documentos\\D5.1.LC5-00-01'

carpeta_destino = 'archivo_comprimido_shutil'

shutil.make_archive(carpeta_destino, 'zip', carpeta_origen)

shutil.unpack_archive('archivo_comprimido_shutil.zip', ' descopmpresion_shutil')