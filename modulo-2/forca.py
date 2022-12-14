import os
from glob import glob
from random import choice
from time import sleep


erro_0 = """
   |-------
   |      |
   |    
   |    
   |    
   |     
   |     
___|___ 
"""
erro_1 = """
   |-------
   |      |
   |      _
   |     |_|
   |      
   |     
   |     
___|___ 
"""

erro_2 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |      |
   |      |
   |     
___|___ 
""")

erro_3 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|
   |      |
   |     
___|___ 
""")

erro_4 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     
___|___ 
""")

erro_5 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     / 
___|___ 
""")

erro_6 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     / \\
___|___ 
""")

grafico_forca = [erro_0,erro_1,erro_2,erro_3,erro_4,erro_5,erro_6]


def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def sorteia_palavra():
  # cria uma lista com todos os paths de arquivos TXT
  listas_palavras = glob('*.txt')
  if listas_palavras:
    # sorteia um path desses arquivos
    lista_sorteada = choice(listas_palavras)
    # carrega o arquivo e cria uma lista das palavras
    with open(lista_sorteada) as arquivo:
      palavras = arquivo.read().split('\n')
    palavras = [palavra.upper() for palavra in palavras if palavra != '']
    # se houver palavras, sorteia uma
    if palavras:
      palavra_sorteada = choice(palavras)
      classe_palavra = lista_sorteada.replace('.txt','').upper()
    
      return classe_palavra, palavra_sorteada
    else:
      return (None,None)
  else:
    return (None,None)


def palavra_secreta(palavra:str,mostrar_letras=[]):
  palavra_secreta = ''.join([letra if letra in mostrar_letras else ' _ ' for letra in palavra])
  return palavra_secreta


def dica(classe_palavra:str, palavra_sorteada:str):
  print(f'Pertence a {classe_palavra} com {len(palavra_sorteada)} letras.')


def leia_letra(msg):
    letra = input(msg)
    while not (len(letra) == 1 and letra.isalpha()):
        print('Entrada inv??lida!')
        letra = input(msg)
    return letra.upper()


def leia_resposta(msg:str) -> bool:
    resposta = input(msg).lower() 
    while resposta not in ('s','n'): 
        print('Resposta Inv??lida') 
        resposta = input(msg).lower() 
    if resposta == 's': 
        return True 
    else: 
        return False


def jogar(classe_palavra, palavra_sorteada, letras_escolhidas, erros):
    while True:
        # Muito bom essa parte
        print('{:=^20}'.format('Jogo da Forca'))
        dica(classe_palavra, palavra_sorteada)

        if letras_escolhidas:
            # Modificado para ficar mais claro para a pessoa jogadora
            print(f'Letras j?? escolhidas: {"-".join(letras_escolhidas)}')
        print(grafico_forca[erros])
        print(palavra_secreta(palavra_sorteada,letras_escolhidas))

        if palavra_secreta(palavra_sorteada,letras_escolhidas) == palavra_sorteada:
            print(f'Parab??ns, voc?? acertou!')
            break

        if erros < 6:
            letra_usuario = leia_letra('Digite uma letra: ')

            if letra_usuario not in letras_escolhidas:
                letras_escolhidas.append(letra_usuario)

                if letra_usuario not in palavra_sorteada:
                    erros += 1
                    print(f'Letra {letra_usuario} n??o faz parte da palavra.')
                    sleep(2)

            else:
                print(f'Voc?? j?? escolheu a letra {letra_usuario}!')    
                sleep(2)
            limpa_tela()

        else:
            print(f'Que pena! Voc?? perdeu. A palavra era : {palavra_sorteada}')
            break


def main():
    continuar_jogo = True
    while continuar_jogo:
      classe_palavra, palavra_sorteada = sorteia_palavra()
      if not classe_palavra:
        raise FileNotFoundError('Arquivo de palavras ausente!')
      erros = 0
      letras_escolhidas = []
      jogar(classe_palavra, palavra_sorteada, letras_escolhidas, erros)

      continuar = leia_resposta('Deseja continuar (s/n)? ')
      limpa_tela()
      if not continuar:
          print('Jogo Encerrado.')
          sleep(2)
          continuar_jogo = False
      else:
          continuar_jogo = True


main()
