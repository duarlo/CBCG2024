# Algoritmo para actualizaciones de archivos en python

## Descripción del proyecto
Una empresa de atención medica, pide actualizar periódicamente un archivo que identifica persona con acceso restringido
La información se basa en quienes están manejando los registros personales de los pacientes
Al personal se le restringe el acceso basado en su dirección IP.
Existe una lista de IP's autorizadas y una lista de empleados que se deben remover
## Abrir el archivo con la lista de permisos
para abrir el documento es necesario que exista el documento `allow_list.txt` hemos generado uno con unas IP de prueba

creamos una función la cual abre el archivo y toma su contenido para crear una lista

```python
# funcion que abre el archivo y convierte en una lista
def open_file_login(document):
    # llama la función open
    with open(document,"r") as file:
        file_text = file.read()
        file.close()
        file_list = file_text.split()
    return file_list
```

guarda el del archivo en un variable llamada `file_text` que la guarda como una cadena de caracteres y cierra el archivo y crea una lista con la cadena de texto

## Iterar a través de la lista de eliminación y elimina las IP
mediante la siguiente función itera sobre una lista la cual tiene los elementos que se desean eliminar de otra lista

```python
# funcion que remueve usuarios
def check_usrs(list,blacklist):
    for element in blacklist:
        if element in list:
            list.remove(element)
    return list

#...
# la siguiente lista 
list_ban = ["127.0.0.2","127.0.0.4","127.0.0.6"]

```

## Actualizar el archivo con la lista revisada de direcciones

con la siguiente función recibe la lista y la dirección donde queremos que sea escrita la nueva información

```python
# funcion que une y escribe el documento
def write_n_close(list,document):
    newtext =' '.join(list)
    os.remove(document)
    with open(document,"x") as file:
        file.write(newtext)
    print("se ha actualizado con exito")
```

## Resumen

- este algoritmo puede eliminar datos y escribir nuevos datos y los escribirá en el documento
- una vez escrito es necesario reiniciar, por lo que no tiene forma de reproducirlo se intento con los siguientes datos.
` 127.0.0.1 127.0.0.2 127.0.0.3 127.0.0.4 127.0.0.5 127.0.0.6 127.0.0.7 127.0.0.8 127.0.0.9 127.0.0.10 127.0.0.11 127.0.0.12 127.0.0.13 127.0.0.14 127.0.0.15`
aunque posteriormente se le puede agregar la función de restauración.
- Tambien las listas que tiene son estáticas por los que se deberían tomar de archivos.