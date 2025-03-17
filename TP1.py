from gpiozero import Buzzer, LED, OutputDevice
from Freenove_DHT import DHT
from time import sleep

alarmvisuel = LED(17)
alarmsonore = Buzzer(5)
DHTPin = 13
motorPins = (18, 23, 24, 25)
motors = list(map(lambda pin: OutputDevice(pin), motorPins))
CCWStep = (0x01,0x02,0x04,0x08)
CWStep = (0x08,0x04,0x02,0x01)

def alarmVisuelON():
    alarmvisuel.on()
    
def alarmVisuelOFF():
    alarmvisuel.off()

def alarmSonoreON():
    alarmsonore.on()
    
def alarmSonoreOFF():
    alarmsonore.off()
    
def moveOnePeriod(direction,ms):    
    for j in range(0,4,1):     
        for i in range(0,4,1):  
            if (direction == 1):
                motors[i].on() if (CCWStep[j] == 1<<i) else motors[i].off()
            else :              
                motors[i].on() if CWStep[j] == 1<<i else motors[i].off()
        if(ms<3):       # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
            ms = 3
        sleep(ms*0.001) 

def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)
        
def motorStop():
    for i in range(0,4,1):
        motors.off()
        
def temp_loop():
    dht = DHT(DHTPin)
    sleep(1) 
    counts = 0
    while(True):
        counts += 1
        for i in range(0,15):            
            chk = dht.readDHT11()
            if (chk == 0):  
                break
            sleep(0.1)
        return dht.getTemperature()
        sleep(2)