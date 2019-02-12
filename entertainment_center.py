import media
import fresh_tomatoes

logan = media.Movie("Logan",
                    "https://usercontent1.hubstatic.com/13519958.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

gotg = media.Movie("Guardian's of the Galaxy",
                   "https://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                   "https://www.youtube.com/watch?v=2LIQ2-PZBC8")

stepbros = media.Movie("Step Brothers",
                       "http://www.gstatic.com/tv/thumb/movieposters/175884/p175884_p_v8_ag.jpg",
                       "https://www.youtube.com/watch?v=_0TWeOrIYVI")

inception = media.Movie("Inception",
                        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

godfather = media.Movie("The Godfather",
                        "https://img.etsystatic.com/il/7af35b/1210293390/il_fullxfull.1210293390_5w3z.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

chef = media.Movie("Chef",
                   "http://www.impawards.com/2014/posters/chef_xlg.jpg",
                   "https://www.youtube.com/watch?v=wgFws3AoIUY")
movies = [logan, gotg, stepbros, inception, godfather, chef]

fresh_tomatoes.open_movies_page(movies)
