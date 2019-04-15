import os
import shutil
from PIL import Image

path = os.path.expanduser('~\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')

out_path_landscape = os.getcwd() + '\\landscape\\'
out_path_portrait = os.getcwd() + '\\portrait\\'

minsize = 100000

if not os.path.exists(out_path_landscape):
    os.makedirs(out_path_landscape)

if not os.path.exists(out_path_portrait):
    os.makedirs(out_path_portrait)

file_paths = [f for f in os.listdir(path) if os.path.getsize(os.path.join(path, f)) > minsize]

for file_name in file_paths:
    img_pth = os.path.join(path, file_name)
    
    img = Image.open(img_pth)
    (width, height) = img.size

    if (width > height):
        out_path = out_path_landscape
    else:
        out_path = out_path_portrait

    shutil.copy(img_pth, out_path)
    os.rename(os.path.join(out_path, file_name), os.path.join(out_path, file_name+'.jpg'))
