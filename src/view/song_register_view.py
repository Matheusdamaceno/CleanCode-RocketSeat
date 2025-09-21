import os

class SongRegisterView:
  def registry_song_initial(self) -> dict:
    self.__clear()
    print("Implementar nova musica \n\n")

    title = input("Determine o nome da musica: ")
    artist = input("Determine o nome do artista: ")
    year = input("Determine o ano da musica: ")

    new_song_informations = {
      "title": title, "artist":artist, "year":year
    }

    return new_song_informations
  
  def __clear(self):
    os.system("cls||clear")