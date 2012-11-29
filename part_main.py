from easygui import * 
import files as fl


msgbox(msg="Proyecto Base de Datos 2 \n Optimizador SQL", title="Sql Optimizaer by CMEV 2012", ok_button="Continue")

tbl = fl.read_add_stats( fl.crt_tables( fl.read_tables() ) )
show=""
for x in tbl :
	show += str(x)

textbox(msg="Selected Data to Work with:",title="Sql Optimizaer by CMEV 2012 Base Data", text=(show+"\n\n\n\n****Changes Will not be saved!!!****"))

sql = enterbox(msg="Insert sql Statment to be optimized: ", title="Sql Optimizaer by CMEV 2012 SQL Input")
sql = sql.lower()
sql = sql.split(" ")
print(sql)
