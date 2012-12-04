import threading
from db import Optimizer as mach
from easygui import * 
import files as fl

def slct_val(tables, slct_sts) :
	slct_sts.pop(0)
	for  x in slct_sts :
		for y in tables :
			if ( x in y ) :
				return True
	return False


def frm_val(tables, frm) :
	for y in frm :
		for x in tables :
			if x.name == y :
				return True
	return False



# msgbox(msg="Proyecto Base de Datos 2 \n Optimizador SQL", title="Sql Optimizer by CMEV 2012", ok_button="Continue")

db = fl.read_indices( fl.read_add_stats( fl.crt_tables( fl.read_tables() ) ) )
show=""
for x in db :
	show += str(x) + "\n"

textbox(msg="Selected Data to Work with:",title="Sql Optimizer by CMEV 2012 Data Base", text=(show + "\n\n\n\n****Changes Will not be saved!!!****"))


for x in db :
	x.print_indices()


sql = enterbox(msg="Insert sql Statment to be optimized: ", title="Sql Optimizer by CMEV 2012 SQL Input")





''' def statements(lst_sts) :
	lst = lst_sts.split("and")
	lst =  lst.split(" ")
	for x in range(0, len(lst), 3) :
		for
		'''  