import tkinter as tk
import csv

from tkinter import messagebox

root = tk.Tk()

root.title("Main Window")
root.geometry("1000x600")
root.resizable(False, False)
root.config(bg="green")

start_window_instance = None
transfer_window_instance = None
training_plan_window_instance = None
stats_window_instance = None
formations_window_instance = None

# Example of active team data (you can modify this)
active_team = {
    "ST": "Player A",
    "LW": "Player B",
    "RW": "Player C",
    "CM": ["Player D", "Player E"],
    "CB": ["Player F", "Player G"],
    "GK": "Player H"
}

# New formations to choose from
formations_list = ["4-3-3", "4-4-2", "3-5-2", "5-3-2", "3-4-3"]
current_formation = "4-3-3"

formations_window_instance = None

def open_start_window():
    global start_window_instance
    if start_window_instance is None or not start_window_instance.winfo_exists():
        start_window_instance = tk.Toplevel(root)
        start_window_instance.title("Start")
        start_window_instance.geometry("1000x600")
        start_window_instance.resizable(False, False)
        label = tk.Label(start_window_instance, text="Start Window", font=("Arial", 16))
        label.pack(pady=50)
        start_window_instance.grab_set()
        start_window_instance.protocol("WM_DELETE_WINDOW", on_closing_window)

def on_closing_window():
    global start_window_instance
    start_window_instance.destroy()
    start_window_instance = None

def open_transfer_window():
    global transfer_window_instance
    if transfer_window_instance is None or not transfer_window_instance.winfo_exists():  # Check if the window exists
        transfer_window_instance = tk.Toplevel(root)
        transfer_window_instance.title("Transfer")
        transfer_window_instance.geometry("1000x600")
        transfer_window_instance.resizable(False, False)
        label = tk.Label(transfer_window_instance, text="Transfer Window", font=("Arial", 16))
        label.pack(pady=50)
        transfer_window_instance.grab_set()
        transfer_window_instance.protocol("WM_DELETE_WINDOW", on_closing_transfer_window)



def on_closing_transfer_window():
    global transfer_window_instance
    transfer_window_instance.destroy()
    transfer_window_instance = None

def training_plan_window():
    global training_plan_window_instance
    if training_plan_window_instance is None or not training_plan_window_instance.winfo_exists():
        training_plan_window_instance = tk.Toplevel(root)
        training_plan_window_instance.title("Training Plan")
        training_plan_window_instance.geometry("1000x600")
        training_plan_window_instance.resizable(False, False)
        label = tk.Label(training_plan_window_instance, text="Training Plan", font=("Arial", 16))
        label.pack(pady=50)
        training_plan_window_instance.grab_set()
        training_plan_window_instance.protocol("WM_DELETE_WINDOW", on_closing_training_window)#############

def on_closing_training_window():
    global training_plan_window_instance
    training_plan_window_instance.destroy()
    training_plan_window_instance = None


# data_loader.py

def load_players_from_csv():
    players = []
    with open("player.csv", mode='r') as file:
        # Read the header (first line) to get column names
        headers = file.readline().strip().split(',')

        # Read each subsequent line as a player entry
        for line in file:
            values = line.strip().split(',')
            player = {headers[i]: values[i] for i in range(len(headers))}
            players.append(player)

    return players

# main.py


# Load players data from CSV file
players = load_players_from_csv()

# Example to display player data in the console
for player in players:
    print(f"Name: {player['Name']}, Position: {player['Position']}, Goals: {player['Goals']}")




def open_stats_window():
    global stats_window_instance
    if stats_window_instance is None or not stats_window_instance.winfo_exists():
        stats_window_instance = tk.Toplevel(root)
        stats_window_instance.title("Stats")
        stats_window_instance.geometry("1000x600")
        stats_window_instance.resizable(False, False)
        stats_window_instance.config(bg="green")
        stats_window_instance.grab_set()
        stats_window_instance.protocol("WM_DELETE_WINDOW", on_closing_stats_window)

        frame = tk.Frame(stats_window_instance)
        frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Dropdown menu for filtering by position
        selected_position = tk.StringVar(value="All")  # Default to "All" to show all players initially
        positions = ["All"] + list(set(player["Position"] for player in players))  # Unique positions from CSV
        dropdown = tk.OptionMenu(frame, selected_position, *positions)
        dropdown.config(width=10, font=("Arial", 12))
        dropdown.pack(side=tk.TOP, pady=10)

        # Text box for displaying player stats
        text_box = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12), width=60, height=20, bg="green", fg="black")

        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the text box
        scrollbar = tk.Scrollbar(frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_box.config(yscrollcommand=scrollbar.set)

        # Function to filter and display players based on the selected position
        def filter_players():
            # Clear the text box
            text_box.delete("1.0", tk.END)
            # Get the selected position
            position = selected_position.get()
            # Filter players based on position
            filtered_players = [player for player in players if player["Position"] == position or position == "All"]
            # Display filtered players in the text box
            for player in filtered_players:
                text_box.insert(tk.END, f"Name: {player['Name']}, Position: {player['Position']}, "
                                        f"Goals: {player['Goals']}, Assists: {player['Assists']}, "
                                        f"Appearances: {player['Appearances']}\n\n")

        # Update display when a new position is selected
        selected_position.trace("w", lambda *args: filter_players())

        # Initial display of all players
        filter_players()



def on_closing_stats_window():
    global stats_window_instance
    stats_window_instance.destroy()
    stats_window_instance = None

active_formation = "form1"  # Default active formation

def open_formations_window():
    global formations_window_instance
    if formations_window_instance is None or not formations_window_instance.winfo_exists():
        formations_window_instance = tk.Toplevel(root)
        formations_window_instance.title("Formations")
        formations_window_instance.geometry("1000x600")
        formations_window_instance.resizable(False, False)
        formations_window_instance.config(bg="green")
        formations_window_instance.grab_set()
        formations_window_instance.protocol("WM_DELETE_WINDOW", on_closing_formations_window)

        # Create a canvas to draw the formation
        canvas = tk.Canvas(formations_window_instance, width=800, height=500, bg="green")
        canvas.pack(pady=20)

        # Draw the current formation on the canvas
        current_formation(canvas)

        # Create a frame inside formations window for formation buttons
        button_frame = tk.Frame(formations_window_instance)
        button_frame.pack(pady=10)

        button_form1 = tk.Button(button_frame, text="4-3-3", command=lambda: set_formation(form1, canvas))
        button_form1.grid(row=0, column=0)

        button_form2 = tk.Button(button_frame, text="4-2-3-1", command=lambda: set_formation(form2, canvas))
        button_form2.grid(row=0, column=1)

        button_form3 = tk.Button(button_frame, text="4-3-3", command=lambda: set_formation(form3, canvas))
        button_form3.grid(row=0, column=2)

        button_form4 = tk.Button(button_frame, text="4-4-2", command=lambda: set_formation(form4, canvas))
        button_form4.grid(row=0, column=3)




def set_formation(formation_func, canvas):
    global current_formation
    current_formation = formation_func
    current_formation(canvas)  # Redraw the selected formation on the canvas


def on_closing_formations_window():
    global formations_window_instance
    formations_window_instance.destroy()
    formations_window_instance = None

def form1():
    # Buttons to open different windows, including formations
    formations_button = tk.Button(root, text="Formations", command=open_formations_window, font=("Arial", 12))
    formations_button.place(x=50, y=500)

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=50)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="ST", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=275, y=100)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="LW", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=625, y=100)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="RW", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=525)
    canvas.create_oval(10, 10, 90, 40, fill="yellow", outline="black")
    canvas.create_text(50, 25, text="GK", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=550, y=425)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=350, y=425)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=250, y=375)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="LB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=650, y=375)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="RB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=350, y=225)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=550, y=225)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=300)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CDM", font=("Arial", 12, "bold"))

