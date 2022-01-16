#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Diego CB
# Created Date: 16/01/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" API REST """

import msg
import sqlite3
import db
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Exibe as lojas
@app.route('/api/lojas', methods=['GET'])
def api_get_lojas():
	lojas = objDB.getLoja(0)
	return jsonify(lojas)

#Exibe loja por ID
@app.route('/api/lojas/<loja_id>', methods=['GET'])
def api_get_loja(loja_id):
	loja = objDB.getLoja(loja_id)
	return jsonify(loja)

#Incluir loja
@app.route('/api/lojas/add',  methods = ['POST'])
def api_add_loja():
    nova_loja = request.get_json()
    return jsonify(objDB.addLoja(nova_loja))

#Atualizar loja
@app.route('/api/lojas/update',  methods = ['PUT'])
def api_update_loja():
    loja = request.get_json()
    return jsonify(objDB.updateLoja(loja))

@app.route('/api/lojas/delete/<loja_id>',  methods = ['DELETE'])
def api_delete_loja(loja_id):
    return jsonify(objDB.deleteLoja(loja_id))

def api_run(oDB, dbname, tablename):
	global objDB
	objDB = oDB
	objDB.createDatabase(dbname)
	app.run()

if __name__ == "__main__":
    app.run()
