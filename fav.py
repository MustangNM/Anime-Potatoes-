import mediaa
import index

# list of movies
aSilentVoice = mediaa.Movie("A Silent Voice", "Great Movie", "silent.jpg",
                            "https://www.youtube.com/watch?v=syqBF25r1Ak")
KimiNoNawa = mediaa.Movie("Your Name", "A love story", "Kimi.no.Na.wa.jpg",
                          "https://www.youtube.com/watch?v=hRfHcp2GjVI")
TheLast = mediaa.Movie("The Last", "Ninja Love", "TheLast.jpg",
                       "https://www.youtube.com/watch?v=tA3yE4_t6SY")
BorutoTheMovie = mediaa.Movie("Boruto The Movie", "Spoiled Kid of Hokage",
                              "Boruto.jpg",
                              "https://www.youtube.com/watch?v=Qyonn5Vbg7s")
WolfChildren = mediaa.Movie("Wolf Children", "Human Wolves", "wolf.jpg",
                            "https://www.youtube.com/watch?v=MZpWdYruu48")
FiveCent = mediaa.Movie("5 Centimeters per Second", "Story", "5cent.jpg",
                        "https://www.youtube.com/watch?v=wdM7athAem0")

# Creating Array of Movies
movies = [aSilentVoice, KimiNoNawa, TheLast, BorutoTheMovie,
          WolfChildren,FiveCent]

# Opening the website
index.open_movies_page(movies)
