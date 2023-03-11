import qrcode

texto = input("Insira um texto/Url: ")
QR = qrcode.QRCode(version=1,box_size=10,border=5)
QR.add_data(texto)
QR.make(fit=True)


img = QR.make_image(fill_color="green", back_color="white")
nome_arquivo= texto + ".png"
img.save(nome_arquivo)
print("Salvo com sucesso!")
