import time
from PIL import Image, ImageFilter

img_names=['img0.jpg', 'img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg', 'img6.jpg', 'img7.jpg', 'img8.jpg', 'img9.jpg', 'img10.jpg']

start=time.perf_counter()
size=(1200, 1200)

for img_name in img_names:
    img=Image.open(img_name)
    img=img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')

finish=time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')