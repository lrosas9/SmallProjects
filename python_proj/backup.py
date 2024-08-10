#from ast import Lambda
import os
import shutil
import datetime
import schedule
import time

source_dir = "C:\\Users\\User\\OneDrive\\Escritorio\\curso\\Screenshots"
dest_dir = "C:\\Users\\User\\OneDrive\\Escritorio\\curso\\Backups"

def copy_folder_to_directory(source, target):
    today = datetime.date.today()
    target_dir = os.path.join(target, str(today))
    try:
        shutil.copytree(source, target_dir)
        print(f"Folder copied to: {target_dir}")
    except FileExistsError:
        print(f"Folder already exists in {target}")

schedule.every().day.at("20:15").do(lambda: copy_folder_to_directory(source_dir, dest_dir))

while True:
    schedule.run_pending()
    time.sleep(60)