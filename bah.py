from PIL import Image, ImageDraw, ImageFont

font_path = "BebasNeue-Regular.ttf" 

font_size = 300
font = ImageFont.truetype(font_path, size=font_size)
posisi = (230, 150)

warna = (0, 0, 0)

for i in range(1, 100):
    angka = f"{i:02d}"
    img = Image.open("1754472306-picsay.jpg")
    draw = ImageDraw.Draw(img)
    draw.text(posisi, angka, font=font, fill=warna)

    img.save(f"tiket/undian_{angka}.jpg")

print("Semua gambar udh dibuat peler.")
