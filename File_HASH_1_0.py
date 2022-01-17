print('\n\n\n\n\n\n')
print('|File HASH - RELEASE 1.0 - 2022|')

import os
import time
import hashlib
import re
import collections
from collections import Counter
import tqdm
from tqdm import tqdm

md5_hash = hashlib.md5()
main_menu = True
main_exit = True
user_direction = ''
fil_files_size = {}
sel_files_size = {}
show_result = {}
dct_size = {}
dct_hash = {}
gva = {}

lst_hash = []
dup_hash = []
lst_size = []
dup_size = []
gvas = []

run_loop = True
contados = 0
counter = 0
status = 0
passd = 0
passo = 0



#===============INPUT_PATH===============INPUT_PATH===============INPUT_PATH===============INPUT_PATH=============
print('\n\n\n\n\n\n')
user_path = input('Location to search duplicated files: ')
gvas_path = os.walk(user_path)
#===============INPUT_PATH===============INPUT_PATH===============INPUT_PATH===============INPUT_PATH=============




#===GETTING_FILE_INFO=============GETTING_FILE_INFO=========GETTING_FILE_INFO===============GETTING_FILE_INFO======
for subdir, dirs, files in gvas_path:
    for file in files:
        filepath = subdir + os.sep + file
        if os.path.isfile(filepath) == True:
            only_name, extension = os.path.splitext(file)
            size = os.path.getsize(filepath)
            created = time.ctime(os.path.getmtime(filepath))
            modified = time.ctime(os.path.getctime(filepath))
            gva[counter] = filepath
            gva[counter + 1] = only_name
            gva[counter + 2] = extension
            gva[counter + 3] = size
            gva[counter + 4] = created
            gva[counter + 5] = modified
            dct_size[filepath] = size
            counter += 6
            gvas.append(filepath)
            gvas.append(only_name)
            gvas.append(extension)
            gvas.append(size)
            gvas.append(created)
            gvas.append(modified)
            lst_size.append(size)
            print(only_name)
            status += 1
print('\n\n\n\n\n\n')
for i in tqdm(range(1000000),ncols=120):
    pass
print(f'Checking {status} files...')
#===GETTING_FILE_INFO=============GETTING_FILE_INFO=========GETTING_FILE_INFO===============GETTING_FILE_INFO======




#====FILTER_SIZE===========FILTER_SIZE===========FILTER_SIZE===========FILTER_SIZE===========FILTER_SIZE===========
dup_size = ([item for item, count in collections.Counter(lst_size).items() if count > 1])
gabriel = 0
duplicate_sizes= {}
duplicate_sizes = Counter(lst_size)
for i, v in duplicate_sizes.items():
    if v > 1:
        gabriel = gabriel + v
run_loop = True
contados = 0
passd = 0
passo = 0
pahash = 0
vassoler = 0
while run_loop == True:
    if passd == 1:
        contados = contados + 1
    for i, v in dct_size.items():
        if dct_size == {}:
            print('Duplicate files not found..')
            run_loop = False
        if v == dup_size[contados]:
            fil_files_size[i] = v
            vassoler += 1
            passo += 1
        if vassoler == gabriel:
            run_loop = False
            break
        pahash = pahash + 1
        if pahash == len(dct_size):
            passd = 1
            pahash = 0
            run_loop == True
#====FILTER_SIZE===========FILTER_SIZE===========FILTER_SIZE===========FILTER_SIZE===========FILTER_SIZE===========




#====FILTER_HASH========FILTER_HASH========FILTER_HASH========FILTER_HASH========FILTER_HASH========FILTER_HASH====
for i, v in fil_files_size.items():
    md5_hash = hashlib.md5()
    a_file = open(i, "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    dct_hash[i] = digest
    lst_hash.append(digest)
dup_hash= ([item for item, count in collections.Counter(lst_hash).items() if count > 1])
gabriel = 0
duplicate_hashes = {}
duplicate_hashes = Counter(lst_hash)
for i, v in duplicate_hashes.items():
    if v > 1:
        gabriel = gabriel + v
run_loop = True
contados = 0
passd = 0
passo = 0
pahash = 0
vassoler = 0
while run_loop == True:
    if passd == 1:
        contados = contados + 1
    for i, v in dct_hash.items():
        if dct_hash == {}:
            print('Duplicate files not found..')
            run_loop = False
        if v == dup_hash[contados]:
            show_result[i] = v
            vassoler += 1
            passo += 1
        if vassoler == gabriel:
            run_loop = False
            break
        pahash = pahash + 1
        if pahash == len(dct_hash):
            passd = 1
            pahash = 0
            run_loop == True
#====FILTER_HASH========FILTER_HASH========FILTER_HASH========FILTER_HASH========FILTER_HASH========FILTER_HASH====




#====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT=========
for i, v in show_result.items():
    print(f'{i}           {v}')
#SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT====SHOW_OUTPUT=========




#=========EXIT===========EXIT=========EXIT=========EXIT===============EXIT==========EXIT==========EXIT========
print('\n\n\n\n')
user_direction = input('Quit?  yes/no: ')
if user_direction == 'yes':
    main_menu = False
elif user_direction == 'no':
    main_exit = False
    main_menu = True
elif user_direction != 'yes' or user_direction != 'no':
    while main_exit == True:
        user_direction = input('Type yes or no to quit: ')
        if user_direction == 'yes':
            main_menu = False
            main_exit = False
        elif user_direction == 'no':
            main_exit = False
            main_menu = True
# =========EXIT===========EXIT=========EXIT=========EXIT===============EXIT==========EXIT==========EXIT=======
















