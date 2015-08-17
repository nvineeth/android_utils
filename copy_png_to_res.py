import os
import shutil
import glob
import sys

RESOLUTION_MAP = {'@1.5x':'hdpi', '@2x':'xhdpi', '@3x':'xxhdpi',  '@mdpi':'mdpi', '@hdpi':'hdpi', '@xhdpi':'xhdpi', '@xxhdpi':'xxhdpi', }

if len(sys.argv) < 3:
    print("Usage %s <res dir> <img-dir> <img-patter>"% os.path.split(sys.argv[0])[-1]);
    sys.exit(-1)


RES_DIR = sys.argv[1];

pattern = "*"
if len(sys.argv) == 4 and sys.argv[3] != "*": pattern = sys.argv[3] + "*"

png_files = glob.glob(os.path.join(sys.argv[2], pattern + '.png'))


for file in png_files:
    lower_file = os.path.split(file)[-1].lower();
    try:
        dst = ''
        if lower_file.find('@') != -1:
            r = '@' + lower_file.split('@')[-1].replace('.png','')
            lower_file = lower_file.replace(r,'')
            dst = os.path.join(RES_DIR, 'drawable-' + RESOLUTION_MAP[r], lower_file)
            shutil.copy(file, dst)
        else:
            dst = os.path.join(RES_DIR, 'drawable-mdpi', lower_file)
            shutil.copy(file, os.path.join(RES_DIR, 'drawable-mdpi', lower_file))
        print('copied ' + file + ' to ' + dst + '\n');
    except:
        print('error in copying ' + file)
        pass
