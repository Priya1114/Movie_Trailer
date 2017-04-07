import fresh_tomatoes
import media
"""This is the file in which we make instances of Movie class"""

toy_story = media.Movie("Toy story", "Movie in which toys get alive",
                        "https://lumiere-a.akamaihd.net/v1/images/" +
                        "open-uri20150422-20810-m8zzyx_5670999f" +
                        ".jpeg?region=0%2C0%2C300%2C450",
                        "https://youtu.be/KYz2wyBy3kc")
mib = media.Movie("Men in Black", "Story of men vs aliens",
                  "https://encrypted-tbn2.gstatic.com/images" +
                  "?q=tbn:ANd9GcRJGFUx5KaCafUEdnmfu7gHI0MyW" +
                  "mkbQ6L8DfteWUGh9oLWRaGF",
                  "https://youtu.be/Z2wbsY3Ktfg")
nightm = media.Movie("Night at the measum", "A measum where things get alive",
                     "https://encrypted-tbn2.gstatic.com/images" +
                     "?q=tbn:ANd9GcR1KC1q2HSSI7L_uJ_EPI2BNqhdX9oN" +
                     "M6PnAI-5kIKmx24LxAmlXA", "https://youtu.be/i0vTJeYLRnA")
avator = media.Movie("Avator", "story of aliens",
                     "https://encrypted-tbn1.gstatic.com/images" +
                     "?q=tbn:ANd9GcQe3oKCiqho0cOlqKqbeFC7v8NAOPm" +
                     "K9gs1KpinjhOR-JuXYElpAw",
                     "https://youtu.be/5PSNL1qE6VY")
snow = media.Movie("Snowhite", "Story of a girl and seven dwarfs",
                   "http://cdn.playbuzz.com/cdn/"+"ad25bdf2-da81" +
                   "-4523-999a-61b6a" +
                   "e92f442/b82c0be6-97d9-4e6f-ba29-0f694102dbbe" +
                   ".jpg", "https://youtu.be/GKVtjm2DgtE")
shrek_m = media.Movie("Shrek", "Story of a funny monster",
                      "https://s-media-cache-ak0.pinimg.com/736x/f" +
                      "c/30/34/fc3034754f7e84c632c02e"+"eef81b1953.jpg",
                      "https://youtu.be/V-bZhXzo2-k")

'''Making an array of objects of Movie class and naming it movies'''

movies = [toy_story, mib, nightm, avator, snow, shrek_m]
'''This is a function of fresh_tomatoes which opens a website in browser with
   all the movies listed which are present in 'movies' array'''
fresh_tomatoes.open_movies_page(movies)
