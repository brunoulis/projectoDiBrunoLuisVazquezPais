import csv
import os

direcciones=[]
pathdata=os.path.join(os.path.dirname(__file__),'datatest.csv')
with open(pathdata,encoding='utf-8')as archivo:
    #intentaremos evitar el error unicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 0: character maps to <undefined>
    datos=csv.DictReader(archivo,delimiter=';')
    for row in datos:
        #guardamos los valores de TIPUSVIA,NEXEVIA y NOMVIA en una lista
        #"Badalona", "Barcelona" ,"L'Hospitalet de Llobregat","Sabadell", "Castelldefels"
        if row['NOMMUNI'] == 'Barcelona'or row ['NOMMUNI'] == 'Badalona' or row ['NOMMUNI'] == "L'Hospitalet de Llobregat" or row ['NOMMUNI'] == 'Sabadell' or row ['NOMMUNI'] == 'Castelldefels':
            direcciones.append(row['NOMMUNI']+' '+row['TIPUSVIA']+' '+row['NEXEVIA']+' '+row['NOMVIA'])
        
            
    
    
#imprimimos la lista
for direccion in direcciones:
    print(direccion)
       
        
