import os
import sys
import io
import time
import re
from bs4 import BeautifulSoup
from google.google import google
from PageResult import PageResult
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
results_path = ''


print('Enter your search: ', end='')
q = input()
print('Enter num pages desired: ', end='')
p = (int)(input())
print('Enter the save depth for links (2 recommended): ', end='')
d = (int)(input())

initial_results = google.search(q, p)
fs = ''
for c in q:
	if c not in ['*','.','/','\\','[',']',':',';','|','=','+',',',"'",'"']:
		fs += c
os.chdir('results')
folder_name = str(time.time())+'_'+fs
os.mkdir(folder_name)
os.chdir(folder_name)



final_results = []
for i in initial_results:
	p = PageResult(i.name, i.link, i.page, i.index, i.description)
	try:
		h = urlopen(p.link).read()
		d = urlparse(p.link)
		filename = 'pg' + str(p.page) + '_ind' + str(p.index)
		if(d is not None):
			filename += '_' + d.netloc
			# dom = re.search(r'(w{3}\.)([A-Za-z0-9]*)', d.netloc)
			# print(d.netloc)
			# if(dom is not None):
			# 	print(dom.group(2))
		filename+='.html'
		with io.open(filename, 'w', encoding='utf-8') as f:
			f.write(str(BeautifulSoup(h, 'html.parser', from_encoding='utf-8')))
		#f.write(str(s.prettify()))
		f.close()
	except HTTPError as err:
		print(str(err) + ' From: ' + p.name)
		continue