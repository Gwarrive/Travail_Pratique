import tkinter as tk
from TP1 import alarmVisuelON, alarmVisuelOFF, alarmSonoreON, alarmSonoreOFF, moveSteps, temp_loop

mode_test = False
door_open = False
temperature = float(0)
reading = True

def changing_mode():
    test = ""
    if mode_test:
        test = "Activé"
    else:
        test = "Désactivé"
    
    label_mode_test.config(text=f"Mode Test : {test}")

def check_state(mode_test):
    state= ""
    if mode_test:
        state = "normal"
    else:
        state = "disabled"
    button_increase_temp.config(state=state)
    button_decrease_temp.config(state=state)
    button_open_trap.config(state=state)
    button_close_trap.config(state=state)
    button_activate_alarm.config(state=state)
    button_deactivate_alarm.config(state=state)
    
def activerAlarme():
    print("Alarm ON")
    alarmVisuelON()
    alarmSonoreON()

def deactiverAlarme():
    print("Alarm OFF")
    alarmVisuelOFF()
    alarmSonoreOFF()

def OpenDoor():
    global door_open
    if door_open == False:
        moveSteps(0,3,128)
        door_open = True
        label_trap.config(text=f"État de la trappe : Ouvert")
    
def CloseDoor():
    global door_open
    if door_open == True:
        moveSteps(1,3,128)
        door_open = False
        label_trap.config(text=f"État de la trappe : Fermée")

def toggle_test():
    global mode_test
    if mode_test:
        mode_test = False
        check_state(mode_test)
    else:
        mode_test = True
        check_state(mode_test)
    changing_mode()
    
# Cherche la temperature du dht et le montre chaque 3 secondes
# Si test mode est ON, la sa ne marche pas
def check_temp():
    global mode_test
    global temperature
    temperature = float(temp_loop())
    label_temp.config(text=f"Température : {temperature:.2f} °C")
    if mode_test==False:
        root.after(3000, check_temp)
        
def tempUp():
    global temperature
    temperature += 1
    label_temp.config(text=f"Température : {temperature:.2f} °C")
    emergency_test()

def tempDown():
    global temperature
    temperature -= 1
    label_temp.config(text=f"Température : {temperature:.2f} °C")
    emergency_test()

# chercher si la temperature augment de 25 automatique
def emergency_auto():
    global temperature
    global mode_test
    if mode_test == False:
        if temperature > 25.00:
            activerAlarme()
            OpenDoor()
        else:
            deactiverAlarme()
            CloseDoor()
    root.after(1000, emergency_auto)

# chercher si la temperature augment de 25 version test
def emergency_test():
    global temperature
    global mode_test
    if mode_test == True:
        if temperature > 25.00:
            activerAlarme()
            OpenDoor()
        else:
            deactiverAlarme()
            CloseDoor()

root = tk.Tk()
root.geometry('400x450')
root.title("Poste d'Incendie Intelligent")

# Labels
label_system = tk.Label(root, text="Système de Surveillance", font=("Arial", 16, "bold"))
label_system.pack(pady=10)

label_temp = tk.Label(root, text=f"Température : {temperature} °C", font=("Arial", 14))
label_temp.pack()

label_trap = tk.Label(root, text=f"État de la trappe : Fermée", font=("Arial", 12))
label_trap.pack(pady=5)

label_mode_test = tk.Label(root, text=f"Mode Test : Désactivé", font=("Arial", 12), fg="blue")
label_mode_test.pack(pady=5)

# Toggle Test Mode Button
button_toggle_test = tk.Button(root, text="Basculer Mode Test", command=toggle_test)
button_toggle_test.pack(pady=5)

# Temperature Adjustment
label_temp_adjust = tk.Label(root, text="Température :", font=("Arial", 12))
label_temp_adjust.pack(pady=5)

frame_temp_adjust = tk.Frame(root)
frame_temp_adjust.pack(pady=5)

button_increase_temp = tk.Button(frame_temp_adjust, text="+", command=tempUp, width=3, bg="lightgreen")
button_increase_temp.pack(side=tk.LEFT)

button_decrease_temp = tk.Button(frame_temp_adjust, text="-", command=tempDown, width=3, bg="lightcoral")
button_decrease_temp.pack(side=tk.LEFT)

# Trap Control
label_trap_control = tk.Label(root, text="Trappe :", font=("Arial", 12))
label_trap_control.pack(pady=5)

frame_trap_control = tk.Frame(root)
frame_trap_control.pack(pady=5)

button_open_trap = tk.Button(frame_trap_control, text="Ouvrir", command=OpenDoor, width=10, bg="lightgreen")
button_open_trap.pack(side=tk.LEFT)

button_close_trap = tk.Button(frame_trap_control, text="Fermer", command=CloseDoor, width=10, bg="lightcoral")
button_close_trap.pack(side=tk.LEFT)

# Alarm Control
label_alarm = tk.Label(root, text="Alarme :", font=("Arial", 12))
label_alarm.pack(pady=5)

frame_alarm = tk.Frame(root)
frame_alarm.pack(pady=5)

button_activate_alarm = tk.Button(frame_alarm, text="Activer", command=activerAlarme, width=10, bg="lightgreen")
button_activate_alarm.pack(side=tk.LEFT)

button_deactivate_alarm = tk.Button(frame_alarm, text="Arrêter", command=deactiverAlarme, width=10, bg="lightcoral")
button_deactivate_alarm.pack(side=tk.LEFT)

check_temp()
emergency_auto()
check_state(mode_test)
root.mainloop()
