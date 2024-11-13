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

        # Create a canvas to draw the formation and limit its height, with temporary bg color for debugging
        canvas = tk.Canvas(formations_window_instance, width=800, height=300, bg="lightblue")
        canvas.pack(pady=(20, 10))  # Add padding to ensure space for the button frame

        # Display the default formation on the canvas

        #print(current_formation, type(current_formation))
        #current_formation()

        # Create a frame for the buttons below the canvas, with a temporary color for debugging
        button_frame = tk.Frame(formations_window_instance, bg="yellow")
        button_frame.pack(pady=10)  # Padding between the canvas and buttons

        # Buttons to select formations, visible with padding
        button_form1 = tk.Button(button_frame, text="4-3-3", command=lambda: set_formation(form1, canvas))
        button_form1.grid(row=0, column=0, padx=5)

        button_form2 = tk.Button(button_frame, text="4-2-3-1", command=lambda: set_formation(form2, canvas))
        button_form2.grid(row=0, column=1, padx=5)

        button_form3 = tk.Button(button_frame, text="4-3-3 Variant", command=lambda: set_formation(form3, canvas))
        button_form3.grid(row=0, column=2, padx=5)

        button_form4 = tk.Button(button_frame, text="4-4-2", command=lambda: set_formation(form4,canvas))
        button_form4.grid(row=0, column=3, padx=5)

formations_window_instance = None

# Define each formation function to draw it on the canvas
def form1(canvas):
    # Clear canvas for new formation
    canvas.delete("all")
    # 4-3-3 Formation
    canvas.create_oval(400, 50, 450, 100, fill="red")
    canvas.create_text(425, 75, text="ST", font=("Arial", 12, "bold"))

    canvas.create_oval(300, 100, 350, 150, fill="red")
    canvas.create_text(325, 125, text="LW", font=("Arial", 12, "bold"))

    canvas.create_oval(500, 100, 550, 150, fill="red")
    canvas.create_text(525, 125, text="RW", font=("Arial", 12, "bold"))

    canvas.create_oval(375, 225, 425, 275, fill="purple")
    canvas.create_text(400, 250, text="LCM", font=("Arial", 12, "bold"))

    canvas.create_oval(450, 225, 500, 275, fill="purple")
    canvas.create_text(475, 250, text="RCM", font=("Arial", 12, "bold"))

    canvas.create_oval(415, 300, 465, 350, fill="purple")
    canvas.create_text(440, 325, text="CDM", font=("Arial", 12, "bold"))

    canvas.create_oval(275, 375, 325, 425, fill="blue")
    canvas.create_text(300, 400, text="LB", font=("Arial", 12, "bold"))

    canvas.create_oval(525, 375, 575, 425, fill="blue")
    canvas.create_text(550, 400, text="RB", font=("Arial", 12, "bold"))

    canvas.create_oval(350, 400, 400, 450, fill="blue")
    canvas.create_text(375, 425, text="CB", font=("Arial", 12, "bold"))

    canvas.create_oval(475, 400, 525, 450, fill="blue")
    canvas.create_text(500, 425, text="CB", font=("Arial", 12, "bold"))

    canvas.create_oval(400, 475, 450, 525, fill="yellow")
    canvas.create_text(425, 500, text="GK", font=("Arial", 12, "bold"))

def form2(canvas):
    # Clear canvas for new formation
    canvas.delete("all")
    # 4-2-3-1 Formation
    canvas.create_oval(400, 50, 450, 100, fill="red")
    canvas.create_text(425, 75, text="ST", font=("Arial", 12, "bold"))

    canvas.create_oval(300, 150, 350, 200, fill="purple")
    canvas.create_text(325, 175, text="LAM", font=("Arial", 12, "bold"))

    canvas.create_oval(450, 150, 500, 200, fill="purple")
    canvas.create_text(475, 175, text="CAM", font=("Arial", 12, "bold"))

    canvas.create_oval(500, 150, 550, 200, fill="purple")
    canvas.create_text(525, 175, text="RAM", font=("Arial", 12, "bold"))

    canvas.create_oval(375, 250, 425, 300, fill="purple")
    canvas.create_text(400, 275, text="CDM", font=("Arial", 12, "bold"))

    canvas.create_oval(450, 250, 500, 300, fill="purple")
    canvas.create_text(475, 275, text="CDM", font=("Arial", 12, "bold"))

    canvas.create_oval(275, 350, 325, 400, fill="blue")
    canvas.create_text(300, 375, text="LB", font=("Arial", 12, "bold"))

    canvas.create_oval(525, 350, 575, 400, fill="blue")
    canvas.create_text(550, 375, text="RB", font=("Arial", 12, "bold"))

    canvas.create_oval(350, 375, 400, 425, fill="blue")
    canvas.create_text(375, 400, text="CB", font=("Arial", 12, "bold"))

    canvas.create_oval(475, 375, 525, 425, fill="blue")
    canvas.create_text(500, 400, text="CB", font=("Arial", 12, "bold"))

    canvas.create_oval(400, 450, 450, 500, fill="yellow")
    canvas.create_text(425, 475, text="GK", font=("Arial", 12, "bold"))

