import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

class TeamPlayerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Team Player Manager")
        self.root.geometry("800x400")
        self.root.config(bg="green")

        # Load CSV data
        self.csv_file = "player.csv"
        self.data = self.load_csv_data()

        # Filtered data for the left listbox
        self.filtered_data = None

        # Left Frame (Team Selector)
        self.left_frame = tk.Frame(self.root, width=400, relief="sunken", borderwidth=2, bg="green")
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Right Frame (Transfer Window)
        self.right_frame = tk.Frame(self.root, width=400, relief="sunken", borderwidth=2, bg="green")
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.create_left_frame()
        self.create_right_frame()

    def load_csv_data(self):
        """Load player data from the CSV file."""
        if not os.path.exists(self.csv_file):
            # If CSV doesn't exist, create a default DataFrame
            data = pd.DataFrame(columns=["Name", "Team"])
            data.to_csv(self.csv_file, index=False)
        else:
            # Read data from the existing file
            data = pd.read_csv(self.csv_file)
            if "Name" not in data.columns or "Team" not in data.columns:
                messagebox.showerror("Error", "CSV file is missing required columns!")
                data = pd.DataFrame(columns=["Name", "Team"])
        return data

    def create_left_frame(self):
        """Create the left frame for team and player selection."""
        tk.Label(self.left_frame, text="Select Your Team", bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

        # Team Dropdown
        self.team_var = tk.StringVar(value="Select Team")
        self.team_dropdown = ttk.Combobox(self.left_frame, textvariable=self.team_var, state="readonly")
        self.team_dropdown.pack(pady=10)
        self.update_team_dropdown(self.team_dropdown)

        # Bind dropdown selection to filter players
        self.team_dropdown.bind("<<ComboboxSelected>>", self.filter_by_team)

        # Player Listbox
        self.player_listbox = tk.Listbox(self.left_frame, selectmode=tk.MULTIPLE, width=40, height=15)
        self.player_listbox.pack(pady=10)

        # Transfer Button
        transfer_button = tk.Button(self.left_frame, text="Transfer Selected Players →",
                                     command=self.transfer_players, font=("Arial", 10))
        transfer_button.pack(pady=10)

    def create_right_frame(self):
        """Create the right frame for team selection and player transfer."""
        tk.Label(self.right_frame, text="Transfer Players to Team", bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

        # Team Dropdown
        self.new_team_var = tk.StringVar(value="Select Team")
        self.new_team_dropdown = ttk.Combobox(self.right_frame, textvariable=self.new_team_var, state="readonly")
        self.new_team_dropdown.pack(pady=10)
        self.update_team_dropdown(self.new_team_dropdown)

        # Transferred Player Listbox
        self.transferred_listbox = tk.Listbox(self.right_frame, width=40, height=15)
        self.transferred_listbox.pack(pady=10)

        # Save Changes Button
        save_button = tk.Button(self.right_frame, text="Save Changes to CSV",
                                 command=self.save_changes, font=("Arial", 10))
        save_button.pack(pady=10)

    def update_team_dropdown(self, dropdown):
        """Update team dropdown with unique teams."""
        teams = self.data["Team"].dropna().unique().tolist()
        dropdown["values"] = teams

    def filter_by_team(self, event=None):
        """Filter players based on the selected team."""
        selected_team = self.team_var.get()
        self.player_listbox.delete(0, tk.END)  # Clear existing players
        if selected_team and selected_team != "Select Team":
            self.filtered_data = self.data[self.data["Team"] == selected_team]
            for player in self.filtered_data["Player Name"]:
                self.player_listbox.insert(tk.END, player)

    def transfer_players(self):
        """Transfer selected players to the new team."""
        selected_indices = self.player_listbox.curselection()
        selected_players = [self.player_listbox.get(i) for i in selected_indices]
        new_team = self.new_team_var.get()

        if not selected_players:
            messagebox.showerror("Error", "No players selected for transfer!")
            return
        if new_team == "Select Team":
            messagebox.showerror("Error", "No destination team selected!")
            return

        # Add players to the transferred list and update the DataFrame
        for player in selected_players:
            self.transferred_listbox.insert(tk.END, f"{player} → {new_team}")
            self.data.loc[self.data["Player Name"] == player, "Team"] = new_team

        # Remove transferred players from the listbox
        for i in reversed(selected_indices):
            self.player_listbox.delete(i)

        # Update dropdown values dynamically
        self.update_team_dropdown(self.team_dropdown)
        self.update_team_dropdown(self.new_team_dropdown)

    def save_changes(self):
        """Save the updated roster back to the CSV file."""
        try:
            self.data.to_csv(self.csv_file, index=False)
            messagebox.showinfo("Success", f"Changes saved to {self.csv_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save changes: {str(e)}")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = TeamPlayerManager(root)
    root.mainloop()
