#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Diego CB
# Created Date: 16/01/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" MENU/MESSAGES STRINGS """

# MENU
menu = {}
menu['1']="Importar CSV"
menu['2']="Contar registros"
menu['3']="Rodar API"
menu['4']="Sair"

# MESSAGES
texto = {}
texto['main']="\nIMPORTAR CSV PARA SQLITE3\n"
texto['menu']="\nPor favor, escolha um número: "
texto['database']="\nDigite o nome do database para conectar (ex. cadastro.db): "
texto['database_con']="\nDatabase gerado/conectado!"
texto['tabela']="\nDigite o nome da tabela (ex. loja): "
texto['csv']="\nDigite o nome do arquivo CSV (ex. restaurants.csv): "
texto['erro']="\nErro : %s"
texto['erro_opt']="\nOpção inválida!: "
texto['erro_get_table']="\nErro ao exibir dados de %s : %s"
texto['erro_conectar']="\nErro ao conectar, favor conferir conexão!"
texto['concluido_press']="\nConcluído! Pressione qualquer tecla..."
texto['erro_row']="\nErro importando row %s : %s \n"
texto['erro_coluna']="\nErro ao criar coluna %s : %s !\n"
texto['aguarde_importando']="\nAguarde, importando dados..."
texto['deleted'] ="\nRegistro removido com sucesso!"
texto['delete_error'] ="\nErro ao remover registro!"
