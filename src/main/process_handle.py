from src.view.first_view import introduction_page
from .contructor.song_register_contructor import song_register_process

def start()-> None:
  while True:

      command=introduction_page()
      if command == '1' : song_register_process()
      elif command == '2' : print("Criando Playlist")
      elif command == '5' : print("Saindo"), exit()
      else: print("\n comando nao encontrado, tente novamente\n\n " )