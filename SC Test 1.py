from machine import Pin
import time as t

#BM 1
In1=Pin(6,Pin.OUT) 
In2=Pin(7,Pin.OUT)  
EN_A=Pin(8,Pin.OUT)

#BM 2
In3=Pin(4,Pin.OUT)  
In4=Pin(3,Pin.OUT)  
EN_B=Pin(2,Pin.OUT)

#FM 1
In11=Pin(19,Pin.OUT) 
In22=Pin(20,Pin.OUT)  
EN_AA=Pin(21,Pin.OUT)

#FM 2
In33=Pin(18,Pin.OUT) 
In44=Pin(17,Pin.OUT)  
EN_BB=Pin(16,Pin.OUT)

EN_A.high()
EN_B.high()
EN_AA.high()
EN_BB.high()

def forward():
    In1.low()
    In2.high()
    In3.high()
    In4.low()
    In11.low()
    In22.high()
    In33.high()
    In44.low()

def backward():
    In1.high()
    In2.low()
    In3.low()
    In4.high ()
    In11.high()
    In22.low()
    In33.low()
    In44.high()  

def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    In11.low()
    In22.low()
    In33.low()
    In44.low()
    
while True:
    forward()
    print("Forward")
    t.sleep(2)
    stop()
    print("Stop")
    t.sleep(2)
    backward()
    print("Backward")
    t.sleep(2)
    stop()
    print("Stop")
    t.sleep(2)