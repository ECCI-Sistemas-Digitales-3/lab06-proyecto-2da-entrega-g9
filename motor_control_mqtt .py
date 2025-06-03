
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

# Pines de control
PWM_PIN = 18
ENABLE_PIN = 23
BUTTON1_STATE = False
BUTTON2_STATE = False

# Inicializar GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)
pwm = GPIO.PWM(PWM_PIN, 1000)
pwm.start(0)

# Variables
motor_enabled = False

# Callback de conexión MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT con código de resultado " + str(rc))
    client.subscribe("motor/speed")
    client.subscribe("motor/button1")
    client.subscribe("motor/button2")

# Callback de mensajes MQTT
def on_message(client, userdata, msg):
    global motor_enabled, BUTTON1_STATE, BUTTON2_STATE
    topic = msg.topic
    payload = msg.payload.decode()
    
    if topic == "motor/speed":
        speed = int(payload)
        if motor_enabled:
            pwm.ChangeDutyCycle(speed)
    elif topic == "motor/button1":
        BUTTON1_STATE = payload == "true"
    elif topic == "motor/button2":
        BUTTON2_STATE = payload == "true"
    
    motor_enabled = BUTTON1_STATE and BUTTON2_STATE
    GPIO.output(ENABLE_PIN, motor_enabled)
    if not motor_enabled:
        pwm.ChangeDutyCycle(0)

# MQTT setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
