import os
import sys
import shutil
import struct
import imghdr
import glob

def main():       
    if len(sys.argv) != 4:
        print('usage : %s <res-folder> <material-design-root-folder> <img-name> \n ex: %s C:\\myproject\\res C:\\material-design-icons-master ic_camera_enhance_white_36dp.png' % (os.path.split(sys.argv[0])[0], os.path.split(sys.argv[0])[0]));
        return
    MATERIAL_ICONS = glob.glob(os.path.join(sys.argv[2], '*', 'drawable-*', '*.png'));
    for material_icon in MATERIAL_ICONS:
        if material_icon.endswith(sys.argv[3]):
            (root, filename) = os.path.split(material_icon)
            (root, folder) = os.path.split(root)
            dpi = folder.split('-')[-1]
            dst = os.path.join(sys.argv[1], 'drawable-'+dpi)
            try:
                shutil.copy(material_icon, dst)
                print("copied %s to %s\n" %(material_icon, dst))
            except:
                print("error in copying %s to %s" %(material_icon, dst))

if __name__ == "__main__":
    main()


