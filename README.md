[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19559610&assignment_repo_type=AssignmentRepo)
# Lab06: Proyecto 2da. entrega


## Integrantes

Jaider Neider Neira


Jonnathan Smith Bueno 

## Documentación

 Control de mescaldor  con Raspberry Pi y MQTT



Este proyecto implementa un controlador de motor DC utilizando una Raspberry Pi, con comunicación inalámbrica mediante el protocolo MQTT. El sistema incorpora un mecanismo de seguridad de doble botón, donde el motor solo se activa si ambos botones virtuales están presionados.


Raspberry Pi (Controlador principal)
Driver de Motor (Para manejar potencia y dirección)
Broker MQTT (Middleware para comunicación remota)
Cliente MQTT (Envía comandos desde otro dispositivo)

Comunicación MQTT
El sistema se comunica mediante tres tópicos MQTT:

Tópico	Descripción	Valores aceptados
motor/speed	Controla la velocidad del motor	0 (apagado) a 100 (máxima velocidad)
motor/button1	Estado del primer botón de seguridad	"true" (activado) o "false" (desactivado)
motor/button2	Estado del segundo botón de seguridad	"true" o "false"

Lógica de Control
1. Habilitación del Motor
El motor solo se enciende si:

python
motor_enabled = (BUTTON1_STATE == True) and (BUTTON2_STATE == True)
Si cualquiera de los botones se desactiva ("false"), el motor se apaga inmediatamente.

2. Control de Velocidad (PWM)
Si el motor está habilitado, acepta cambios de velocidad mediante motor/speed.

Si se desactiva, la velocidad se establece en 0% (frenado suave).

3. Señal de Enable (ENABLE_PIN)
Este pin activa/desactiva el driver del motor.
Solo está en HIGH cuando ambos botones están activos.

Diseños e implementación sobre un giro de un motor como mesclador el cual está programada en Python esta implementación esta programada en una Raspebrry pi y como adicional se conecta un modulo L298N para su modulación PWM  

Designs and implementation on a motor rotation as a mixer which is programmed in Python. This implementation is programmed on a Raspberry Pi and additionally an L298N module is connected for its PWM modulation. 

Objetivos 

Configuración de Raspberry pi para contrarl giro de motor 

Implementar circuito simple para el giro 

Programación en Python para velocidad y giro. 

 

Materiales. 
Rasberry pi 2w  placa a utilizar para nuestro mesclador. 
Motor DC  
Driver L298N  
Fuente de alimentación 12V 

 

Conexión 
Raberry pi2w 
GPIO 17 conector Giro 
GPIO 13 Conector PWM 
L298N 
Enable conector PWM 
Pin IN1 para sentido de giro de motor. 
Entrada 12V 
Tierra 
OUT1 Salida de motor 1 

 

Consideración. 

Protección de voltaje con diodos para evitar daños en el motor. 
Aislamiento eléctrico para cortos eléctricos. 
Una fuente externa para el motor. 
Implementación de una base de datos para tener unos parámetros de mezcla. 

 
presenta las imagenes de la configuracion de Node_RED
![image](https://github.com/user-attachments/assets/9fc83c6f-8558-40d1-8d62-56b67b5fcf58)
![image](https://github.com/user-attachments/assets/6da6fbbf-53b2-4dd4-a330-0387ad3a42aa)

Se presenta diagrama correspondiente al programa antes mensionado

![diagrama_digitals_3 1_page-0001 (1)](https://github.com/user-attachments/assets/b93b491b-d603-4eb0-92cd-b1329c823e8f)

[diagrama_digitals_3 (1).pdf](https://github.com/user-attachments/files/20528085/diagrama_digitals_3.1.pdf)
