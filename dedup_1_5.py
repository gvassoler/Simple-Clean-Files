import os
import time
import sys
import collections
import hashlib

print('|Dedup files 1.4 @gvas|')

#Prompt while
run_loop = 'y'
all_name_length = []
all_size_length = []
counter = 0
gva = {}
gvas = []
pointer = True
user_action = 3


print("Ex.: /home ")
user_path = input('search path: ')
gvas_path = os.walk(user_path)
counter = 0


#Search dup files:   (3)

if user_action == 3:
    print('\n ')


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

                counter += 6
                gvas.append(filepath)
                gvas.append(only_name)
                gvas.append(extension)
                gvas.append(size)
                gvas.append(created)
                gvas.append(modified)
                print(only_name)
                

    # filtrando repetidos
    gva_len = int(len(gva.items()))
    # Output variables:

    index_dic_size = {}

    for i in range(3, gva_len, 6):
        index_dic_size[i] = (gva[i])
        index_dic_size[i] = gvas.index(gvas[i])

    index_list_size = []

    for i, v in index_dic_size.items():
        index_list_size.append(v)
    dup_size = []

    dup_size = ([item for item, count in collections.Counter(index_list_size).items() if count > 1])

    sel_files_size = {}
    for i in dup_size:
        sel_files_size[dup_size.index(i)] = i

    fil_files_size = {}

    run_loop = True
    contados = 0
    passd = 0
    passo = 0
    edge_of_the_world = 0
    while run_loop == True:
        if passd == 1:
            contados += 1

            if contados == len(dup_size):
                #print(f'size: {contados + 1}')
                break

        for i, v in index_dic_size.items():
            if sel_files_size == {}:
                print('Duplicate files not found..')
                run_loop = False

            if contados == len(dup_size):
                edge_of_the_world = 1
            if len(dup_size) == 0:
                print('There is no files duplicated in this path. Bye')
                sys.exit()
            if v == sel_files_size[contados]:
                fil_files_size[i] = v
                passo += 1
            if edge_of_the_world == 1:
                run_loop = False
            if passo > len(index_dic_size):
                passo = 0

                passd = 1


    ind_show_all = 0
    ind_show_name = 0
    ind_show_extension = 0
    ind_show_size = 0
    ind_show_created = 0
    ind_show_modified = 0
    deletar = {}
    repdel = []
    for i, v in fil_files_size.items():
        ind_show_all = i - 3
        ind_show_name = i - 2
        ind_show_extension = i - 1
        ind_show_size = i
        ind_show_created = i + 1
        ind_show_modified = i + 2
        #print(f'{gva[ind_show_all]}   {gva[ind_show_size]}   {gva[ind_show_created]}   {gva[ind_show_modified]}')
        md5_hash = hashlib.md5()
        a_file = open(gva[ind_show_all], "rb")
        content = a_file. read()
        md5_hash. update(content)
        digest = md5_hash. hexdigest()
        deletar [i] = (digest)
        deletar [i+1] = (gva[ind_show_all])
        deletar [i+2] = (gva[ind_show_size])
        deletar [i+3] = (gva[ind_show_modified])
        repdel.append(digest)




    fezes = []
    fezes = ([item for item, count in collections.Counter(repdel).items() if count > 1])

    deletarit = int(len(fezes))
    countdel = deletarit

    ghy = 0
    ghw = 1
    menufile = 1
    lixo = {}
    count_files = deletarit
    size_field = 0
    byte_field = 0
    space_counter = 1
    spaces = ' '
    #esp_indn = len(str(gva[indn]))
    #print(f'{gva[indn]}{((75 - esp_indn)


while countdel == deletarit:
        print('=============================================================================================')
        print(f'Remains {count_files} files duplicated')
        for i, v in deletar.items():

            out_hash = i
            out_full = i+1
            out_size = i+2
            out_date = i+3



            if v == fezes[ghy]:
                size_field = len(str(deletar[out_full]))
                byte_field = len(str(deletar[out_size]))
                print(f'{menufile}: {deletar[out_full]}{((120-size_field) * spaces) }{deletar[out_size]}{((8-byte_field) * spaces) }  {deletar[out_date]}  {deletar[out_hash]}')
                lixo[menufile]=(deletar[i + 1])
                ghw = ghw + 1

                menufile = menufile + 1
        print('*********************************************')
        print('Attention: The others files will be excluded!')
        print('*********************************************')
        #morre = int(input('Keep only the file number: '))
        morre = 1
        del lixo[morre]
        space_counter = space_counter + 1
        print('\n')

        print('=============================================================================================')
        for i, v in lixo.items():
            os.remove(v)
            print(f'File: {v} deleted.')

        count_files = count_files - 1
        ghy = ghy + 1
        menufile = 1
        time.sleep(0.3)

        lixo.clear()

        if ghy == deletarit:
            print('Finished')
            countdel = countdel+1


























run_loop = 'n'










