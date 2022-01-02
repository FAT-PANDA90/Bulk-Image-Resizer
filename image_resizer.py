__author__ = "SABYASACHI SHARMA"
__title__ = "ScanImage Resizer"
import os
from PIL import Image
import zipfile


try:
    print(f"Programmed by Sabyasachi Sharma (835148)")
    print(f"Keep all the files in one folder and run this program")
    print(f"Warning: all images will be replaced with resized images bearing "
          f"filename:-edited_original_file_name")
    input("Press enter when ready")
except SyntaxError:
    pass
to_delete = []
for file in os.listdir():
    if file.endswith('.jpg'):
        im = Image.open(file)
        new_im = im.resize((620, 870), Image.ANTIALIAS)
        new_im.save(f'edited_{os.path.splitext(file.title())[0]}.jpg')
        to_delete.append(file.title())

zf = zipfile.ZipFile('originals.zip', mode='w') # zipping original files and then deleting them
for file in os.listdir():
    if file.title() in to_delete:
        zf.write(file)
        os.remove(file)
zf.close()
try:
    print("original files replaced with new resized images")
    input("Press enter to exit")
except SyntaxError:
    pass
