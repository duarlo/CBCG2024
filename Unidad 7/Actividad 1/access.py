# importaciones
import os
# funcion que abre el archivo y convierte en una lista
def open_file_login(document):
    # llama la función open
    with open(document,"r") as file:
        file_text = file.read()
        file.close()
        file_list = file_text.split()
    return file_list
# funcion que remueve usuarios
def check_usrs(list,blacklist):
    for element in blacklist:
        if element in list:
            list.remove(element)
    return list
# funcion que añade a nuevos usuarios
def new_usrs(list,whitelist):
    for element in whitelist:
        if element in list:
            continue
        else:
            list.append(element)
    return list
# funcion que une y escribe el documento
def write_n_close(list,document):
    newtext =' '.join(list)
    os.remove(document)
    with open(document,"x") as file:
        file.write(newtext)
    print("se ha actualizado con exito")

# programa que administa las direciones IP
file = "Unidad 7/Actividad 1/allow_list.txt"   
list_usr = open_file_login(file)
# lista de usuarios baneados
list_ban = ["127.0.0.2","127.0.0.4","127.0.0.6"]
#lista de usuarios nuevos
list_new = ["127.0.0.16","127.0.0.17"]
without_ban_usrs = check_usrs(list_usr,list_ban)
add_new_usrs = new_usrs(without_ban_usrs,list_new)
write_n_close(add_new_usrs,file)


