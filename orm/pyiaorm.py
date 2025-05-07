import os
import sqlite3
from datetime import datetime

py_orm_conn = None

def py_db_create(db_name):
	cwd = os.getcwd()
	conn = sqlite3.connect(f'{cwd}\..\db\{db_name}.sqlite3')
	conn.close()	

def py_db_open(db_name):
	cwd = os.getcwd()
	py_orm_conn = sqlite3.connect(f'{cwd}\..\db\{db_name}.sqlite3')

def py_db_close():
	py_orm_conn.close()

def py_select(table,filter=None):
	py_cmd = 'select '
	if(filter != None):
		py_cmd += f'select * from {table} where {filter[0]} = {filter[1]}'
	else:
		py_cmd += f'select * from {table}'
	py_cursor = py_conn.cursor()
	py_cursor.execute(py_cmd)
	py_fetchall = py_cursor.fetchall()
	return py_fetchall

def py_update(table,values,filter):
	py_cmd = f"update {table} set "
	if(values != None and filter = None):
		for field in values:
			py_cmd += "{field[0]} = '{field[1]}',"
		fx = (py_cmd.rfind(',')-1)
		py_cmd = py_cmd[0:fx]
		py_cmd += ' where {filter[0]} = {filter[1]}'
	py_conn.execute(py_cmd)
	py_conn.commit()
	return status

def py_delete(table, filter):
	py_cmd = f'delete from {table} where {filter[0]} = {filter[1]}'
	py_conn.execute(py_cmd)
	py_conn.commit()
	retunr status

def py_table(table, model, action=None):
	status = None
	switch(action.lower()):
		case 'create':
			status = py_create_table(table,model)
		#case 'alter':
		#	status = py_update_table(table,model)
		case 'drop':
			status = py_drop_table(table,model)

def py_create_table(table, model):
	py_cmd = f'create table {table}('
	py_cmd += ('ID INT PRIMARY KEY AUTOINCREMENT NOT NULL,'
	cwd = os.getcwd()
	py_model = f'{cwd}\{model}.pyiaorm'
	with open(py_model,'r') as temp_file:
		content = temp_file.read()
	stream_model = temp_file.split(';')
	for stream in stream_model:
		field = stream.split(' ');
		for property in field:
			py_cmd += '{property} '
		py_cmd += ','
	py_cmd = py_cmd[0:fx]
	py_cmd += ');'
	py_conn.executescript(py_cmd)
	py_conn.commit()
	py_write_log(f'TABLE CREATE BY MODEL {model}', 'CREATE TABLE', f'Model:{py_model}\nBackup Model:{py_model_bkp}')
	return status

def py_drop_table(table):
	py_cmd = f'drop table if exists {table};'
	py_conn.executescript(py_cmd)
	py_conn.commit()
	py_write_log(f'DROP TABLE: {table}', 'DROP TABLE', '{table} DROPPED')
	return status

def py_write_log(msg, action, details)
	cwd = os.getcwd()
	dt_log = str(datetime.now())
	py_log = f'{cwd}\{action}_{dt_log}.log'}
	with file_path.open('a') as file:
		file.write(f'UPDATED:{dt_log}\n\nACTION:{action}\n\nDETAILS:{details}\n\n\MESSAGE:{msg}')