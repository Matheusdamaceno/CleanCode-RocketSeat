def introduction_page() -> str:
  message= ''' 
    Sitema Musical

  *  Cadastrar musica - 1
  *  Criar Playlist - 2
  * Sair - 5 
'''

  print(message)
  command=input("Comando: ")
  return command
    

