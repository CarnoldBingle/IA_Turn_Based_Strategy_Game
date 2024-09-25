"""""// Start
of
the
process
START

// Main
GUI
displayed
DISPLAY
Main_GUI

// Check
which
button is pressed
IF
buttonPressed
THEN
// Check if the
Transfer
button is pressed
IF
transferButtonPressed
THEN
// Open
Transfer
GUI
DISPLAY
Transfer_GUI

// Transfer
GUI
logic
IF
playerClickedInTransferMarket
THEN
// Open
Transfer
Market
Player
Options
Popup
DISPLAY
TransferMarketPlayerOptionsPopup

// Check
which
option is selected
IF
buyOptionSelected
THEN
// Open
Negotiation
GUI
for Buying
    DISPLAY
    Negotiation_GUI_for_Buying

// Negotiate
Price
NEGOTIATE
price

// Check if an
agreement is reached
IF
agreementReached
THEN
// Complete
the
purchase
COMPLETE
Purchase
ELSE
// Cancel
the
purchase
CANCEL
Purchase
ENDIF
ELSEIF
loanOptionSelected
THEN
// Open
Negotiation
GUI
for Loaning
    DISPLAY
    Negotiation_GUI_for_Loaning

// Negotiate
Loan
Terms
NEGOTIATE
loanTerms

// Check if an
agreement is reached
IF
agreementReached
THEN
// Complete
the
loan
COMPLETE
Loan
ELSE
// Cancel
the
loan
CANCEL
Loan
ENDIF
ELSEIF
statsOptionSelected
THEN
// Open
Stats
GUI
DISPLAY
Stats_GUI
ELSEIF
cancelOptionSelected
THEN
// Close
Popup
CLOSE
Popup
ENDIF
ELSEIF
playerClickedInSquad
THEN
// Open
Squad
Player
Options
Popup
DISPLAY
SquadPlayerOptionsPopup

// Check
which
option is selected
IF
sellOptionSelected
THEN
// Mark
Player as Available
for Sale
    MARK
    Player as Available_for_Sale
ELSEIF
loanOptionSelected
THEN
// Mark
Player as Available
for Loan
    MARK
    Player as Available_for_Loan
ELSEIF
cancelOptionSelected
THEN
// Close
Popup
CLOSE
Popup
ENDIF
ENDIF
ELSEIF
formationsButtonPressed
THEN
// Open
Formations
GUI
DISPLAY
Formations_GUI

// Formations
GUI
logic
DISPLAY
Current_Formation
SCROLL
Down?
IF
yes
THEN
DISPLAY
List_of_Formations
ENDIF

// Check if a
formation is selected
IF
formationSelected
THEN
// Replace
current
formation
with selected formation
REPLACE
Current_Formation
WITH
Selected_Formation
ENDIF

// Check if Edit
Team
button is pressed
IF
editTeamButtonPressed
THEN
// Open
Edit
Team
GUI
DISPLAY
Edit_Team_GUI

// Edit
Team
GUI
logic
PLAYER_POSITION
Selected?
IF
yes
THEN
// Open
Player
Selection
Popup
DISPLAY
Player_Selection_Popup
DISPLAY
List_of_Players

// Check if a
player is selected
IF
playerSelected
THEN
// Change
player in position
CHANGE
Player_in_Position
ELSE
// Cancel
CANCEL
CLOSE
Popup
ENDIF

// Check if changes
should
be
saved
SAVE
Changes?
IF
yes
THEN
// Save
formation
SAVE
Formation
ENDIF
ENDIF
ENDIF
ELSEIF
statsButtonPressed
THEN
// Open
Stats
GUI
DISPLAY
Stats_GUI

// Stats
GUI
logic
IF
viewStats
THEN
DISPLAY
Player_Stats
ELSEIF
backButtonPressed
THEN
DISPLAY
Main_GUI
ENDIF
ELSEIF
trainingPlansButtonPressed
THEN
// Open
Training
Plans
GUI
DISPLAY
Training_Plans_GUI

// Training
Plans
GUI
logic
IF
viewCurrentPlans
THEN
DISPLAY
Current_Training_Plans
ELSEIF
createNewPlan
THEN
DISPLAY
New_Training_Plan_GUI
INPUT
Training_Plan_Details
SAVE
Training_Plan
ELSEIF
backButtonPressed
THEN
DISPLAY
Main_GUI
ENDIF
ELSEIF
startButtonPressed
THEN
// Open
Start
GUI
DISPLAY
Start_GUI

// Start
GUI
logic
IF
startNewSeason
THEN
INITIALIZE
New_Season
ELSEIF
loadSavedGame
THEN
LOAD
Saved_Game
ELSEIF
backButtonPressed
THEN
DISPLAY
Main_GUI
ENDIF
ELSE
// Handle
other
buttons
HANDLE
Other_Buttons
ENDIF
ENDIF

// End
of
the
process
END"""