def form2():  # 4-2-3-1 Formation
    # Buttons to open different windows, including formations
    formations_button = tk.Button(root, text="Formations", command=open_formations_window, font=("Arial", 12))
    formations_button.place(x=50, y=500)

    # Forward
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=50)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="ST", font=("Arial", 12, "bold"))

    # Attacking Midfielders
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=275, y=150)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="LAM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=150)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CAM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=625, y=150)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="RAM", font=("Arial", 12, "bold"))

    # Central Midfielders
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=350, y=300)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CDM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=550, y=300)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CDM", font=("Arial", 12, "bold"))

    # Defenders
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=250, y=375)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="LB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=650, y=375)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="RB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=350, y=425)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=550, y=425)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

    # Goalkeeper
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=525)
    canvas.create_oval(10, 10, 90, 40, fill="yellow", outline="black")
    canvas.create_text(50, 25, text="GK", font=("Arial", 12, "bold"))

def form3():  # 4-3-3 Formation
    # Buttons to open different windows, including formations
    formations_button = tk.Button(root, text="Formations", command=open_formations_window, font=("Arial", 12))
    formations_button.place(x=50, y=500)

    # Forwards
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=50)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="ST", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=275, y=100)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="LW", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=625, y=100)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="RW", font=("Arial", 12, "bold"))

    # Midfielders
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=300, y=275)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="LCM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=300)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=600, y=275)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="RCM", font=("Arial", 12, "bold"))

    # Defenders
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=250, y=375)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="LB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=650, y=375)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="RB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=350, y=425)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=550, y=425)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

    # Goalkeeper
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=525)
    canvas.create_oval(10, 10, 90, 40, fill="yellow", outline="black")
    canvas.create_text(50, 25, text="GK", font=("Arial", 12, "bold"))

def form4():  # 4-4-2 Formation
    # Buttons to open different windows, including formations
    formations_button = tk.Button(root, text="Formations", command=open_formations_window, font=("Arial", 12))
    formations_button.place(x=50, y=500)

    # Forwards
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=400, y=50)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="ST", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=500, y=50)
    canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
    canvas.create_text(50, 25, text="ST", font=("Arial", 12, "bold"))

    # Midfielders
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=275, y=200)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="LM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=625, y=200)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="RM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=400, y=250)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CM", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=500, y=250)
    canvas.create_oval(10, 10, 90, 40, fill="purple", outline="black")
    canvas.create_text(50, 25, text="CM", font=("Arial", 12, "bold"))

    # Defenders
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=250, y=375)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="LB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=650, y=375)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="RB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=350, y=425)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=550, y=425)
    canvas.create_oval(10, 10, 90, 40, fill="blue", outline="black")
    canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

    # Goalkeeper
    canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=450, y=525)
    canvas.create_oval(10, 10, 90, 40, fill="yellow", outline="black")
    canvas.create_text(50, 25, text="GK", font=("Arial", 12, "bold"))










start_button = tk.Button(root, text="Start", command=open_start_window, font=("Arial", 12))
start_button.place(x=900, y=550)

transfer_button = tk.Button(root, text="Transfer", command=open_transfer_window, font=("Arial", 12))
transfer_button.place(x=50, y=50)

training_plan_button = tk.Button(root, text="Training plan", command=training_plan_window, font=("Arial", 12))
training_plan_button.place(x=50, y=200)

stats_button = tk.Button(root, text="Stats", command=open_stats_window, font=("Arial", 12))
stats_button.place(x=50, y=350)

formations_button = tk.Button(root, text="Formations", command=open_formations_window, font=("Arial", 12))
formations_button.place(x=50, y=500)

form1()

root.mainloop()
