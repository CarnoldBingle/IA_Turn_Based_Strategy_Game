import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

# Global variables
csv_file = "roster"
data = pd.read_csv(csv_file)
filtered_data = None

# Functions for UI logic
def create_left_frame(parent):
    """Create the left frame for team and player selection."""
    global team_var, player_listbox

    left_frame = tk.Frame(parent, width=400, relief="sunken", borderwidth=2)
    left_frame.pack(side="left", fill="both", expand=True)

    # Team Dropdown
    team_var = tk.StringVar(value="Select Team")
    team_dropdown = ttk.Combobox(left_frame, textvariable=team_var, state="readonly")
    team_dropdown.pack(pady=10)
    team_dropdown["values"] = data["Team"].unique().tolist()
    team_dropdown.bind("<<ComboboxSelected>>", filter_by_team)

    # Player Listbox
    player_listbox = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, width=40, height=15)
    player_listbox.pack(pady=10)

    # Transfer Button
    transfer_button = tk.Button(left_frame, text="Transfer Selected Players →", command=transfer_players)
    transfer_button.pack(pady=10)

    return left_frame


def create_right_frame(parent):
    """Create the right frame for team selection and player transfer."""
    global new_team_var, transferred_listbox

    right_frame = tk.Frame(parent, width=400, relief="sunken", borderwidth=2)
    right_frame.pack(side="right", fill="both", expand=True)

    # Team Dropdown
    new_team_var = tk.StringVar(value="Select Team")
    new_team_dropdown = ttk.Combobox(right_frame, textvariable=new_team_var, state="readonly")
    new_team_dropdown.pack(pady=10)
    new_team_dropdown["values"] = data["Team"].unique().tolist()

    # Transferred Player Listbox
    transferred_listbox = tk.Listbox(right_frame, width=40, height=15)
    transferred_listbox.pack(pady=10)

    # Save Changes Button
    save_button = tk.Button(right_frame, text="Save Changes to CSV", command=save_changes)
    save_button.pack(pady=10)

    return right_frame


def filter_by_team(event=None):
    """Filter players based on the selected team."""
    global filtered_data

    selected_team = team_var.get()
    if selected_team != "Select Team":
        filtered_data = data[data["Team"] == selected_team]
        player_listbox.delete(0, tk.END)  # Clear existing players
        for player in filtered_data["Player Name"]:
            player_listbox.insert(tk.END, player)


def transfer_players():
    """Transfer selected players to the new team."""
    selected_indices = player_listbox.curselection()
    selected_players = [player_listbox.get(i) for i in selected_indices]

    if not selected_players or new_team_var.get() == "Select Team":
        return  # Do nothing if no players are selected or team not selected

    # Add players to the right listbox
    for player in selected_players:
        transferred_listbox.insert(tk.END, f"{player} → {new_team_var.get()}")

    # Update the dataframe to reflect transfers
    for player in selected_players:
        data.loc[data["Player Name"] == player, "Team"] = new_team_var.get()

    # Remove transferred players from the left listbox
    for i in reversed(selected_indices):
        player_listbox.delete(i)


def save_changes():
    """Save the updated roster back to the CSV file."""
    try:
        data.to_csv(csv_file, index=False)
        messagebox.showinfo("Success", f"Changes saved to {csv_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save changes: {str(e)}")



root = tk.Tk()
root.title("Team Player Manager")
root.geometry("800x400")  # Set the window size

# Create UI frames
create_left_frame(root)
create_right_frame(root)

root.mainloop()