def form3(canvas):
    # Clear canvas for new formation
    canvas.delete("all")
    # 4-3-3 Variant Formation
    canvas.create_oval(400, 50, 450, 100, fill="red")
    canvas.create_text(425, 75, text="ST", font=("Arial", 12, "bold"))

    canvas.create_oval(300, 125, 350, 175, fill="red")
    canvas.create_text(325, 150, text="LW", font=("Arial", 12, "bold"))

    canvas.create_oval(500, 125, 550, 175, fill="red")
    canvas.create_text(525, 150, text="RW", font=("Arial", 12, "bold"))

    canvas.create_oval(350, 225, 400, 275, fill="purple")
    canvas.create_text(375, 250, text="LCM", font=("Arial", 12, "bold"))

    canvas.create_oval(450, 225, 500, 275, fill="purple")
    canvas.create_text(475, 250, text="RCM", font=("Arial", 12, "bold"))

    canvas.create_oval(400, 300, 450, 350, fill="purple")
    canvas.create_text(425, 325, text="CDM", font=("Arial", 12, "bold"))

    canvas.create_oval(275, 375, 325, 425, fill="blue")
    canvas.create_text(300, 400, text="LB", font=("Arial", 12, "bold"))

    canvas.create_oval(525, 375, 575, 425, fill="blue")
    canvas.create_text(550, 400, text="RB", font=("Arial", 12, "bold"))

    canvas.create_oval(350, 400, 400, 450, fill="blue")
    canvas.create_text(375, 425, text="CB", font=("Arial", 12, "bold"))

    canvas.create_oval(475, 400, 525, 450, fill="blue")
    canvas.create_text(500, 425, text="CB", font=("Arial", 12, "bold"))

    canvas.create_oval(400, 475, 450, 525, fill="yellow")
    canvas.create_text(425, 500, text="GK", font=("Arial", 12, "bold"))

def form4(canvas):
    # Clear canvas for new formation
    canvas.delete("all")
    # 4-4-2 Formation
    canvas.create_oval(375, 50, 425, 100, fill="red")
    canvas.create_text(400, 75, text="ST", font=("Arial", 12, "bold"))

    canvas.create_oval(475, 50, 525, 100, fill="red")
    canvas.create_text(500, 75, text="ST", font=("Arial", 12, "bold"))

    canvas.create_oval(300, 150, 350, 200, fill="purple")
    canvas.create_text(325, 175, text="LM", font=("Arial", 12, "bold"))

    canvas.create_oval(500, 150, 550, 200, fill="purple")
    canvas.create_text(525, 175, text="RM", font=("Arial", 12, "bold"))

    canvas.create_oval(375, 200, 425, 250, fill="purple")
    canvas.create_text(400, 225, text="LCM", font=("Arial", 12, "bold"))

    canvas.create_oval(450, 200, 500, 250, fill="purple")
    canvas.create_text(475, 225, text="RCM", font=("Arial", 12, "bold"))

    canvas.create_oval(275, 350, 325, 400, fill="blue")
    canvas.create_text(300, 375, text="LB", font=("Arial", 12, "bold"))

    canvas.create


def set_formation(formation_func, canvas):
    print("line 217----- ", canvas, set_formation)
    global current_formation
    current_formation = formation_func
    canvas.delete("all")  # Clear the canvas before drawing the new formation
    current_formation(canvas)  # Call the selected formation function to update the canvas




def on_closing_formations_window():
    global formations_window_instance
    formations_window_instance.destroy()
    formations_window_instance = None









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


root.mainloop()
