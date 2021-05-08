'''
Description: Try to catch the Moviemon you’ve just flushed out!
11
Python-Django Training - Rush 00 Moviemon
• URL: ’/battle/<moviemon_id>’. <moviemon_id> will be replaced by the Moviemon’s
ID you’re about to battle.
• Screen: Displays the poster and the strength of the Moviemon, the number of
movieballs in stock, the stength of the player and the winning rate (see below).
If caught, you must also display a catch phrase (no pun intended) like "You caught
it" to mark the event.
If you failed, you must also display a phrase like "You missed !".
As long as the Moviemon is not caught, the screen must also display ’A - Launch
movieball’.
Anyway, you must always show that the ’button’ B takes the player back to the
Worldmap.
• Controls :
◦ A : Throw a movieball
If the player has none, the action is effectless (you can display a little taunt
fromm the ennemy on the screen).
Otherwise, the number of movieballs is decreases by 1 and a luck roll calculates
whether or not the Moviemon is caught.
Luck rate C is calculated as follows:
C = 50 - (monster strength * 10) + (player strength * 5)
Et 1 <= C <= 90
For instance:
For a monster with a 8.2 strength and a strength 2 player:
C = 50 - 82 + 10 = -22
This monster has 1% chance to get caught.
For a monster with a 5 strength, and a strength 8 player:
C = 50 - 50 + 40 = 40
This monster has 40% chance to get caught.
For a monster with a 2 strength, and a strength 14 player:
C = 50 - 20 + 70 = 100
This monster has 90% chance to get caught.
If successful, the Moviemon is caught and stocked in the MovieDex. The A
button becomes inactive.
12
Python-Django Training - Rush 00 Moviemon
In case of a failure, the player can throw as many movie balls they have in
their possession.
◦ B: Returns to Worldmap
'''

def index(request):
    pass

def moviemon(request):
    pass
from django.shortcuts import render

# Create your views here.
