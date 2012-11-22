from db import Unit
def contains(string, keyword) :
	words = string.split("\n")
	for x in words :
		if x.lower == keyword.lower :
			return True
	return False



file = open("/home/carlo/Documents/BD2/proyectoBD/bdarchivopr.txt", "r+")

statements = ""
for line in file :
	statements += line
blocks = statements.split('\n\n')
print(blocks)
sql=""
for c in blocks :
	if contains(c, "select") :
		sql = c
print(sql)
print(blocks[1])
table = Unit(blocks[1])
print(table)