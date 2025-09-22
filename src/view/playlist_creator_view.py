import os

class PlaylistCreatorView:
  def playlist_creator_sucess(self, controller_response) ->None:
    self.__clear()
    print("Playlist criado com sucesso \n\n")

    for music in controller_response["playlist"]:
      message = '''
        Titulo da musica: {}
        Artista: {}
        Ano da publicação: {}
      '''.format(
        music.title,
        music.artist,
        music.year
      )
      print(message)

  def playlist_creator_fail(self, controller_response) ->None:
    self.__clear()

    message='''
      Erro na criação da playlist]

      * Erro:{}

    '''.format(
        controller_response["error"]
    )
    print(message)

  def __clear(self):
    os.system("cls||clear")