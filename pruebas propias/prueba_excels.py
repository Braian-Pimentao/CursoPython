import openpyxl
excel_document = openpyxl.open('C:\\Users\\bpimentao\\OneDrive - Indra\Documentos\\Simulador Avinor S018E018\\SN_S018E018_PV2_16_V1_iSIM_V1.xlsx')

sheet = excel_document['Map Polygons']
print(sheet['A2'].fill.bgColor)
print(sheet['A2'].column)
