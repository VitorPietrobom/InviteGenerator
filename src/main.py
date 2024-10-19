import qrcode
from PIL import Image

NUMERO_DE_CONVITES = 10
MENSAGEM_QR_CODE = "Convite nº"
DIMENSAO_QR_CODE = 8
POSICAO_QR_CODE_W = 59
POSICAO_QR_CODE_H = 394

def gerar_qr_code(numero):
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=DIMENSAO_QR_CODE,
        border=1,
    )
    qr_code.add_data(MENSAGEM_QR_CODE + str(numero))
    img = qr_code.make_image(fill_color="black", back_color="white")
    caminho = "assets/qr_codes/qr_code_convite_" + str(numero) + ".png"
    img.save(caminho)
    return caminho

def juntar_imagens(caminho_qr_code, numero_convite):
    template = Image.open("assets/template.png")
    qr_code = Image.open(caminho_qr_code)
    template.paste(qr_code, (POSICAO_QR_CODE_H, POSICAO_QR_CODE_W))
    template.save("assets/convites/convite_" + str(numero_convite) + ".pdf", format="PDF")

def gerar_convites():
    for i in range(NUMERO_DE_CONVITES):
        caminho = gerar_qr_code(i+1)
        juntar_imagens(caminho_qr_code= caminho, numero_convite= i+1)

if __name__ == "__main__":
    input_usuario = input(	"Qual comando deseja executar? (1 -> Gerar convites, 2 -> Gerar QR unico, 3 -> Gerar convite unico) \n") 

    if input_usuario == "1":
        gerar_convites()

    elif input_usuario == "2":
        numero = input("Digite o numero do QR Code: ")
        gerar_qr_code(numero)

    elif input_usuario == "3":
        numero = input("Digite o numero do convite: ")
        caminho = gerar_qr_code(numero)
        juntar_imagens(caminho, numero)