import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names=['img0.jpg', 'img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg', 'img6.jpg', 'img7.jpg', 'img8.jpg', 'img9.jpg', 'img10.jpg']

start=time.perf_counter()
size=(1200, 1200)

def processImage(img_name):
    img=Image.open(img_name)
    img=img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')

#Using threads or cores may vary on the application and the software. On PC, this program performs better on threads, but on the Coral, it is faster using cores.
with concurrent.futures.ProcessPoolExecutor() as executor:
#with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(processImage, img_names)

finish=time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')