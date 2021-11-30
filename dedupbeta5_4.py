from typing import Set, Any
import os
import os.path
import time
from collections import Counter

print('\n\n')
print('===================================')
print('File Clean v 0.8 - Nov/2021 - gvas')
print('===================================')

# Input Path:
chosen_path = (input('Search path: '))
#
print('\n')

# ===============VARIABLES AND OBJECTS===============
gva = {}
gvas = []
# Output - screen/alignment:
all_name_length = []
all_size_length = []
spaces = ' '
# User path
gvas_path = os.listdir(chosen_path)
# Miscellaneous:
total_files = 0
# Pointers variables - setting pointers to first record
pointer_name, pointer_size, pointer_created, pointer_modified, counter = 0, 1, 2, 3, 0

# FOR to store OS info:
for files in gvas_path:
    # OS data collect:
    size = os.path.getsize(f'{chosen_path}/{gvas_path[counter]}')
    modified = time.ctime(os.path.getmtime(f'{chosen_path}/{gvas_path[counter]}'))
    created = time.ctime(os.path.getctime(f'{chosen_path}/{gvas_path[counter]}'))
    name = (f'{chosen_path}{gvas_path[counter]}')
    short_name, file_extension = os.path.splitext(f'{gvas_path[counter]}')
    # Filling the LIST:
    gvas.append(name)
    gvas.append(size)
    gvas.append(created)
    gvas.append(modified)
    # Filling the DICT:
    gva[(pointer_name)] = (name)
    gva[(pointer_size)] = (size)
    gva[(pointer_created)] = (created)
    gva[(pointer_modified)] = (modified)
    # Formating output items
    name_length = len(str(gva[pointer_name]))
    size_length = len(str(gva[pointer_size]))
    all_name_length.append(name_length)
    all_size_length.append(size_length)
    # Setting pointers to next record:
    counter += 1
    pointer_name, pointer_size, pointer_created, pointer_modified = \
        pointer_name + 4, pointer_size + 4, pointer_created + 4, pointer_modified + 4

# Returning pointers to default values:
pointer_name, pointer_size, pointer_created, pointer_modified, counter = 0, 1, 2, 3, 0

# Output variables:
spaces_for_name = max(all_name_length)
spaces_for_size = max(all_size_length)
# Showing found files:
for i in gvas:
    print(f'{gvas[pointer_name]}{((spaces_for_name + 2) - (all_name_length[counter])) * spaces}|{2 * spaces}'
          f'{gvas[pointer_size]}{((spaces_for_size + 2) - (all_size_length[counter])) * spaces}|{2 * spaces}'
          f'{gvas[pointer_created]}  |  {gvas[pointer_modified]}')
    pointer_name, pointer_size, pointer_created, pointer_modified = \
        pointer_name + 4, pointer_size + 4, pointer_created + 4, pointer_modified + 4
    total_files += 1
    counter += 1
    if pointer_modified >= len(gvas):
        break
print('=====================')
print(f'{total_files} arquivos na pasta.')
print('=====================')

import collections

g = 0
result = []
a = 0
pointer_size = 1
dup_ind = {}
filt_dup_ind = []
print('\n')
tamanho_gva = int(len(gva.items()))
index_dic = {}
# print(pointer_size)
storage_files = []
compar = []

for i in range(1, tamanho_gva, 4):
    index_dic[i] = (gva[i])
    index_dic[i] = gvas.index(gvas[i])
for i, v in gva.items():
    if i == 0:
        break
calcul = {}
virada = []

loops_search = len(storage_files)
loops_itens = int(len(index_dic))
print('==========INDEX_DIC==========')
for i, v in index_dic.items():
    print(f'Index:    {i}    Value:    {v}')
    calcul[i] = v
    virada.append(v)
# print(tamanho_gva)

storage_files=([item for item, count in collections.Counter(virada).items() if count > 1])
print(f'dddddddddddddddddddddddddddddddddddddddddddddd')
print(storage_files)
counter = len(storage_files)
counter1 = len(index_dic)
contados = 0
sel_files = {}
for i in storage_files:
    sel_files[storage_files.index(i)]=i

fil_files = {}

print(sel_files)
passo = 0
passo1 =1
get = 0
passd =0
volta = 0

while get == 0:
    if passd == 1:
        contados +=1

        if contados == len(storage_files)-1:
            print(f'size: {contados+1}')
            get = 1
    for i, v in index_dic.items():
        if v == sel_files[contados]:
            fil_files[i] = v
            passo += 1
        if passo > len(index_dic):
            passd = 1


selection_number=len(sel_files)
print(selection_number)
print(gvas[5])
print(gva[5])


for v in fil_files.items():
    print(v)



    print(i)
# Showing found files:
sn=0
sc=0
sm=0
for i, v in fil_files.items():
    sn = i-1
    sc = i+1
    sm = i +2
    print(f'{gva[sn]}          {gva[i]}       {gva[sc]}       {gva[sm]}')



