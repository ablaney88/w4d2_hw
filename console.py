import pdb 
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository  
import repositories.album_repository as album_repository

artist_repository.delete_all()

album_repository.delete_all()

artist_1 = Artist("Brand New")
artist_repository.save(artist_1)

artist_2 = Artist("Coheed & Cambria")
artist_repository.save(artist_2)

artist_3 = Artist("TesseracT")
artist_repository.save(artist_3)

album_1 = Album("Science Fiction")
album_repository.save(album_1)

album_2 = Album("Vaxis II: A Window of the Waking Mind")
album_repository.save(album_2)

album_3 = Album("Sonder")
album_repository.save(album_3)

# artist_2.artist_name = "Sleep Token"
# artist_repository.update(artist_2)

# album_2.album_name = "Sundowning"
# album_repository.update(album_2)

artist_repository.delete(artist_3.id)

album_repository.delete(album_3.id)

artists = artist_repository.select_all()

albums = album_repository.select_all()


