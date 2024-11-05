# Análisis del reforzamiento de la red

Descripción
*Eres un analista de seguridad que trabaja para una organización de redes sociales. La organización experimentó recientemente una importante filtración de datos, que ha puesto en peligro la seguridad de la información personal de sus clientes, como nombres y direcciones. Tu organización quiere implementar prácticas sólidas de refuerzo de la red que puedan llevarse a cabo de forma coherente para evitar ataques y filtraciones en el futuro.*

*Después de inspeccionar la red de la organización, descubres cuatro vulnerabilidades importantes. Estas vulnerabilidades son las siguientes:*

1. *Los empleados de la organización comparten las contraseñas.*
2. *La contraseña del administrador de la base de datos es la predeterminada.*
3. *Los firewalls no tienen reglas establecidas para filtrar el tráfico que entra y sale de la red.*
4. *No se utiliza la autenticación multifactor (MFA).*

*Si no se toman medidas para abordar estas vulnerabilidades, la organización corre el riesgo de experimentar otra filtración de datos u otros ataques en el futuro.*

*En esta actividad, redactarás una evaluación de riesgos de seguridad para analizar el incidente y explicar qué métodos se pueden utilizar para proteger aún más la red.*

---

# Informe de evaluación de riesgos de seguridad

## Selecciona hasta tres herramientas y métodos de reforzamiento a implementar
Recomendaría que cambiar la política de contraseñas,Filtrado de puertos y autenticación multifactor (MFA).

## Explica tus recomendaciones

- Cambios en la política de contraseñas:
Utilizar métodos como el hashing para las contraseñas, establecer contraseñas de una minima cantidad de caracteres que no sean consecutivos o que no sean comunes, Que cada empleado tenga su inicio de sesión para no compartir las contraseñas,cambiar las contraseñas predeterminadas: esto evitara que el ingreso al sistema no sea viable para ataques de fuerza bruta o también si hay configuraciones predeterminadas evitar que gente ingrese de forma no deseada
- Filtrar puertos:
Desde la configuración del firewall inhabilitar puertos que no se necesiten, disminuyendo la superficie de ataque
- Emplear MFA
en caso de que se adivine la contraseña o algo similar todavía requieren conocer el otro factor para ingresar al sistema
