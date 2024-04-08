import shutil
import os

file_source = r"./test/"
file_destination =  r"./test_sub/"

get_files = os.listdir(file_source)

for g in get_files:
    g_list = g.split('.')
    if len(g_list) > 1:
        # print(g_list)
        #g_list[0]=name,g_list[1]=file format
        new_g = g_list[0]+'_'+'.'+g_list[1]
        shutil.copy(file_source + g ,file_source + new_g)
        shutil.move(file_source + new_g, file_destination)

        shutil.move(file_destination + new_g, file_destination+g)