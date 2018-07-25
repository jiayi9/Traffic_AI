from PIL import Image
im = Image.open('D:/car/train_b/00c7d278-bdd6-4b5d-8026-81ee033f99f9.jpg')
im.show()


import os
PATH = 'D:/car/train_b'
for i in os.listdir(PATH)[1:10]:
    ABS_PATH = os.path.join(PATH, i)
    print(ABS_PATH)
#    im = Image.open(ABS_PATH)
#    im.show()
    



import pandas as pd
D = pd.read_csv('D:/car/train_b.csv', sep =',')
D.sample(2)

D2 = D.loc[1:10,'name']

for i in D2[1:3]:
    print(i)   
    COORD = D[D.name == i].coordinate.to_string()
    print(COORD)
    CARS = COORD.split(';')
    print(CARS)
    for j in CARS:
        x = j.split('_')
        print(x)
    ABS_PATH = os.path.join(PATH, i)
 #   print(ABS_PATH)
 #   im = Image.open(ABS_PATH)
 #   im.show()
str = '1042_0_27_47;391_12_128_110;292_171_179_183'

str.split(';')

tmp = D[D.name == 'eeeb4783-6acb-4e83-9adf-fc0d2ee1f74d.jpg'].coordinate
tmp



for i in os.listdir('C:/COS'):
    if i.endswith('.txt'):
        print(i)
['myfile_'+x for x in os.listdir('C:/COS') if x.endswith('.txt')]



for root, dirs, files in os.walk('C:/DNOX'):
    print(root)
    # This prints all full path of dir (including the root path)
    
    print(dirs)
    # This prints all folders in the full path shown above correspondingly
    
    print(files)
    # This prints all file names (NOT folder) in the full path shown in the first print above

    
    
import glob, os
os.chdir("C:/COS")
for file in glob.glob("*.txt"):
    print(file)
    
