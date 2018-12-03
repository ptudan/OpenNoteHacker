import os
#os.chdir("C:\\Users\\Paul\\Documents\\Senior\\personal projects\\offline_search_saver\\g")
from google import google
import sys
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PageResult import PageResult
results_path = ''

print('Enter your search:')
q = input()
print('Enter num pages desired:')
p = (int)(input())
print('Enter the save depth for links (2 recommended):')
d = (int)(input())

initial_results = google.search(q, p)

os.chdir('results')
folder_name = q+'_'+str(time.time())
os.mkdir(folder_name)
os.chdir(folder_name)
i = initial_results[0]
# print(i.name) # The title of the link
# print(i.link) # The external link
# print(i.google_link) # The google link
# print(i.description) # The description of the link
# print(i.thumb) # The link to a thumbnail of the website (NOT implemented yet)
# print(i.cached) # A link to the cached version of the page
# print(i.page) # What page this result was on (When searching more than one page)
# print(i.index) # What index on this page it was on
# print(i.number_of_results) # The total number of results the query returned

# final_results = []
# for i in initial_results:
p = PageResult(i.name, i.link, i.page, i.index, i.description)
h = urlopen(p.link).read()
filename = 'result' + str(p.page) + '_' + str(p.index) + '.html'
f = open(filename, 'w')
s = BeautifulSoup(h, 'html.parser', from_encoding='utf-8')
f.write(str(s.prettify()))
f.close()