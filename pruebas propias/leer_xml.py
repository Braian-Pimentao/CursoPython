from xml.dom import minidom
contador_mapa = 1
doc = minidom.parse("D:\\Adaptaciones\\Canada\\doc_canada.xml")


coordenadas = doc.getElementsByTagName("coordinates")

for coordenada in coordenadas:
    string_coor = coordenada.firstChild.data
    string_coor = string_coor.strip()
    mapa_copiar = open(f'D:\\Adaptaciones\\Canada\\mapas_sin_formatear\\coordenadas_sin_formatear_{contador_mapa}.txt', 'w')
    mapa_copiar.write(string_coor[:-2])
    mapa_copiar.close()

    contador_mapa += 1

print(len(coordenadas))

