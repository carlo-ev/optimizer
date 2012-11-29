from db import Table
from easygui import *

def read_tables():
	tablas = open(fileopenbox(msg="Seleccione Archivo de Tablas",default="/home/carlo/documents/BD2/proyectobd",filetypes=["*.txt"]), "r")	
	tbl_lines = ""
	for line in tablas :
		tbl_lines += line
	tablas.close()
	return tbl_lines.split("\n\n")

def crt_tables(tb_stack):
	tables = []
	for x in tb_stack:
		x.splitlines()
		tables.append( Table(x.splitlines()) )
	return tables

def read_add_stats(tables):
	estds = open(fileopenbox(msg="Seleccione Archivo de Estadisticas",default="/home/carlo/documents/BD2/proyectobd",filetypes=["*.txt"]),"r")
	est_lines=""
	for line in estds :
		est_lines += line
	estds.close()
	raw_stats = est_lines.split("\n\n")
	for x in raw_stats :
		x = x.splitlines()
		for y in tables :
			if y.name == x[0] :
				y.insert_prop(x)
	return tables