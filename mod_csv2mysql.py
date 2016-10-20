import json
import mysql.connector
import os

#==============	Load config.json ==============================
config = None
def load_config():
	with open('config.json','r') as f:
		return json.load(f)

def get_config():
	global config
	if config is None:
		config = load_config()
	return config
#==============================================================

#================= Misc functions =============================
def get_csv_files(dir_path):
	return [dir_path+os.sep+name for name in os.listdir(dir_path) if ('.csv' in name and os.path.isfile(os.path.join(dir_path,name)))]
def get_csv_file_first_line(csv_file):
	first_line = ''
	with open(csv_file,'r') as f:
		for l in f:
			first_line = l
			first_line = first_line.replace('\n','')
			break
	return first_line

#==============================================================

#==============	Database operations ===========================
cxn = None
def create_connection():
	return mysql.connector.connect(option_files='mysql-connector.cnf')

def get_connection():
	global cxn
	if cxn is None:
		cxn = create_connection()
	return cxn
#=========== Main function ====================================

def load_csvs(csvs_folder):
	if csvs_folder:
		csv_files = get_csv_files(csvs_folder)
		for csv_file in csv_files:
			entity_name = csv_file.split(os.sep).pop().split('.')[0]
			cxn = get_connection()
			cursor = cxn.cursor()
			query = 'LOAD DATA LOCAL INFILE \''+csv_file+ \
					'\' INTO TABLE '+entity_name+' FIELDS TERMINATED BY \',\' ENCLOSED BY \'"\' LINES TERMINATED BY \'\\n\' IGNORE 1 LINES '+ \
					' ('+get_csv_file_first_line(csv_file)+') '
			cursor.execute(query)

#==============================================================
