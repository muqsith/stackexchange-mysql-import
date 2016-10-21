import xml.parsers.expat
import json
from xml.sax.saxutils import escape
import subprocess
import os
import argparse
import functools

#==============	Load config.json ==============================
config = None
def get_config():
	global config
	if config is None:
		with open('config.json','r') as f:
			config = json.load(f)
	return config
#==============================================================

#==============	Extract xml files =============================

def extract_7z_archive(archive_path):
	successful = False
	archive_name = archive_path.split(os.sep).pop()
	directory_path = archive_path.replace(os.sep+archive_name,'')
	extracted_directory = directory_path+os.sep+'d.'+archive_name
	out_bytes = subprocess.check_output(['7z','x','-o'+extracted_directory,archive_path])
	out_text = out_bytes.decode('utf-8')
	for l in out_text.split('\n'):
		if (l == 'Everything is Ok'):
			successful = True
			break
	if not successful:
		extracted_directory = ''
	return extracted_directory
#==============================================================

def get_xml_files(dir_path):
	return [dir_path+os.sep+name for name in os.listdir(dir_path) if ('.xml' in name and os.path.isfile(os.path.join(dir_path,name)))]

#==============================================================

#==============================================================

def create_temp_csv_dir(parent_dir_path):
	try:
		os.makedirs(parent_dir_path+'/csvtemp')
		return parent_dir_path+'/csvtemp'
	except Exception as err:
		print(err)

#==============================================================

def write_col_header(csv_file):
	entity_name = csv_file.split(os.sep).pop().split('.')[0]
	s = ''
	with open(csv_file, 'w') as f:
		for k in get_config()[entity_name]['columns'].keys():
			s += k+','
		s = s[:len(s)-1]+'\n'
		f.write(s)


def write_data(csv_file=None, data=None):
	entity_name = csv_file.split(os.sep).pop().split('.')[0]
	s = ''
	with open(csv_file, 'a') as f:
		for k in get_config()[entity_name]['columns'].keys():
			try:
				d = data[k]
				s += '"'+escape(d, {'"':'&quot;'})+'",'
				s = s.replace('&amp;quot;','&quot;')
			except:
				s += '"",'
		s = s[:len(s)-1]
		s = repr(s)
		s = s[1:len(s)-1]
		s = s+'\n'
		f.write(s)


def write2csv(element, attrs):
	if element == 'row':
		write_data(data=attrs)
		

def parse_xml(xml_file,csv_folder):
	entity_name = xml_file.split(os.sep).pop().split('.')[0]
	csv_file = csv_folder+os.sep+entity_name+'.csv'
	global write_data
	write_data = functools.partial(write_data, csv_file=csv_file)
	p = xml.parsers.expat.ParserCreate()
	p.StartElementHandler = write2csv
	with open(xml_file, 'rb') as f:
		write_col_header(csv_file)
		p.ParseFile(f)


#==============================================================

#=============== Main Function =================================

def xml2csv(archive_path=None, xmls_dir=None):
	csvs_dir = ''
	if archive_path:
		xmls_dir = extract_7z_archive(archive_path)
	if xmls_dir:
		csvs_dir = create_temp_csv_dir(xmls_dir)
		if xmls_dir:
			xml_files = get_xml_files(xmls_dir)
			for xml_file in xml_files:
				parse_xml(xml_file,csvs_dir)
	return csvs_dir

#==============================================================