import threading
from db import Approval
from easygui import * 
import files as fl


# msgbox(msg="Proyecto Base de Datos 2 \n Optimizador SQL", title="Sql Optimizer by CMEV 2012", ok_button="Continue")

db = fl.read_indices( fl.read_add_stats( fl.crt_tables( fl.read_tables() ) ) )
#show=""
#for x in db :
#	show += str(x) + "\n\n"

#textbox(msg="Selected Data to Work with:",title="Sql Optimizer by CMEV 2012 Data Base", text=(show + "\n\n\n\n****Changes Will not be saved!!!****"))


#for x in db :
#	x.print_indices()


sql = enterbox(msg="Insert sql Statment to be optimized: ", title="Sql Optimizer by CMEV 2012 SQL Input")


Approval.validate(sql, db)


''' def statements(lst_sts) :
	lst = lst_sts.split("and")
	lst =  lst.split(" ")
	for x in range(0, len(lst), 3) :
		for
		'''  