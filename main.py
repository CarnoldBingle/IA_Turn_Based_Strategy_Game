import tkinter as tk
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

def open_stats_window():
    global stats_window_instance
    if stats_window_instance is None or not stats_window_instance.winfo_exists():
        stats_window_instance = tk.Toplevel(root)
        stats_window_instance.title("Stats")
        stats_window_instance.geometry("1000x600")
        stats_window_instance.resizable(False, False)
        label = tk.Label(stats_window_instance, text="Stats Window", font = ("Arial, 16"))
        label.pack(pady=50)
        stats_window_instance.grab_set()
        stats_window_instance.protocol("WM_DELETE_WINDOW", on_closing_window())

def on_closing_stats_window():
    global stats_window_instance
    stats_window_instance.destroy()
    stats_window_instance = None

def open_formations_window():
    global formations_window_instance
    if formations_window_instance is None or not formations_window_instance.winfo_exists():
        formations_window_instance = tk.Toplevel(root)
        formations_window_instance.title("Formations")
        formations_window_instance. geometry("1000x600")
        formations_window_instance.resizable(False,False)
        formations_window_instance.config(bg="green")
        display_formation(formations_window_instance)
        formations_window_instance.grab_set()
        formations_window_instance.protocol("WM_DELETE_WINDOW", on_closing_window())

def display_formation(window):
    """Display the active team formation as ovals and labels."""
    positions = {
        "ST": (450, 50, "red"),
        "LW": (275, 100, "red"),
        "RW": (625, 100, "red"),
        "CM": [(350, 225), (450, 300), (550, 225)],
        "CB": [(350, 425), (550, 425)],
        "GK": (450, 525, "yellow")
    }

    # Display single-position players (like ST, LW, RW, GK)
    for pos, (x, y, color) in positions.items():
        if pos != "CM" and pos != "CB":
            draw_player(window, x, y, color, pos, active_team[pos])

    # Display multiple-position players (like CM, CB)
    for pos, coords in [("CM", positions["CM"]), ("CB", positions["CB"])]:
        for i, (x, y) in enumerate(coords):
            draw_player(window, x, y, "blue" if pos == "CB" else "purple", pos, active_team[pos][i])

def draw_player(window, x, y, color, position, player_name):
    """Draws an oval with a player's name and position."""
    canvas = tk.Canvas(window, width=100, height=50, bg="green", highlightthickness=0)
    canvas.place(x=x, y=y)
    canvas.create_oval(10, 10, 90, 40, fill=color, outline="black")
    canvas.create_text(50, 15, text=position, font=("Arial", 12, "bold"))
    canvas.create_text(50, 35, text=player_name, font=("Arial", 10))

def on_closing_formations_window():
    global formations_window_instance
    formations_window_instance.destroy()
    formations_window_instance = None

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
