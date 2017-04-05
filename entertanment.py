import fresh_tomatoes
import media
"""This project is about movie Trailer .we are using classes.
In which we are using objects our objects are
Bad_Boys,Rush_Hour,Star_Wars,Jurassic_World .
here we are using Movie Trailer.
Their you tube links and Image address"""
Bad_Boys = media.Movie("Bad_Boys",
                       "American buddy cop action comedy film "
                       "directed by Michael Bay",
                       "produced by Jerry Bruckheimer, and "
                       "starring Martin Lawrence and Will Smith",
                       "https://encrypted-tbn3.gstatic.com/images?q=tbn:" +
                       "ANd9GcRQNmxaaP_xOVFy70_H-z-e_" +
                       "NthRazoHgQfJFxprGi615XJhvpJNA",
                       "https://youtu.be/ty8eBdHaf1c")
print(Bad_Boys.storyline)
Rush_Hour = media.Movie("Rush_Hour",
                        "Two cops from different cultures, "
                        "who cannot stand each other",
                        "https://encrypted-tbn3.gstatic.com/images?q=tbn:" +
                        "ANd9GcSbmxkKXhLaeoiYtPzVdOqUwd4ihKUy3ndjmOvo8r" +
                        "ZqY8GODBUAkg",
                        "https://youtu.be/JMiFsFQcFLE")
print(Rush_Hour.storyline)
Rush_Hour.show_trailer()
Star_Wars = media.Movie("Star_Wars",
                        "The Force Awakens",
                        "https://encrypted-tbn1.gstatic.com/images?q=tbn:" +
                        "ANd9GcSpbvzxAmqtLcgAAHCVydhCLSZb-" +
                        "Ec0e2pvvVLRQnSZblHkyOrHzA",
                        "https://youtu.be/sGbxmsDFVnE")
Jurassic_World = media.Movie("Jurassic_World",
                             "It was directed and co-written "
                             "by Colin Trevorrow",
                             "https://encrypted-tbn3.gstatic.com/images?q=" +
                             "tbn:ANd9GcSNupRR8W-jh1t7JwrBgwoWS6X2kF" +
                             "f8UOY1yp9n7anzoXtm8XD8Pw",
                             "https://youtu.be/RFinNxS5KN4")
"""We are using an Array of objects of movie"""
movies = [Bad_Boys, Rush_Hour, Star_Wars, Jurassic_World]
fresh_tomatoes.open_movies_page(movies)
