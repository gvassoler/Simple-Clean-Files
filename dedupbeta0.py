# importing libraries
from typing import Set, Any
import os
import os.path
import time
from collections import Counter

#splash screen
print('\n\n')
print('===================================')
print('File Clean v 0.8 - Nov/2021 - gvas')
print('===================================')
print('\n')

#input search path
directory = (input('Search path: '))
print('\n\n')

#variable 'space' used to align output
spaces = ' '

#used to get and show the number of files searched
total_files = 0

#variable counter used for loop's
counter = 0

#this is the dict to save file path/attributes
gva = {}

#this is the list to save file path/attributes
gvas = []

#this is the dict to save file path/attributes
files_dict = {}

#this is the list to save file path/attributes
files_list = []

#used to initialize the prompt while
prompt = 'q'

#used to store file path
all_attrib = os.listdir(directory)

#used to fill file path/attributes dict and list
indice_nome = 0
indice_size = 1
indice_modified = 2
indice_created = 3

#here, I fill the major dict and list with OS information about the files searched
#1-filling the list 'gvas'
for files in all_attrib:
    size = os.path.getsize(f'{directory}/{all_attrib[counter]}')
    modified = time.ctime(os.path.getmtime(f'{directory}/{all_attrib[counter]}'))
    created = time.ctime(os.path.getctime(f'{directory}/{all_attrib[counter]}'))
    name = (f'{directory}/{all_attrib[counter]}')
    gvas.append(name)
    gvas.append(size)
    gvas.append(modified)
    gvas.append(created)
    counter = counter + 1
#2- filling the dict 'gva'
    gva[(indice_nome)] = (name)
    gva[(indice_size)] = (size)
    gva[(indice_modified)] = (modified)
    gva[(indice_created)] = (created)
    indice_nome = indice_nome + 4
    indice_size = indice_size + 4
    indice_modified = indice_modified + 4
    indice_created = indice_created + 4

# return indexes to initial position, because their used in the next loops
indice_nome = 0
indice_size = 1
indice_modified = 2
indice_created = 3

#this len and esp's in the gvas list is used to help align the output bellow
tab = len(gvas)
esp_nome = ''
esp_size = ''
esp_m = []
esp_s = []
show_files = []
show_name = 0
show_size = 1
show_created = 2
show_modified = 3

#output of the path sourced, 'tab' is the list gvas length, 'indice_nome` is the index of the field name in this list
while tab > indice_nome:
#the next two lines are only to allign output
    esp_nome = len(str(gva[indice_nome]))
    esp_size = len(str(gva[indice_size]))
    esp_m.append(esp_nome)
    esp_s.append(esp_size)
#store the file information in a new list 'show_files'
    show_files.append(gva[indice_nome])
    show_files.append(gva[indice_size])
    show_files.append(gva[indice_created])
    show_files.append(gva[indice_modified])
#changing the indexes values in the position to get the next files
    indice_nome = indice_nome + 4
    indice_size = indice_size + 4
    indice_modified = indice_modified + 4
    indice_created = indice_created + 4
#used to count the number of files searched
    total_files = total_files + 1
#to stop the while when the index reached the maximum value
    if tab >= indice_created:
        pass
#allign output
limit_table = len(show_files)
table_format = max(esp_m)
table_s = max(esp_s)
counter = 0
#show file table
for i in show_files:
    print(f'{show_files[show_name]}{((table_format + 2)-(esp_m[counter])) * spaces}|{2 * spaces}'
          f'{show_files[show_size]}{((table_s + 2)-(esp_s[counter]))* spaces }|{2 * spaces}'
          f'{show_files[show_modified]}  |  {show_files[show_created]}')
    show_name = show_name + 4
    show_size = show_size + 4
    show_created = show_created + 4
    show_modified = show_modified + 4
    counter = counter + 1
    if show_modified >= limit_table:
        break

#used to output the number of files encountered
print('=====================')
print(f'{total_files} arquivos na pasta.')
print('=====================')

import collections

index_name = 0
index_size = 1
index_created = 2
index_modified = 3

dup_names = []

dup_created = []
dup_modified = []

name_index = 0
size_index = 0

limit_table = len(show_files)

counter = 0
#name check stuff
all_names = []
all_names_filtered = []
count_name = 0
#size check stuff
all_sizes = []
all_sizes_filtered = []
count_size = 1
#date created check stuff
all_created = []
all_created_filtered = []
count_created = 2
#date modified check stuff
all_modified = []
all_modified_filtered = []
count_modified = 2

#getting duplicated names
for i in show_files:
    all_names.append(show_files.index(show_files[count_name]))
    all_names.append(show_files[count_name])
    count_name = count_name + 4
    if count_name >= len(show_files):
        break
all_names_filtered.append([item for item, count in collections.Counter(all_names).items() if count > 1])
print(f'all names: {all_names}')
print(f'Same name: {all_names_filtered}')
#getting duplicated sizes
for i in show_files:
    all_sizes.append(show_files.index(show_files[count_size]))
    all_sizes.append(show_files[count_size])
    count_size = count_size + 4
    if count_size >= len(show_files):
        break
all_sizes_filtered.append([item for item, count in collections.Counter(all_sizes).items() if count > 1])
print(f'all sizes: {all_sizes}')
print(f'Same size: {all_sizes_filtered}')
#getting duplicated date created
for i in show_files:
    all_created.append(show_files.index(show_files[count_created]))
    all_created.append(show_files[count_created])
    count_size = count_created + 4
    if count_created >= len(show_files):
        break
all_created_filtered.append([item for item, count in collections.Counter(all_created).items() if count > 1])
print(f'all created date: {all_created}')
print(f'same Created date: {all_created_filtered}')
#getting duplicated date modified
for i in show_files:
    all_modified.append(show_files.index(show_files[count_modified]))
    all_modified.append(show_files[count_modified])
    count_modified = count_modified + 4
    if count_modified >= len(show_files):
        break
all_modified_filtered.append([item for item, count in collections.Counter(all_modified).items() if count > 1])
print(f'all modified date: {all_modified}')
print(f'same modified date: {all_modified_filtered}')











'''
for i in show_files:
    if index_name - 1 >= limit_table:
        break
    dup_names.append([item for item, count in collections.Counter(show_files).items() if count > 1])
    (name_index.index(dup_names[0]))


repetidos.sort()


print(name_index.index(6))
print('\n')

jksize = []
repetidos = []
for i in gvas:
    if indice_size - 1 >= limit:
        break
    # jksize.append(gvas[indice_size])
    indice_size = indice_size + 4
    repetidos.append([item for item, count in collections.Counter(gvas).items() if count > 1])

repetidos.sort()

print('\n')


count = 0
ipn = ''
esp_indn= ''
esp_v = ''
for i, v in gva.items():
    indn = i - 1
    indm = i + 1
    indc = i + 2
    if (repetidos[count][0]) == v:
        esp_indn = len(str(gva[indn]))
        print(f'{gva[indn]}{((75-esp_indn) * spaces) }{v}{gva[indm]}   {gva[indc]} ')
    cont = count + 1
'''