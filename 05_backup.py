"""
Program that makes backup files in .zip
"""
from datetime import datetime
import os, zipfile, time

file_path = input("Enter path to file or folder:")
if not os.path.exists(file_path):
    raise Exception("File does not exist")
backup_time = input("Enter how often do you need to save (in mins):")

while True:
    zip_path = os.path.abspath(file_path) + '_' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.zip'
    backup_zip = zipfile.ZipFile(zip_path, 'w')
    if os.path.isdir(file_path):
        for folders, subfolders, files in os.walk(file_path):
            print('Adding  %s' % (folders))
            try:
                backup_zip.write(folders)
            except Exception as err:
                print(str(err))
            for file in files:
                if file.startswith(file_path) and file.endswith('.zip'): # if you archiving directory with backup it does not backup already existing backups
                    continue
                else:
                    try:
                        backup_zip.write(os.path.join(folders, file))
                    except Exception as err:
                        print(str(err))
    else:
        backup_zip.write(file_path)
    backup_zip.close()
    time.sleep(float(backup_time) * 60)
