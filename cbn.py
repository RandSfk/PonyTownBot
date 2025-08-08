from PIL import Image, ImageOps
import os

img_folder = r"tiket"
output_folder = "./output"
os.makedirs(output_folder, exist_ok=True)

img_prefix = "undian_"
img_ext = ".jpg"
total_images = 99
cols = 3
rows = 7
images_per_sheet = cols * rows
padding = 10

top_space = 200
bottom_space = 200

thumb_width = 1000
thumb_height = int(thumb_width * 9 / 16)

final_width = cols * thumb_width + (cols + 1) * padding
inner_height = rows * thumb_height + (rows + 1) * padding
final_height = top_space + inner_height + bottom_space

try:
    resample = Image.Resampling.LANCZOS
except AttributeError:
    resample = Image.ANTIALIAS

def get_image_path(index):
    return os.path.join(img_folder, f"{img_prefix}{index:02d}{img_ext}")

for batch_start in range(1, total_images + 1, images_per_sheet):
    batch_end = min(batch_start + images_per_sheet - 1, total_images)
    image_paths = [get_image_path(i) for i in range(batch_start, batch_end + 1)]

    collage = Image.new("RGB", (final_width, final_height), color=(255, 255, 255))

    for idx, path in enumerate(image_paths):
        try:
            img = Image.open(path).convert("RGB")
            img = img.resize((thumb_width, thumb_height), resample)
        except Exception as e:
            print(f"Gagal membuka {path}: {e}")
            continue
        row = idx // cols
        col = idx % cols
        x = padding + col * (thumb_width + padding)
        y = top_space + padding + row * (thumb_height + padding)
        collage.paste(img, (x, y))
    output_file = os.path.join(output_folder, f"output_{(batch_start - 1) // images_per_sheet + 1}.jpg")
    collage.save(output_file)
    print(f"Tersimpan: {output_file}")
