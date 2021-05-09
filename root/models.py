import logging
import pickle
import random

from django.db import models

# Create your models here.
from . import db , movies

'''
• ’load’: Load the game data passed in parameters in the class instance. Returns the
current instance.
• ’dump’: Returns the game’s data.
• ’get_random_movie’: Returns a random Moviemon among the Moviemons not yet
captured.
• ’load_default_settings’: Loads the game data in the class instance from the settings. Requests and stocks all the Moviemons details on IMDB. Returns the current
intance.
• ’get_strength’: Returns the player’s strength.
• ’get_movie’: Returns a Python dictionary containing all the det'''


class Supplier:
    __settings = db.db.get('settings')

    remote_api = movies.get_movies_list()
    remote_api1 = [
        {"Title": "Monster", "Year": "2003", "Rated": "R",
         "Released": "30 Jan 2004", "Runtime": "109 min",
         "Genre": "Biography, Crime, Drama, Thriller",
         "Director": "Patty Jenkins", "Writer": "Patty Jenkins",
         "Actors": "Charlize Theron, Christina Ricci, Bruce Dern, Lee Tergesen",
         "Plot": "Based on the life of Aileen Wuornos, a Daytona Beach prostitute who became a serial killer.",
         "Language": "English", "Country": "USA, Germany",
         "Awards": "Won 1 Oscar. Another 29 wins & 26 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BMTI4NzI5NzEwNl5BMl5BanBnXkFtZTcwNjc1NjQyMQ@@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "7.3/10"},
                     {"Source": "Rotten Tomatoes", "Value": "81%"},
                     {"Source": "Metacritic", "Value": "74/100"}],
         "Metascore": "74", "imdbRating": "7.3", "imdbVotes": "138,228",
         "imdbID": "tt0340855", "Type": "movie", "DVD": "16 Apr 2015",
         "BoxOffice": "$34,469,210",
         "Production": "K/W Productions, MDP Worldwide, Denver and Delilah Productions, DEJ Productions, Zodiac Productions Inc.",
         "Website": "N/A", "Response": "True"},
        {"Title": "Dark", "Year": "2017–2020", "Rated": "TV-MA",
         "Released": "01 Dec 2017", "Runtime": "60 min",
         "Genre": "Crime, Drama, Mystery, Sci-Fi, Thriller", "Director": "N/A",
         "Writer": "Baran bo Odar, Jantje Friese",
         "Actors": "Louis Hofmann, Karoline Eichhorn, Lisa Vicari, Maja Schöne",
         "Plot": "A family saga with a supernatural twist, set in a German town, where the disappearance of two young children exposes the relationships among four families.",
         "Language": "German", "Country": "Germany, USA",
         "Awards": "6 wins & 20 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BOTk2NzUyOTctZDdlMS00MDJlLTgzNTEtNzQzYjFhNjA0YjBjXkEyXkFqcGdeQXVyMjg1NDcxNDE@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "8.8/10"}],
         "Metascore": "N/A", "imdbRating": "8.8", "imdbVotes": "294,486",
         "imdbID": "tt5753856", "Type": "series", "totalSeasons": "3",
         "Response": "True"},
        {"Title": "The Light Between Oceans", "Year": "2016", "Rated": "PG-13",
         "Released": "02 Sep 2016", "Runtime": "133 min",
         "Genre": "Drama, Romance", "Director": "Derek Cianfrance",
         "Writer": "Derek Cianfrance (written for the screen by), M.L. Stedman (novel)",
         "Actors": "Michael Fassbender, Alicia Vikander, Rachel Weisz, Florence Clery",
         "Plot": "A lighthouse keeper and his wife living off the coast of Western Australia raise a baby they rescue from a drifting rowing boat.",
         "Language": "English",
         "Country": "UK, New Zealand, USA, India, Australia",
         "Awards": "1 win & 16 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BNTI1NzQzMjgxOF5BMl5BanBnXkFtZTgwOTY1OTY2OTE@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "7.2/10"},
                     {"Source": "Rotten Tomatoes", "Value": "61%"},
                     {"Source": "Metacritic", "Value": "60/100"}],
         "Metascore": "60", "imdbRating": "7.2", "imdbVotes": "53,065",
         "imdbID": "tt2547584", "Type": "movie", "DVD": "24 Jan 2017",
         "BoxOffice": "$12,545,979",
         "Production": "Heyday Films, Participant Media", "Website": "N/A",
         "Response": "True"},
        {"Title": "Twilight", "Year": "2008", "Rated": "PG-13",
         "Released": "21 Nov 2008", "Runtime": "122 min",
         "Genre": "Drama, Fantasy, Romance", "Director": "Catherine Hardwicke",
         "Writer": "Melissa Rosenberg (screenplay), Stephenie Meyer (novel)",
         "Actors": "Kristen Stewart, Sarah Clarke, Matt Bushell, Billy Burke",
         "Plot": "When Bella Swan moves to a small town in the Pacific Northwest, she falls in love with Edward Cullen, a mysterious classmate who reveals himself to be a 108-year-old vampire.",
         "Language": "English", "Country": "USA",
         "Awards": "32 wins & 16 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BMTQ2NzUxMTAxN15BMl5BanBnXkFtZTcwMzEyMTIwMg@@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "5.2/10"},
                     {"Source": "Rotten Tomatoes", "Value": "49%"},
                     {"Source": "Metacritic", "Value": "56/100"}],
         "Metascore": "56", "imdbRating": "5.2", "imdbVotes": "430,933",
         "imdbID": "tt1099212", "Type": "movie", "DVD": "21 Nov 2015",
         "BoxOffice": "$193,962,473", "Production": "Temple Hill",
         "Website": "N/A", "Response": "True"},
        {"Title": "The Ghost Busters", "Year": "1975", "Rated": "N/A",
         "Released": "06 Sep 1975", "Runtime": "30 min",
         "Genre": "Comedy, Family, Fantasy, Sci-Fi", "Director": "N/A",
         "Writer": "Marc Richards",
         "Actors": "Forrest Tucker, Larry Storch, Bob Burns",
         "Plot": "Two guys and their pet gorilla hunt spooks.",
         "Language": "English", "Country": "USA", "Awards": "N/A",
         "Poster": "https://m.media-amazon.com/images/M/MV5BOTYwOTMyNTUtNzAyMS00NjdhLWIxZTAtNDdkZTQ1YWIxNGFjXkEyXkFqcGdeQXVyNjgwNDM1ODU@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "7.4/10"}],
         "Metascore": "N/A", "imdbRating": "7.4", "imdbVotes": "345",
         "imdbID": "tt0072505", "Type": "series", "totalSeasons": "1",
         "Response": "True"},
        {"Title": "Ghost", "Year": "1990", "Rated": "PG-13",
         "Released": "13 Jul 1990", "Runtime": "127 min",
         "Genre": "Drama, Fantasy, Romance, Thriller",
         "Director": "Jerry Zucker", "Writer": "Bruce Joel Rubin",
         "Actors": "Patrick Swayze, Demi Moore, Tony Goldwyn, Stanley Lawrence",
         "Plot": "After a young man is murdered, his spirit stays behind to warn his lover of impending danger, with the help of a reluctant psychic.",
         "Language": "English", "Country": "USA",
         "Awards": "Won 2 Oscars. Another 16 wins & 23 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BMTU0NzQzODUzNl5BMl5BanBnXkFtZTgwMjc5NTYxMTE@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "7.1/10"},
                     {"Source": "Rotten Tomatoes", "Value": "74%"},
                     {"Source": "Metacritic", "Value": "52/100"}],
         "Metascore": "52", "imdbRating": "7.1", "imdbVotes": "199,965",
         "imdbID": "tt0099653", "Type": "movie", "DVD": "01 Aug 2013",
         "BoxOffice": "$217,631,306", "Production": "Paramount Pictures",
         "Website": "N/A", "Response": "True"},
        {"Title": "A Nightmare on Elm Street", "Year": "1984", "Rated": "R",
         "Released": "16 Nov 1984", "Runtime": "91 min", "Genre": "Horror",
         "Director": "Wes Craven", "Writer": "Wes Craven",
         "Actors": "John Saxon, Ronee Blakley, Heather Langenkamp, Amanda Wyss",
         "Plot": "The monstrous spirit of a slain child murderer seeks revenge by invading the dreams of teenagers whose parents were responsible for his untimely death.",
         "Language": "English", "Country": "USA",
         "Awards": "4 wins & 5 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BNzFjZmM1ODgtMDBkMS00NWFlLTg2YmUtZjc3ZTgxMjE1OTI2L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "7.5/10"},
                     {"Source": "Rotten Tomatoes", "Value": "94%"},
                     {"Source": "Metacritic", "Value": "76/100"}],
         "Metascore": "76", "imdbRating": "7.5", "imdbVotes": "209,479",
         "imdbID": "tt0087800", "Type": "movie", "DVD": "24 Jul 2014",
         "BoxOffice": "$25,504,513", "Production": "New Line Cinema",
         "Website": "N/A", "Response": "True"},
        {"Title": "Screamers", "Year": "1995", "Rated": "R",
         "Released": "26 Jan 1996", "Runtime": "108 min",
         "Genre": "Horror, Sci-Fi, Thriller", "Director": "Christian Duguay",
         "Writer": "Philip K. Dick (short story \"Second Variety\"), Dan O'Bannon (screenplay), Miguel Tejada-Flores (screenplay)",
         "Actors": "Peter Weller, Roy Dupuis, Jennifer Rubin, Andrew Lauer",
         "Plot": "A military commander stationed off planet during an interplanetary war travels through the devastated landscape to negotiate a peace treaty, but discovers that the primitive robots they built to kill enemy combatants have gained sentience.",
         "Language": "English", "Country": "Canada", "Awards": "3 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BM2M2ZGM0NDUtODRhNS00MjcxLTg3ZWYtYjkyZDJkYmVjOWYwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "6.4/10"},
                     {"Source": "Rotten Tomatoes", "Value": "29%"}],
         "Metascore": "N/A", "imdbRating": "6.4", "imdbVotes": "25,466",
         "imdbID": "tt0114367", "Type": "movie", "DVD": "16 Apr 2012",
         "BoxOffice": "$5,711,695", "Production": "Triumph Films",
         "Website": "N/A", "Response": "True"},
        {"Title": "The Basilisk", "Year": "1914", "Rated": "N/A",
         "Released": "01 Dec 1914", "Runtime": "28 min",
         "Genre": "Short, Horror", "Director": "Cecil M. Hepworth",
         "Writer": "Cecil M. Hepworth",
         "Actors": "Tom Powers, Alma Taylor, William Felton, Chrissie White",
         "Plot": "A mesmerist, obsessed with putting a beautiful woman under his power, hypnotizes her to try to force her to kill her fiance. His plans are altered with the appearance of a deadly serpent.",
         "Language": "None", "Country": "UK", "Awards": "N/A", "Poster": "N/A",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "3.6/10"}],
         "Metascore": "N/A", "imdbRating": "3.6", "imdbVotes": "5",
         "imdbID": "tt0003660", "Type": "movie", "DVD": "N/A",
         "BoxOffice": "N/A", "Production": "N/A", "Website": "N/A",
         "Response": "True"},
        {"Title": "The Shining", "Year": "1980", "Rated": "R",
         "Released": "13 Jun 1980", "Runtime": "146 min",
         "Genre": "Drama, Horror", "Director": "Stanley Kubrick",
         "Writer": "Stephen King (based upon the novel by), Stanley Kubrick (screenplay by), Diane Johnson (screenplay by)",
         "Actors": "Jack Nicholson, Shelley Duvall, Danny Lloyd, Scatman Crothers",
         "Plot": "A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.",
         "Language": "English", "Country": "UK, USA",
         "Awards": "4 wins & 8 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "8.4/10"},
                     {"Source": "Rotten Tomatoes", "Value": "84%"},
                     {"Source": "Metacritic", "Value": "66/100"}],
         "Metascore": "66", "imdbRating": "8.4", "imdbVotes": "914,386",
         "imdbID": "tt0081505", "Type": "movie", "DVD": "15 Aug 2008",
         "BoxOffice": "$45,332,952",
         "Production": "Producers Circle, Warner Brothers, Peregrine, Hawk Films",
         "Website": "N/A", "Response": "True"},
        {"Title": "Alien", "Year": "1979", "Rated": "R",
         "Released": "22 Jun 1979", "Runtime": "117 min",
         "Genre": "Horror, Sci-Fi", "Director": "Ridley Scott",
         "Writer": "Dan O'Bannon (screenplay by), Dan O'Bannon (story by), Ronald Shusett (story by)",
         "Actors": "Tom Skerritt, Sigourney Weaver, Veronica Cartwright, Harry Dean Stanton",
         "Plot": "After a space merchant vessel receives an unknown transmission as a distress call, one of the crew is attacked by a mysterious life form and they soon realize that its life cycle has merely begun.",
         "Language": "English", "Country": "UK, USA",
         "Awards": "Won 1 Oscar. Another 17 wins & 22 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BMmQ2MmU3NzktZjAxOC00ZDZhLTk4YzEtMDMyMzcxY2IwMDAyXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "8.4/10"},
                     {"Source": "Rotten Tomatoes", "Value": "98%"},
                     {"Source": "Metacritic", "Value": "89/100"}],
         "Metascore": "89", "imdbRating": "8.4", "imdbVotes": "799,115",
         "imdbID": "tt0078748", "Type": "movie", "DVD": "25 Nov 2015",
         "BoxOffice": "$81,900,459",
         "Production": "Twentieth Century Fox, Brandywine Productions",
         "Website": "N/A", "Response": "True"},
        {"Title": "World War Z", "Year": "2013", "Rated": "PG-13",
         "Released": "21 Jun 2013", "Runtime": "116 min",
         "Genre": "Action, Adventure, Horror, Sci-Fi",
         "Director": "Marc Forster",
         "Writer": "Matthew Michael Carnahan (screenplay), Drew Goddard (screenplay), Damon Lindelof (screenplay), Matthew Michael Carnahan (screen story), J. Michael Straczynski (screen story), Max Brooks (based on the novel by)",
         "Actors": "Brad Pitt, Mireille Enos, Daniella Kertesz, James Badge Dale",
         "Plot": "Former United Nations employee Gerry Lane traverses the world in a race against time to stop a zombie pandemic that is toppling armies and governments and threatens to destroy humanity itself.",
         "Language": "English, Spanish, Hebrew, Arabic",
         "Country": "USA, UK, Malta", "Awards": "3 wins & 25 nominations.",
         "Poster": "https://m.media-amazon.com/images/M/MV5BNDQ4YzFmNzktMmM5ZC00MDZjLTk1OTktNDE2ODE4YjM2MjJjXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
         "Ratings": [{"Source": "Internet Movie Database", "Value": "7.0/10"},
                     {"Source": "Rotten Tomatoes", "Value": "66%"},
                     {"Source": "Metacritic", "Value": "63/100"}],
         "Metascore": "63", "imdbRating": "7.0", "imdbVotes": "607,786",
         "imdbID": "tt0816711", "Type": "movie", "DVD": "07 Jun 2015",
         "BoxOffice": "$202,359,711", "Production": "Plan B Films, 2DUX2",
         "Website": "N/A", "Response": "True"},
    ]


    @staticmethod
    def load():
        try:
            with open('db.db', 'r') as f:
                return pickle.load(f)
        except Exception as e:
            logging.error(e)

    @staticmethod
    def dump(game):
        try:
            with open('db.db', 'w')as f:
                pickle.dump(game, f)
        except Exception as e:
            logging.error(e)

    @staticmethod
    def get_random_movie():
        pass

    @staticmethod
    def new_game():
        idxs = random.sample(range(1, len(Supplier.remote_api)), Supplier.__settings.get("max_moviemons"))


    @staticmethod
    def load_default_settings():
        return {'grid_size_x': Supplier.__settings.get('size'), 'grid_size_y': Supplier.__settings.get('size'),
                'start_x': Supplier.__settings.get('start_x'), 'start_y': Supplier.__settings.get('start_y')}

    @staticmethod
    def get_strength():
        pass

    @staticmethod
    def get_movie():
        pass
