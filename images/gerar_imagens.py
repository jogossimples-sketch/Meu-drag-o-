from PIL import Image, ImageDraw, ImageFont
import os

if not os.path.exists("images"):
    os.makedirs("images")

def criar_imagem(nome_arquivo, tamanho, cor_fundo, conteudo):
    img = Image.new("RGB", tamanho, cor_fundo)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default(size=20)
    texto_largura, texto_altura = draw.textsize(conteudo, font=font)
    x = (tamanho[0] - texto_largura) // 2
    y = (tamanho[1] - texto_altura) // 2
    draw.text((x, y), conteudo, fill="black", font=font)
    img.save(f"images/{nome_arquivo}.png")

criar_imagem("dragao_normal", (512, 512), "lightyellow", "DRAGÃO\nSAUDÁVEL")
criar_imagem("dragao_faminto", (512, 512), "orange", "DRAGÃO\nFAMINTO")
criar_imagem("dragao_triste", (512, 512), "lightblue", "DRAGÃO\nTRISTE")
criar_imagem("dragao_sujo", (512, 512), "brown", "DRAGÃO\nSUJO")
criar_imagem("dragao_cansado", (512, 512), "gray", "DRAGÃO\nCANSADO")
criar_imagem("botao_comer", (100, 100), "red", "COMER")
criar_imagem("botao_brincar", (100, 100), "yellow", "BRINCAR")
criar_imagem("botao_limpar", (100, 100), "green", "LIMPAR")
                                  
