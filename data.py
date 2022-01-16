#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Diego CB
# Created Date: 16/01/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Ler/importar os dados do arquivo CSV """

import msg
import db
import os
import pandas as pd
import sqlite3

# LOAD DATA
class loadData:

	def __init__(self):
		pass

	# Carrega e importa o arquivo CSV
	def loadCSV(self, objDB, csv_filename, tablename):
		if objDB.is_connected == True:
			df = pd.read_csv(csv_filename)

			# Cria tabela e colunas
			for col in df.columns:
				if not (col == 'Unnamed: 0'):
					try:
						objDB.cur.execute("ALTER TABLE %s ADD %s TEXT" % (tablename, col.lower()))
					except Exception as e:
						print(msg.texto['erro_coluna'] % (col.lower(), e))
						pass

				#OPCIONAL: limpa a tabela antes de importar
				objDB.cur.execute("DELETE FROM %s" % (tablename))
				objDB.con.commit()

			# Importa/insere dados
			try:
			    print(msg.texto['aguarde_importando'])
			    for valor in df.values:
			    	line = '"'+'","'.join(map(str, valor))+'"'
			    	sql = 'INSERT INTO %s VALUES(%s) ' % (tablename, line)	    	
			    	objDB.cur.execute(sql)
			    	objDB.con.commit()
			except Exception as e:
				print(msg.texto['erro_row'] % (row, e))

			foo = input(msg.texto['concluido_press'])
		else:
			objDB.cls()
			print(msg.texto['erro_conectar'])