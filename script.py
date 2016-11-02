#!/usr/bin/env python3.5

import argparse
import os
import shutil

from mod_xml2csv import xml2csv
from mod_csv2mysql import load_csvs

parser = argparse.ArgumentParser(description='7z -> XML -> csv -> MySQL')
parser.add_argument("file_path",help='''Please pass the following as argument
	7z file path (OR) directory path where xmls are located
	''')
args = parser.parse_args()

csvs_dir = ''
if os.path.isfile(args.file_path):
	csvs_dir = xml2csv(archive_path=args.file_path)
else:
	csvs_dir = xml2csv(xmls_dir=args.file_path)
if csvs_dir:
	load_csvs(csvs_dir)
	shutil.rmtree(csvs_dir)
