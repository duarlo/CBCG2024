# Permisos de archivo en linux

## Descripción del proyecto

Documentar los comandos necesarios para poder realizar las siguientes acciones: listar contenidos dentro de un directorio y cambiar los permisos de archivos y directorios.

## comprobar detalles del archivo y del directorio
con el comando `ls` nos permite conocer los archivos que hay en un directorio
al utilizar el atributo `-a` nos permite ver archivos ocultos y con el atritubuto `-l` nos da el archivo con los permisos que tiene el nombre del usuario y grupo al que pertenece fecha y hora de creacion y nombre del archivo tambien nos permite combinar ambos atributos

```sh
# lista el contenido en un directorio
ls
# lista el contenido del directorio mas los archivos ocultos 
ls -a
# lista el contenido del directorio y sus propiedades como permisos, usuario ,grupo,fecha y hora de creaci[on
ls -l
# tambien se puede combinar
ls -la
```

## descripción de la cadena de permisos.

El sistema de permisos consiste en 10 letras dependiendo si esta presente o ausente indicara el permiso que tiene el archivo o el directorio

el primer carácter indica si es un archivo`-` o un directorio`d`
del segundo al cuarto carácter indica que tipo de permisos tiene el usuario `u` sobre el archivo o directorio

del quinto a séptimo indica que tipo de permisos tiene el grupo`g` sobre el archivo o directorio

del octavo al decimo indica que tipo de permisos tienen otros`o` sobre el archivo o directorio

### tipos de permisos
`r` lectura equivale a 4
`w` escritura equivale a 2
`x` ejecución equivale a 1


## Cambio de permisos de un archivo
Para el cambio de permisos de un archivo o directorio se realiza de la siguinete forma.  el comando `chmod` el permiso a cambiar `u+-rwx,g+-rwx,o+-rwx` y atributo `-R`

Ejemplo
```sh
touch hola.txt
# generara un archivo con los permisos 644
chmod u+x,g+w,o-r hola.txt
# Añade permisos de ejecución al usuario añade permisos de escritura al grupo quita permisos de lectura a otros 
chmod 760 hola.txt
# lo mismo que lo anterior pero en su forma octal
```

## cambio de permisos de un archivo oculto
Es muy similar al caso anterior solo que los archivos ocultos inician con un punto en su nombre
Ejemplo
```sh
touch .adios.txt
# generara un archivo con los permisos 644 esta oculto
chmod u+x,g+w,o-r .adios.txt
# Añade permisos de ejecución al usuario añade permisos de escritura al grupo quita permisos de lectura a otros 
chmod 760 .adios.txt
# lo mismo que lo anterior pero en su forma octal
```

## Cambio de permisos de un directorio
Similar al caso anterior solo que puede añadirse un atributo para aplicar a todo el contenido del directorio
```sh
mkdir saludos
# generara un directorio con los permisos 644 
chmod u+x,g+w,o-r saludos
# Añade permisos de ejecución al usuario añade permisos de escritura al grupo quita permisos de lectura a otros 
chmod 760 saludos
# tambien puede apliarse a todo el contenido del directorio
chmod 760 -R saludos
```

## Resumen 
chmod es un comando util para la gestion de permisos de archivos en linux es importante conocer que permisos tiene tu archivo en caso de que utilices el sistema octal ya que este podría cambiar todos los permisos de usuario en cambio el modo simbólico es mas relativo a la configuración de permisos previa
