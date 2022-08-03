import csv

with open('Datos.csv') as file:
    reader=csv.reader(file)
    for row in reader: 
        print("Apellido: {0}, Nombre: {1}, Género: {2}, Edad: {3}, Universidad: {4}, Carrera: {5} ".format(row[0], row[1], row[2], row[3], row[4], row[5]))
