'''
Option
• Description: Game’s options.
• URL: ’/options’
• Screen: Displays the game’s options: ’A - Save’, ’B - Quit’ as well as ’start - cancel’
• Controls:
◦ Start button: Link to the Worldmap page.
◦ A button: Link to the Save page.
◦ B button: Link to the TitleScreen page.
Save
• Description: Allows to save an ongoing game in either one of the three available
slots.
• URL: /options/save_game
• Screen: must display 3 slots: ’Slot A’, ’Slot B’ and ’Slot C’.
A selected slot must be marked with a specific graphic element, like an arrow preceding its name.
If a slot is empty, it must be followed by ’Free’. Otherwise, it must be followed by
the numbers of Moviemons caught.
For instance: ’Slot A: 2/15’ means this save file contains a game in which 2
Moviemons out of 15 have been caught.
The screen must also display ’A - Save’ and ’B - Cancel’.
• Controls:
◦ Directions: Directions ’top’ and ’bottom’ are used to select a slot.
◦ A: Copies the file containing the current state of the game in another file that
must be stocked in the folder ’saved_game’ of your project.
The file name must be ’slot<n>_<score>.mmg’. <n> will be replaced by the
slot’s name ’a’, ’b’ or ’c’ and <score> will be replaced by the game’s score.
For instance: slotb_1_15.mmg. (Please, don’t try to put a slash in a file’s
name).
◦ B: Link to the Option page
14
Python-Django Training - Rush 00 Moviemon
Load
• Description: Allows to load a saved game in either one of the three slots.
• URL: /options/load_game
• Screen: must display three slots: ’Slot A’, ’Slot B’ and ’Slot C’.
A selected slot must be marked with a specific graphic element, like an arrow preceding its name.
If a slot is empty, it must be followed by ’Free’. Otherwise, it must be followed by
the numbers of Moviemons caught.
For instance: ’Slot A: 2/15’ means this save file contains a game in which 2
Moviemons out of 15 have been caught.
The screen must also display ’A - Save’ and ’B - Cancel’.
Once the game is loaded,’A - Load’ must be replaced by ’A - start game’.
• Directions: Directions ’top’ and ’bottom’ are used to select a slot.
• A:
If no game is loaded: Copy the content of the file matching the selected slot in the
file used to stock the current state of the game.
If a game was just loaded, the ’button’ is used as a link to the Worldmap page.
Obviously, trying to load a ’Free’ slot mustn’t have any effect.
• B: Link to the TitleScreen page.

'''
from django.shortcuts import render

# Create your views here.
def index(request):
    pass
def save_game(request):
    pass
def load_game(request):
    pass