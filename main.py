from gtts import gTTS
import os

def criar_audiolivro(ficheiro_texto, saida_ficheiro):
    with open(ficheiro_texto, 'r', encoding='utf-8') as ficheiro: texto = ficheiro.read()

    tts = gTTS(texto=texto, lang='pt')

    tts.save(saida_ficheiro)
    print(f"Audio livro salvo como {saida_ficheiro}")
ficheiro_texto = "teste.txt"
saida_ficheiro = "audiolivro.mp3"

criar_audiolivro(ficheiro_texto, saida_ficheiro)
os.system(f"start {saida_ficheiro}")