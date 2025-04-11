import tkinter as tk

import random
import time

# Create the main window
root = tk.Tk()
root.title("Five Buttons Example")
root.geometry("300x250")  # Set window size (optional)

# Initialize a counter
counter = 0
#when the imgae is selected
teamd = ""



#when the imgae is selected
def button1_action():
    global teamd
    teamd = "team1"
    print(teamd)

def button2_action():
    print("Button 2 clicked!")

def button3_action():
    print("Button 3 clicked!")

def button4_action():
    print("Button 4 clicked!")

def increment_counter():
    global counter
    counter += 1
    counter_label.config(text=f"Counter: {counter}")

def gameplay():
    if  teamd == "team1":
        team_stats = [.1, .2, .3, -.5, -.4]
    for i in range (0,90):
        team_stats = [.1, .2, .3, -.5, -.4]
        global counter
        global counter_label
        time.sleep(.1)
        counter = i
        counter_label.config(text=f"Counter: {counter}")

        for j in range (len(team_stats)):
            ran_flt = random.uniform(.001,1)#might be neg
            team_stats[j] = team_stats[j]* ran_flt
            result = sum(team_stats)

            print(result, "  ", i)
    result = sum(team_stats)
    print(result,"  ", i)





# Create four buttons
button1 = tk.Button(root, text="Button 1", command=button1_action)
button2 = tk.Button(root, text="Button 2", command=gameplay)
button3 = tk.Button(root, text="Button 3", command=button3_action)
button4 = tk.Button(root, text="Button 4", command=button4_action)

# Create the counter label and button
counter_label = tk.Label(root, text="Counter: 0", font=("Arial", 14))
counter_button = tk.Button(root, text="Increment Counter", command=increment_counter)

# Arrange buttons in the window
button1.pack(pady=5)  # Add spacing between buttons
button2.pack(pady=5)
button3.pack(pady=5)
button4.pack(pady=5)
counter_label.pack(pady=5)
counter_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
