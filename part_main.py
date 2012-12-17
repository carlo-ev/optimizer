import math
from db import *
from easygui import * 
import files as fl
import tkinter as win


msgbox(msg="Proyecto Base de Datos 2 \n Optimizador SQL", title="Sql Optimizer by CMEV 2012", ok_button="Continue")

db = fl.read_indices( fl.read_add_stats( fl.crt_tables( fl.read_tables() ) ) )
show=""
#print(db)
for x in db :
	show +=  "%s \n\n" % (x.to_p())

#textbox(msg="Selected Data to Work with:",title="Sql Optimizer by CMEV 2012 Data Base", text=(show + "\n\n\n\n****Changes Will not be saved!!!****"))
root = win.Tk().title("Sql Optimizer by CMEV 2012 Data Base 2 DB Summary")
scroll = win.Scrollbar(root)
scroll.pack(side=win.RIGHT, fill=win.Y)
txt = win.Text(root, yscrollcommand=scroll.set)
txt.insert(win.END, "Selected Data to Work with:\n\n" + show)
txt.config(state=win.DISABLED, bg="BLACK", fg="WHITE", font=12)
txt.pack()
scroll.config(command=txt.yview)

sql = enterbox(msg="Insert sql Statment to be optimized: ", title="Sql Optimizer by CMEV 2012 SQL Input")

if sql is None: exit()

if (Approval.validate(sql, db)) :
	tables_used = Approval.tables_in_use
	select = Approval.last_used_select
	where  = Approval.last_used_where
	#print(tables_used)
	#print(select)
	#print(where)
	display = "Sql statement provided: \n{0}\n\nSelect: {1}\nFrom: {2}\nWhere: {3}\n\nValid Sql!\n\nEach Where Statement and its Cost:\n\n".format(sql,select, str(tables_used),where)
	total_cost = 0

	for statement in where :
		display += "{0} {1} {2}".format(str(statement[0]),str(statement[1]),str(statement[2]))
		current = ceil( Calculations.cost(tables_used, statement) )
		display += " => {0} Blocks\n".format(current)
		total_cost += current
		#print("The cost in blocks of this statement is {0}".format( current ) )
	#print("Total Cost for First run without modifications: {0}".format(total_cost))
	display += "\nTotal cost of Search without optimization (First run): {0}\n\n\nStatement Arrangement after Optimization for improved performance:\n\n".format(total_cost)

	opt = sorted(where, key = lambda stat : ceil( Calculations.cost(tables_used,stat) ) )
	for stat in opt :
		#print(stat)
		display += "{0} {1} {2}  =>  {3} Blocks\n".format( str(stat[0]), str(stat[1]), str(stat[2]), str(ceil(Calculations.cost(tables_used, stat))) )
	#print("Costo total luego de optimizacion: " + str(total_cost))

	textbox(msg="Query Processing Finished, Showing Results: ",title="Sql Optimizer by CMEV 2012 Data Base", text=display)

else:
	print("Error in Sql Statment, plz check input.")

