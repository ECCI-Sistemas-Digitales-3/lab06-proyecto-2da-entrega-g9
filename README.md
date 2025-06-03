[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19559610&assignment_repo_type=AssignmentRepo)
# Lab06: Proyecto 2da. entrega


## Integrantes

Jaider Neider Neira


Jonnathan Smith Bueno 

## Documentación 

![17489118037012796522903990294716](https://github.com/user-attachments/assets/4ae76412-9138-46b0-874c-751421ed1639)


# Control de Motor Mezclador con Raspberry Pi y L298N

## Introducción

Este proyecto implementa el control de un motor DC para funcionar como mezclador, utilizando una Raspberry Pi y el módulo L298N para la modulación PWM. El sistema permite ajustar la velocidad y el sentido de giro del motor mediante programación en Python, con la capacidad de ser controlado remotamente a través de MQTT.

---

## Objetivos

- Configurar la Raspberry Pi para controlar el giro de un motor DC.  
- Implementar un circuito simple para el control del motor.  
- Desarrollar un programa en Python para gestionar la velocidad y dirección del giro.  
- Integrar un sistema de control remoto mediante MQTT.

---

## Materiales Utilizados

- Raspberry Pi 2W (placa principal)  
- Motor DC  
- Driver L298N (para control PWM)  
- Fuente de alimentación externa de 12V  
- Diodos de protección  
- Componentes para aislamiento eléctrico

---

## Conexiones

### Raspberry Pi
  

- GPIO 18 - PWM (utilizado en el código)  
- GPIO 23 - Enable (utilizado en el código)
![17489066010286441083028138637551](https://github.com/user-attachments/assets/27aa61e4-8d23-4efe-9679-46ed9e04cf93)

### Módulo L298N

- Enable - Conexión PWM  
- IN1 - Control de dirección  
- Entrada de 12V - Alimentación del motor  
- GND - Tierra común  
- OUT1 - Salida al motor
![17489065624854492721058160867959](https://github.com/user-attachments/assets/5151dda1-6e18-451c-b993-a8c16cf7b943)

---

## Explicación del Código Python

### Inicialización GPIO

El programa configura los pines GPIO de la Raspberry Pi en modo BCM. Se establecen como salidas el pin de PWM (GPIO 18) y el pin de habilitación del motor (GPIO 23). El PWM se inicializa con una frecuencia de 1000 Hz, permitiendo un control fino de la velocidad del motor.

### Control MQTT

El código emplea el protocolo MQTT para comunicarse con otros dispositivos o plataformas. Al iniciar, se suscribe a tres temas:

- `motor/speed`: Recibe el valor de velocidad (de 0 a 100) como porcentaje.  
- `motor/button1` y `motor/button2`: Simulan botones de seguridad. Ambos deben estar en "true" para que el motor se active.

### Lógica  de seguridad

El sistema implementa una lógica de doble seguridad: el motor solo se activa si ambos botones virtuales están en estado "true". Esto garantiza que el motor no se active accidentalmente. Si uno de los botones cambia a "false", el motor se desactiva de inmediato.

### Gestión de Velocidad

Cuando el sistema está habilitado, el valor recibido en el tema `motor/speed` se utiliza para ajustar el ciclo de trabajo del PWM, lo que a su vez regula la velocidad del motor con alta precisión.

---

## Consideraciones Importantes

### Protección del Motor

- Se utilizan diodos para evitar daños por voltajes inversos.  
- Se implementa aislamiento eléctrico para prevenir cortocircuitos.  
- El motor tiene su propia fuente de alimentación externa de 12V, evitando sobrecargar la Raspberry Pi.

### Seguridad

- El sistema requiere la confirmación de dos botones para operar, aumentando la seguridad del usuario.  
- El motor se detiene automáticamente ante cualquier cambio en los botones.  
- El control de velocidad ayuda a evitar sobrecalentamientos.

### Extensibilidad

- Gracias al uso de MQTT, es posible conectar el sistema con otros dispositivos IoT.  
- Se puede ampliar el proyecto integrando una base de datos para almacenar parámetros de mezcla.


---

## Requerimientos Funcionales

El sistema debe permitir:

- Ajuste programático de la velocidad del motor.  
- Control remoto mediante MQTT.  
- Operación segura con doble confirmación.  
- Protección contra sobrevoltajes y cortocircuitos.

---

## Conclusión

Este proyecto demuestra cómo implementar un sistema de control de motores seguro y configurable utilizando una Raspberry Pi. Es ideal para aplicaciones de mezcla o cualquier otro proceso que requiera control preciso de motores DC, combinando programación en Python con tecnologías de comunicación como MQTT.

 ## Configuración Node -RED
 
presenta las imagenes de la configuracion de Node_RED
![image](https://github.com/user-attachments/assets/9fc83c6f-8558-40d1-8d62-56b67b5fcf58)
![image](https://github.com/user-attachments/assets/6da6fbbf-53b2-4dd4-a330-0387ad3a42aa)




El sistema de control se ha complementado con una interfaz visual creada en Node-RED, permitiendo la interacción remota a través de una red local o desde una plataforma IoT. La configuración incluye:

### Estructura del Flujo

- **Velocidad del motor**: Controlada mediante un deslizador (`slider`), cuyos valores se publican al tema `motor/speed` mediante un nodo MQTT.
- **Botón 1 y Botón 2**: Simulados con interruptores (`switches`) que publican valores booleanos (`on` / `off`) a los temas `motor/button1` y `motor/button2`, activando la lógica de seguridad.
- **Visualización**: Un `gauge` (indicador circular) muestra visualmente el porcentaje de velocidad establecido.

### Temas MQTT utilizados:

- `motor/speed`: recibe el valor de velocidad (0–100%)
- `motor/button1`: estado de seguridad del botón 1 (true/false)
- `motor/button2`: estado de seguridad del botón 2 (true/false)

### Interfaz del Panel

El panel de control incluye:
- Un control deslizante para modificar la velocidad.
- Un indicador tipo gauge para visualizar el porcentaje actual.
- Dos botones para activar/desactivar los seguros de operación.
- Switches conectados a los botones virtuales.




Se presenta diagrama correspondiente al programa antes mensionado

![diagrama_digitals_3 1_page-0001 (1)](https://github.com/user-attachments/assets/b93b491b-d603-4eb0-92cd-b1329c823e8f)

[diagrama_digitals_3 (1).pdf](https://github.com/user-attachments/files/20528085/diagrama_digitals_3.1.pdf)
