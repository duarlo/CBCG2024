# Aplica técnocas de reforzamiento de SO

*Eres un analista de ciberseguridad para yummyrecipesforme.com, un sitio web que vende recetas y libros de cocina. Un panadero descontento ha decidido publicar las recetas más vendidas del sitio web para que el público pueda acceder a ellas de forma gratuita.*

*El panadero ejecutó un ataque de fuerza bruta para acceder al host de la web. Introdujo repetidamente varias contraseñas predeterminadas conocidas para la cuenta administrativa hasta que acertó con la correcta. Después de obtener las credenciales de acceso, pudo acceder al panel de administración y modificar el código fuente del sitio web. Incrustó una función de JavaScript en el código fuente que pedía a los visitantes que descargaran y ejecutaran un archivo al visitar el sitio web. Tras ejecutar el archivo descargado, los clientes eran redirigidos a una versión falsa del sitio web donde las recetas del vendedor ya estaban disponibles de forma gratuita.*

*Varias horas después del ataque, varios clientes enviaron correos electrónicos al servicio de asistencia de yummyrecipesforme. Se quejaban de que el sitio web de la empresa les había pedido que descargaran un archivo para actualizar sus navegadores. Los clientes afirmaron que, tras ejecutar el archivo, la dirección del sitio web cambió y sus computadoras personales comenzaron a funcionar más lentamente.*

*En respuesta a este incidente, el propietario del sitio web intenta iniciar sesión en el panel de administración, pero no lo consigue, por lo que se pone en contacto con el proveedor de alojamiento del sitio web. Tú y otros analistas de ciberseguridad reciben el encargo de investigar este incidente de seguridad.*

*Para abordarlo, creas un entorno sandbox para observar el comportamiento sospechoso del sitio web. Ejecuta el analizador de protocolos de red tcpdump y escribes la URL del sitio web, yummyrecipesforme.com. En cuanto se carga el sitio web, se te pide que descargues un archivo ejecutable para actualizar tu navegador. Aceptas la descarga y permites que el archivo se ejecute. Entonces observas que tu navegador te redirige a una URL diferente, greatrecipesforme.com, que está diseñada para parecerse al sitio original. Sin embargo, las recetas que vende tu empresa ahora se publican ahora gratuitamente en el nuevo sitio web.*

Los registros muestran el siguiente proceso

1. El navegador solicita una resolución DNS de la URL yummyrecipesforme.com.
2. El servidor DNS responde con la dirección IP correcta. 
3. El navegador inicia una solicitud HTTP para la página web.
4. El navegador inicia la descarga del malware.
5. El navegador solicita otra resolución DNS para greatrecipesforme.com.
6. El servidor DNS responde con la nueva dirección IP.
7. El navegador inicia una solicitud HTTP a la nueva dirección IP.

Un analista de alto nivel confirma que el sitio web se vio comprometido. El analista verifica el código fuente del sitio web. Nota que se ha agregado código JavaScript para solicitar a los visitantes del sitio web que descarguen un archivo ejecutable. El análisis del archivo descargado encontró un script que redirige los navegadores de los visitantes de yummyrecipesforme.com a greatrecipesforme.com. 

El equipo de ciberseguridad informa que el servidor web se vio afectado por un ataque de fuerza bruta. El panadero descontento pudo adivinar la contraseña fácilmente porque la contraseña de administrador seguía siendo la contraseña predeterminada. Además, no había controles para prevenir un ataque de fuerza bruta. 

# Actividades
documentar el incidente en detalle, incluida la identificación de los protocolos de red utilizados para establecer la conexión entre el usuario y el sitio web.

## informe del incidente de seguridad
El dueño de la empresa yummi recipes el cual tiene una pagina para la venta de libros de cocina y recetas, un exempleado inconformé se antes de retirarse tuvo acceso al servidor y realizo unos cambios en el JS para que descargara un complemento, este complemento causa la redireción a otra pagina la cual tiene publicadas todas las recetas de forma gratuita.

### Sección 1: Identificación del protocolo de red involucrado en el incidente
Los protocolos involucrados en esta actividad son HTTP y DNS para la redireción de la pagina web del atacante

Para la manipulación de la pagina web es necesario conectarse a un servidor por lo que tambien el puerto SSH para realizar los cambios
### Sección 2: Documentación del incidente

