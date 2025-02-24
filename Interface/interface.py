import tkinter as tk

root = tk.Tk()
root.geometry('400x500')
root.title("Poste d'Incendie Intelligent")

# Labels
label_system = tk.Label(root, text="Système de Surveillance", font=("Arial", 16, "bold"))
label_system.pack(pady=10)

label_temp = tk.Label(root, text=f"Température : °C", font=("Arial", 14))
label_temp.pack()

label_trap = tk.Label(root, text=f"État de la trappe : ", font=("Arial", 12))
label_trap.pack(pady=5)

label_mode_test = tk.Label(root, text="Mode Test : Désactivé", font=("Arial", 12), fg="blue")
label_mode_test.pack(pady=5)

# Toggle Test Mode Button
button_toggle_test = tk.Button(root, text="Basculer Mode Test")
button_toggle_test.pack(pady=5)

# Temperature Adjustment
label_temp_adjust = tk.Label(root, text="Température :", font=("Arial", 12))
label_temp_adjust.pack(pady=5)

frame_temp_adjust = tk.Frame(root)
frame_temp_adjust.pack(pady=5)

button_increase_temp = tk.Button(frame_temp_adjust, text="+", width=3, bg="lightgreen")
button_increase_temp.pack(side=tk.LEFT)

button_decrease_temp = tk.Button(frame_temp_adjust, text="-", width=3, bg="lightcoral")
button_decrease_temp.pack(side=tk.LEFT)

# Trap Control
label_trap_control = tk.Label(root, text="Trappe :", font=("Arial", 12))
label_trap_control.pack(pady=5)

frame_trap_control = tk.Frame(root)
frame_trap_control.pack(pady=5)

button_open_trap = tk.Button(frame_trap_control, text="Ouvrir", width=10, bg="lightgreen")
button_open_trap.pack(side=tk.LEFT)

button_close_trap = tk.Button(frame_trap_control, text="Fermer", width=10, bg="lightcoral")
button_close_trap.pack(side=tk.LEFT)

# Alarm Control
label_alarm = tk.Label(root, text="Alarme :", font=("Arial", 12))
label_alarm.pack(pady=5)

frame_alarm = tk.Frame(root)
frame_alarm.pack(pady=5)

button_activate_alarm = tk.Button(frame_alarm, text="Activer", width=10, bg="lightgreen")
button_activate_alarm.pack(side=tk.LEFT)

button_deactivate_alarm = tk.Button(frame_alarm, text="Arrêter", width=10, bg="lightcoral")
button_deactivate_alarm.pack(side=tk.LEFT)


root.mainloop()

