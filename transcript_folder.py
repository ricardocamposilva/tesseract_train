import os
import sys
import pytesseract
import time

args = sys.argv[1:]

for file in os.listdir(args[0]):
    if file.split('.')[len(file.split('.'))-1] == 'png':
        string = pytesseract.image_to_string(f'{args[0]}/{file}', output_type='string', lang='spa_ricardo', config="--dpi 300 --psm 7")
        data = pytesseract.image_to_data(f'{args[0]}/{file}', lang='spa_ricardo', config="--dpi 300 --psm 7")

        print(pytesseract.get_tesseract_version())
        print(file)
        print(string)
        print(data)

        f = open(f'{args[0]}/{file.split(".")[0]}.txt', 'w')
        
        f.close()

        time.sleep(3)