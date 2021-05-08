'''
Description: a world map, where the character moves, grabs movieballs and hunts
Moviemons.
• Screen: A grid the size defined in the settings. A representation of the player (image, character...) must stand on the square matching their current position. It
must be clearly visible.
The screen must also display:
◦ The number of movieballs.
◦ A message when a movieball is found.
◦ A message when a Moviemon flushed out, as well as an indication of the button
to push to start the catching process.]
• Url : ’/worldmap’
• Controls:
◦ Directions: Each direction must move the character one case in the same
direction. The player must not be able to exit the map.
Each move gives a chance to flush out a Moviemon or grab a movieball.
If a Moviemon is flushed out, it is randomly picked among the Moviemons that
have not yet been caught.
◦ A: Only if a Moviemon is flushed out: Link to Battle page of the battle against
this Moviemon.
◦ start: Link to the Option page.
◦ select: Link to the Moviedex page.
Refeshing this page must not change the player position on the map.
'''
from django.shortcuts import render

# Create your views here.
def index(request):
    pass