```sh
# la maquina envia una solicitud al DNS para la URL yummirecipesforme.com
14:18:32.192571 IP your.machine.52444 > dns.google.domain: 35084+ A? yummyrecipesforme.com. (24)
# El DNS envia a la maquina de prueba la direción IP
14:18:32.204388 IP dns.google.domain > your.machine.52444: 35084 1/0/0 A 203.0.113.22 (40)

# inicia la coneción de la pagina web
14:18:36.786501 IP your.machine.36086 > yummyrecipesforme.com.http: Flags [S], seq 2873951608, win 65495, options [mss 65495,sackOK,TS val 3302576859 ecr 0,nop,wscale 7], length 0
# 
14:18:36.786517 IP yummyrecipesforme.com.http > your.machine.36086: Flags [S.], seq 3984334959, ack 2873951609, win 65483, options [mss 65495,sackOK,TS val 3302576859 ecr 3302576859,nop,wscale 7], length 0
14:18:36.786529 IP your.machine.36086 > yummyrecipesforme.com.http: Flags [.], ack 1, win 512, options [nop,nop,TS val 3302576859 ecr 3302576859], length 0
# Realiza una inserción de datos utiliza el metodo GET
14:18:36.786589 IP your.machine.36086 > yummyrecipesforme.com.http: Flags [P.], seq 1:74, ack 1, win 512, options [nop,nop,TS val 3302576859 ecr 3302576859], length 73: HTTP: GET / HTTP/1.1
14:18:36.786595 IP yummyrecipesforme.com.http > your.machine.36086: Flags [.], ack 74, win 512, options [nop,nop,TS val 3302576859 ecr 3302576859], length 0
# utiliza el protocolo 80 para http
…<a lot of traffic on the port 80>... 

# vuelve a solicitar al DNS la siguiente direción greatrecipies.com
14:20:32.192571 IP your.machine.52444 > dns.google.domain: 21899+ A? greatrecipesforme.com. (24)
# envia la siguiente direción IP la del servidor de greatrecipies.com 
14:20:32.204388 IP dns.google.domain > your.machine.52444: 21899 1/0/0 A 192.0.2.17 (40)
# incia conexión con el servidor
14:25:29.576493 IP your.machine.56378 > greatrecipesforme.com.http: Flags [S], seq 1020702883, win 65495, options [mss 65495,sackOK,TS val 3302989649 ecr 0,nop,wscale 7], length 0
14:25:29.576510 IP greatrecipesforme.com.http > your.machine.56378: Flags [S.], seq 1993648018, ack 1020702884, win 65483, options [mss 65495,sackOK,TS val 3302989649 ecr 3302989649,nop,wscale 7], length 0
14:25:29.576524 IP your.machine.56378 > greatrecipesforme.com.http: Flags [.], ack 1, win 512, options [nop,nop,TS val 3302989649 ecr 3302989649], length 0
14:25:29.576590 IP your.machine.56378 > greatrecipesforme.com.http: Flags [P.], seq 1:74, ack 1, win 512, options [nop,nop,TS val 3302989649 ecr 3302989649], length 73: HTTP: GET / HTTP/1.1
14:25:29.576597 IP greatrecipesforme.com.http > your.machine.56378: Flags [.], ack 74, win 512, options [nop,nop,TS val 3302989649 ecr 3302989649], length 0
…<a lot of traffic on the port 80>... 
```
### Sección 3: Recomendación de una solución para los ataques de fuerza bruta
Recomendaciones restablecer la versión anterior de la pagina web antes de la inserción de Código malicioso dependiendo en la situación en la que se encuentra.

- Había un backup, realizar la carga del backup lo más pronto posible
- No había un backup o el atacante daño el código fuente: solicitar a un experto la búsqueda de ese código malicioso.

Si esta en el segundo escenario una recomendación adicional tenga su código fuente en un repositorio y aplique las siguientes medidas de seguridad para las contraseñas

Fortalecer las claves para ingresar al servidor.

- Evite utilizar las contraseñas default
- Utilice contraseñas con mínimo de 8 caracteres y caracteres especiales
- Cambie las contraseñas de vez en cuando al menos cada 6 meses
- No de contraseñas clave para ingresar al servidor, adminístrelas desde el panel de control y asigne niveles de acceso
- 