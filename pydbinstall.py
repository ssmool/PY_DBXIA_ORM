from orm import pyiaorm

def startdb(database):
	py_db_create(database)
	dict_src = os.getcwd()
	dict_src += '\dict'
	stream_list = [tempx for tempx os.listdir(dict_src) if os.path.isfile(os.path.join(dict_src, f))]
	py_db_open(database)
	for stream in stream_list:
		table = stream.lower()
		py_create_table(table, stream)
	py_database_close()