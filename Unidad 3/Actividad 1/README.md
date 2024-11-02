# Analizar la comunicación en la capa de red
**Objetivos**

- Analizar el trafico DNS e ICMP utilizando los datos de un analizador de protocolos de red
- Que tipo de protocolo de red se utilizo en la evaluación del incidente de seguridad
- identificar el trafico malicioso para evaluar los riesgo de seguridad de una red y reforzarla

**Más información**
en el modelo TCP/IP, la IP formatea los paquetes de datos en datagramas IP. La información proporcionada en el datagrama de un paquete IP proporciona información de paquetes de datos sospechosos

## Descripción
*Eres un analista de ciberseguridad que trabaja en una empresa que se especializa en la prestación de servicios de consultoría informática. Varios clientes se pusieron en contacto con tu empresa para informar que no podían acceder al sitio web de la empresa www.yummyrecipesforme.com, y vieron el error “puerto de destino inalcanzable” después de esperar a que se cargara la página.*

*Tienes la tarea de analizar la situación y determinar qué protocolo de red se vio afectado durante este incidente. Para empezar, visitas el sitio web y también recibes el error “puerto de destino inalcanzable”. A continuación, cargas tu herramienta de análisis de red, tcpdump, y vuelves a cargar la página web. Esta vez, recibes una gran cantidad de paquetes en tu analizador de red. El analizador muestra que cuando envías paquetes UDP y recibes una respuesta ICMP devuelta a su host, los resultados contienen un mensaje de error: “udp port 53 unreachable.” (puerto udp 53 inalcanzable).*

*Dentro de los registros de DNS e ICMP  encuentras la siguiente información*

- En las dos primeras líneas del archivo de registro, ves la solicitud inicial saliente de tu computadora al servidor DNS solicitando la dirección IP de yummyrecipesforme.com. Esta solicitud se envía en un paquete UDP.
- A continuación, encontrarás marcas de tiempo que indican cuándo ocurrió el evento. En el registro, esta es la primera secuencia de números que se muestra. Por ejemplo: 13:24:32.192571. Esto muestra el tiempo 1:24 p. m., 32.192571 segundos.
- La siguiente es la dirección IP de origen y destino. En el registro de errores, esta información se muestra como: 192.51.100.15.52444 > 203.0.113.2.domain. La dirección IP a la izquierda del símbolo mayor que (>) es la dirección de origen. En este ejemplo, la fuente es la dirección IP de tu computadora. La dirección IP a la derecha del símbolo mayor que (>) es la dirección IP de destino. En este caso, es la dirección IP del servidor DNS: 203.0.113.2.domain
- La segunda y tercera líneas del registro muestran la respuesta a tu paquete inicial de solicitud ICMP. En este caso, la línea ICMP 203.0.113.2 es el comienzo del mensaje de error que indica que el paquete ICMP no se pudo entregar en el puerto del servidor DNS.
- A continuación, están el protocolo y el número de puerto, que muestra qué protocolo se utilizó para gestionar las comunicaciones y a qué puerto se entregó. En el registro de errores, esto aparece como “udp port 53 unreachable” (puerto udp 53 inalcanzable). Esto significa que el protocolo UDP se utilizó para solicitar una resolución de nombre de dominio utilizando la dirección del servidor DNS a través del puerto 53. El puerto 53, que se alinea con la extensión .domain en 203.0.113.2.domain, es un puerto bien conocido para el servicio DNS. La palabra “inalcanzable” en el mensaje indica que el mensaje no llegó al servidor DNS. Tu navegador no pudo obtener la dirección IP de yummyrecipesforme.com, que necesita para acceder al sitio web porque ningún servicio estaba escuchando en el puerto DNS receptor, como indica el mensaje de error ICMP “udp port 53 unreachable.” (puerto udp 53 inalcanzable).
- Las líneas restantes del registro indican que los paquetes ICMP se enviaron dos veces más, pero se recibió el mismo error de entrega en ambas ocasiones. 

---
# Informe sobre incidentes de ciberseguridad:Analisis de trafico de red

## Resumen del problema encontrado en el registro de DNS e ICMP
Los responsables del funcionamiento de la pagina yummyrecipies tienen un problema que al ingresar mediante la url de su pagina, tienen un error que el puerto 53 es inalcanzable.

posteriormente se utilizo un software de Análisis de paquetes y se envía una petición a yummyrecipiesforme.com y ICMP devuelve que el puerto 53 que es el de DNS no es alcanzable se vuelve a probar 3 veces y se tienen los mismos resultado.

## Análisis de los datos y medidas a implementar
por los datos mostrados queda demostrado el problema que tienen con el acceso a la pagina las siguientes acciones a tomar son:

- Revisar la configuración de la pagina web que este todo este correcto
- Si se utiliza un firewall revisar que no este bloqueando las comunicaciones con el puerto 53.
- Revisar si no hay un trafico inusual en el servidor.

Es importante realizar estas acciones a la brevedad para que vuelva a estar disponible la pagina web

## Evidencias
```sh
# la ip donde estamos solicitando el acceso a la pagina, el servidor mediante ICMP nos esta devolviendo udp port 53 unreachable
13:24:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:24:36.098564 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 
udp port 53 unreachable length 254

13:26:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:27:15.934126 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 
udp port 53 unreachable length 320

13:28:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:28:50.022967 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 
udp port 53 unreachable length 150
```