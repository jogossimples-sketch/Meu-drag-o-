import pgzrun
import random
from datetime import datetime

meu_dragao = {
    "nome": "Ember",
    "fome": 50,
    "felicidade": 50,
    "limpeza": 50,
    "energia": 50,
    "ultima_verificacao": datetime.now()
}

WIDTH = 400
HEIGHT = 600

personagem = Actor("dragao_normal", (WIDTH/2, HEIGHT/2))
botao_comer = Actor("botao_comer", (100, 500))
botao_brincar = Actor("botao_brincar", (200, 500))
botao_limpar = Actor("botao_limpar", (300, 500))

def atualizar_status():
    tempo_passou = (datetime.now() - meu_dragao["ultima_verificacao"]).total_seconds() / 60
    if tempo_passou > 0:
        meu_dragao["fome"] -= tempo_passou * 2
        meu_dragao["felicidade"] -= tempo_passou * 1.5
        meu_dragao["limpeza"] -= tempo_passou * 1
        meu_dragao["energia"] -= tempo_passou * 0.8

        for status in ["fome", "felicidade", "limpeza", "energia"]:
            meu_dragao[status] = max(0, min(100, meu_dragao[status]))
        meu_dragao["ultima_verificacao"] = datetime.now()

    if meu_dragao["fome"] < 20:
        personagem.image = "dragao_faminto"
    elif meu_dragao["felicidade"] < 20:
        personagem.image = "dragao_triste"
    elif meu_dragao["limpeza"] < 20:
        personagem.image = "dragao_sujo"
    elif meu_dragao["energia"] < 20:
        personagem.image = "dragao_cansado"
    else:
        personagem.image = "dragao_normal"

def update():
    atualizar_status()

def draw():
    screen.fill((135, 206, 235))
    screen.draw.text(f"Fome: {int(meu_dragao['fome'])}%", (50, 50), color="red", fontsize=24)
    screen.draw.text(f"Felicidade: {int(meu_dragao['felicidade'])}%", (50, 90), color="yellow", fontsize=24)
    screen.draw.text(f"Limpieza: {int(meu_dragao['limpeza'])}%", (50, 130), color="green", fontsize=24)
    screen.draw.text(f"Energia: {int(meu_dragao['energia'])}%", (50, 170), color="blue", fontsize=24)
    screen.draw.text(meu_dragao["nome"], (170, 20), color="darkblue", fontsize=32, bold=True)
    personagem.draw()
    botao_comer.draw()
    botao_brincar.draw()
    botao_limpar.draw()

def on_mouse_down(posicao):
    if botao_comer.collidepoint(posicao) and meu_dragao["fome"] < 100:
        meu_dragao["fome"] += random.randint(10, 20)
        meu_dragao["energia"] -= random.randint(2, 5)
    elif botao_brincar.collidepoint(posicao) and meu_dragao["felicidade"] < 100:
        meu_dragao["felicidade"] += random.randint(10, 20)
        meu_dragao["fome"] -= random.randint(3, 6)
        meu_dragao["energia"] -= random.randint(5, 10)
    elif botao_limpar.collidepoint(posicao) and meu_dragao["limpeza"] < 100:
        meu_dragao["limpeza"] += random.randint(15, 25)
        meu_dragao["felicidade"] += random.randint(3, 8)

pgzrun.go()
