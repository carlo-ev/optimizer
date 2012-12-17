from db import Table
from easygui import *

def read_tables():
	tablas = open(fileopenbox( msg="Seleccione Archivo de Tablas",default="/home/carlo/Documents/BD2/proyectoBD",filetypes=["*.txt"]), "r")	
	#tablas = open("/home/carlo/Documents/BD2/proyectoBD/tablasprueba.txt", "r")
	tbl_lines = ""
	for line in tablas :
		tbl_lines += line.lower()
	tablas.close()
	return tbl_lines.split("\n\n")

def crt_tables(tb_stack):
	tables = []
	for x in tb_stack:
		x.splitlines()
		tables.append( Table(x.splitlines()) )
	return tables

def read_add_stats(tables):
	estds = open(fileopenbox(msg="Seleccione Archivo de Estadisticas",default="/home/carlo/Documents/BD2/proyectoBD",filetypes=["*.txt"]),"r")
	#estds = open("/home/carlo/Documents/BD2/proyectoBD/estadisticasprueba.txt", "r")
	est_lines=""
	for line in estds :
		est_lines += line.lower()
	estds.close()
	raw_stats = est_lines.split("\n\n")
	for x in raw_stats :
		x = x.splitlines()
		for y in tables :
			if y.name == x[0] :
				y.insert_prop(x)
	return tables

def read_indices(tables):
	indices = open(fileopenbox(msg="Seleccione Archivo de Indices",default="/home/carlo/Documents/BD2/proyectoBD",filetypes=["*.txt"]),"r")
	#indices = open("/home/carlo/Documents/BD2/proyectoBD/indicesprueba.txt", "r")
	ind_lines=""
	for lines in indices :
		ind_lines += lines.lower()
	indices.close()
	#print(ind_lines)
	raw_ind = ind_lines.split("\n\n")
	for x in raw_ind :
		x = x.splitlines()
		for y in tables :
			if y.name == x[0] :
				y.insert_ind(x)
	return tables
