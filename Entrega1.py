import csv
with open("calles_de_medellin_con_acoso.csv") as archivo:
    datos = csv.reader(archivo, delimiter=";")
    columns = datos.__next__()
    rows = []
    for row in datos:
        row_as_dict = {}
        for idx, item in enumerate(row):
            row_as_dict[columns[idx]] = item
        rows.append(row_as_dict)

    for row in rows:
        if row['origin'] == '(-75.5728593, 6.2115169)':
            print(row)
