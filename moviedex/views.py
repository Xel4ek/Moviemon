'''
Moviedex
• Description: List of newly caught Moviemons. You must be able to select a film to
access its informations.
• URL: ’/moviedex’
• Screen: All the caught Moviemons posters must show on screen. The selected poster
must be clearly set appart by a graphic element like a blue frame.
You will also add ’A - More information’ and ’select - Back’.
• Controls:
◦ Directions: Directions allow you to select a different film. You must use at
least 2 directions: left and right or top and bottom.
◦ select: Link to the Worldmap page.
◦ A: Link to the Detail page of the selected Moviemon.
As a default setting, when reaching the page, the film selected will
be the first in the list.
Detail
• Description: Detail of a moviemon.
• URL: ’/moviedex/<moviemon>’ <moviemon> must be replaced with the Moviemon
ID.
• Screen: Must display the name, poster, director, year, rating, synopsis and actors
of the Moviemon as well as ’B-Back’.
• Controls:
◦ B Button: Link to the Moviedex page
'''
from django.shortcuts import render

# Create your views here.

def index(request):
    pass


def moviemon(request):
    pass