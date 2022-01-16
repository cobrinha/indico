#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Diego CB
# Created Date: 16/01/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" DATABASE SQLITE """

import msg
import os 
import sqlite3

# LOAD DB
class loadDB:

	def __init__(self):
		self.con = False
		self.cur = False
		self.is_connected = False
		self.tablename = False
		self.dbname = False

	# Conecta/cria database
	def createDatabase(self, dbname): 
		self.con = sqlite3.connect(dbname, check_same_thread=False)
		self.cur = self.con.cursor()
		self.is_connected = True
		self.dbname = dbname

	#Cria tabela
	def createTable(self, tablename):
		self.cur.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY)" % (tablename))
		self.tablename = tablename

	# Exibe IDs da tabela
	def getTableData(self, tablename):
		if self.is_connected == True:
			try:
				self.cur.execute("SELECT id FROM %s" % (tablename))
				rows = self.cur.fetchall()
				for row in rows:
					print(str(row))
			except Exception as e:
				print(msg.texto['erro_get_table'] % (tablename, e))
				pass
		else:
			self.cls()
			print(msg.texto['erro_conectar'])

	# Exibe lojas
	def getLoja(self, LojaId=0):
		if self.is_connected == True:
			lojas = []
			try:
				if(LojaId!=0):
					sql = (
						"SELECT address, name, city FROM %s WHERE id = %s" 
						% (self.tablename, LojaId)
					)
					self.cur.execute(sql)
				else:
					sql = (
						"SELECT address, name, city FROM %s " 
						% (self.tablename)
					)					
					self.cur.execute(sql)

				rows = self.cur.fetchall()
				for row in rows:
					loja = {}
					loja["address"] = row[0]
					loja["name"] = row[1]
					loja["city"] = row[2]
					lojas.append(loja)

				return lojas
			except Exception as e:
				print(msg.texto['erro_get_table'] % (self.tablename, e))
				pass
		else:
			self.cls()
			print(msg.texto['erro_conectar'])

	# Insere loja
	def addLoja(self, Loja):
		if self.is_connected == True:
			NovaLoja = {}
			try:
				sql = (
					'INSERT INTO %s (address, name, city, categories, country, latitude, '
					' longitude, postalcode, province, websites) '
					' VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' 

					% (self.tablename, Loja['address'], Loja['name'], 
						Loja['city'], Loja['categories'], Loja['country'],
						Loja['latitude'], Loja['longitude'], Loja['postalcode'], 
						Loja['province'], Loja['websites'],
						)
				)
				self.cur.execute(sql)
				self.con.commit()
				NovaLoja = self.getLoja(self.cur.lastrowid)
			except Exception as e:
				print(msg.texto['erro'] % e)

			return NovaLoja
		else:
			self.cls()
			print(msg.texto['erro_conectar'])

	# Atualiza loja
	def updateLoja(self, Loja):
		if self.is_connected == True:
			LojaUpdate = {}
			try:
				sql = (
					'UPDATE %s SET address="%s", name="%s", city="%s", categories="%s", country="%s", '
					'latitude="%s", longitude="%s", postalcode="%s", province="%s", websites="%s"'
					'WHERE id =%s' 

					% (self.tablename, Loja['address'], Loja['name'], 
						Loja['city'], Loja['categories'], Loja['country'],
						Loja['latitude'], Loja['longitude'], Loja['postalcode'], 
						Loja['province'], Loja['websites'], Loja['id']
						)
				)
				self.cur.execute(sql)
				self.con.commit()
				LojaUpdate = self.getLoja(Loja['id'])
			except Exception as e:
				print(msg.texto['erro'] % e)

			return LojaUpdate
		else:
			self.cls()
			print(msg.texto['erro_conectar'])

	#Exclui loja
	def deleteLoja(self, LojaId):
		message = {}
		if self.is_connected == True:
			try:
				self.cur.execute("DELETE FROM %s WHERE id = %s" % (self.tablename, LojaId))
				self.con.commit()
				message["status"] = msg.texto['deleted']
			except:
				self.con().rollback()
				message["status"] = msg.texto['delete_error']
		else:
			self.cls()
			print(msg.texto['erro_conectar'])

		return message			

	# Limpa o terminal
	def cls(self):
		os.system('cls' if os.name=='nt' else 'clear')