#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Diego CB
# Created Date: 16/01/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" MAIN APP """

import msg
import api
import data
import db

def main():
	objData = data.loadData()
	objDB = db.loadDB()
	objDB.cls()	
	print(msg.texto['main'])
	dbname=input(msg.texto['database'])
	objDB.createDatabase(dbname)
	tablename=input(msg.texto['tabela'])
	objDB.createTable(tablename)
	print(msg.texto['database_con'])
	objDB.cls()

	while True:
		options=msg.menu.keys()
		options=sorted(options)
		print(msg.texto['main'])

		for entry in options: 
			print(entry, msg.menu[entry])
		selection=input(msg.texto['menu'])

		## OPT IMPORTAR CSV
		if selection =='1':		
			csv_filename=input(msg.texto['csv'])			
			objData.loadCSV(objDB, csv_filename, tablename)		
			objDB.cls()

		## OPT EXIBIR IDS IMPORTADOS
		elif selection == '2':
			objDB.getTableData(tablename)

		## RODAR API
		elif selection == '3':
			api.api_run(objDB, dbname, tablename)

		elif selection == '4':
			print('\n')
			break
		else:
			print(msg.texto['erro_opt'])

if __name__ == "__main__":
	main() #run main