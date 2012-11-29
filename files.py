from db import Table		

def contains(string, keyword) :
	words = string.split("\n")
	for x in words :
		if x.lower == keyword.lower :
			return True
	return False


estadisticas = open("/home/carlo/Documents/BD2/proyectoBD/estadisticasprueba.txt","r+")
tablas = open("/home/carlo/Documents/BD2/proyectoBD/tablasprueba.txt", "r+")

tbl_lines = ""
for line in tablas :
	tbl_lines += line

tablas.close()

raw_tables = tbl_lines.split("\n\n")
tables = []
for x in raw_tables:
	x.splitlines()
	tables.append( Table(x.splitlines()) )

est_lines=""
for line in estadisticas :
	est_lines += line

estadisticas.close()

raw_stats = est_lines.split("\n\n")
for x in raw_stats :
	x = x.splitlines()
	for y in tables :
		if y.name == x[0] :
			y.insert_prop(x)

print(tables[0])
