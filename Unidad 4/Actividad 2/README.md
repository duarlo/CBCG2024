# Filtros a consultas SQL

Las empresas pueden guardas sus datos en bases de datos relacionales, este tipo de bases de datos utilizan un lenguaje para realizar sus búsquedas, el más común es SQL por lo que el dominio de este lenguaje resultara indispensable.

## Observaciones

se realizara una breve descripción de la estructura de la base de datos. Solo se dará ejemplo de las búsquedas y una pequeña descripción
Nombre de la DB:`Organization`
- tabla `log in attempts`
    - columna `event_id` numérico
    - columna `username` cadena de texto
    - columna `login_date` fecha
    - columna `login_time` hora
    - columna `country` cadena de texto
    - columna `ip_address` cadena de texto
    - columna `success` booleano
- tabla `employees`
    - columna `employee_id` numérico
    - columna `device_id` cadena de texto
    - columna `username` cadena de texto
    - columna `department` cadena de texto
    - columna `office` cadena de texto

# Ejemplo de consultas:

Se dará una muestra de los consultas y un ejemplo mas general
Devolver los datos de intentos fallidos de ingreso después de las horas de trabajo

```sql
-- devulvera todas las columnas de la tabla log_in_attempts donde el valor de hora de logeo despues de las 6 y que sean fallidos.
SELECT *FROM log_in_attempts
WHERE login_time > '18:00' AND success = FALSE;
```

Devolver los intentos de ingreso durante un periodo.

```sql
-- devulvera todas las comlumnas de la tabla log_in_attempts cuya fecha de ingreso sea entre el el dia 9 y 8 de mayo.
SELECT * FROM log_in_attempts 
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
```

En la tabla guarda datos de México de las siguientes formas MEX o MEXICO enviara los datos que coincidan con estas dos formas

```sql
-- devuelve todas las columnas de la tabla que coincidan con la cadana inicial de MEX
SELECT * FROM log_in_attempts 
WHERE NOT country LIKE 'MEX%';
```

En la tabla employees queremos filtrar todas las sucursales del este y que sean del departamento de marketing

```sql
-- devuelve datos que sean del departamento de marketing y sean de las sucursales del este
SELECT * FROM employees 
WHERE department = 'Marketing' AND office LIKE 'East%';
```

En la tabla employees queremos filtrar dos departamentos finanzas y ventas

```sql
-- nos devielve datos de trabajadores de finanzas o ventas
SELECT * 
FROM employees 
WHERE department = 'Finance' OR department = 'Sales';
```

En la tabla employees queremos filtrar los trabajadores que no sean TI

```sql
-- si pertenece a Information Technology no lo imprime en pantalla
SELECT * 
FROM employees 
WHERE NOT department = 'Information Technology';
```

# Conclusiones

Los filtros SQL nos permiten realizar búsquedas entre los datos que coincidan con los parámetros sin embargo es importante conocer las sintaxis para obtener lo que deseamos y que la consola no nos devuelva un error.

- para búsquedas utilizamos el comando `WHERE` 
- especificamos lo que queremos buscar en determinadas columnas y podemos aplicar los diferentes operadores en este caso ` = ` y ` > `
- Si requerimos que un  elemento cumpla simultáneamente dos condiciones utilizamos `AND` como enlace entre condiciones
- Si requerimos que sea alguna de las dos `OR`
- Si requerimos que contenga cierto grupo de caracteres `&`