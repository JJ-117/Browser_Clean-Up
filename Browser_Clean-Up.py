import getpass
import logging
import os
import time
import shutil
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
from tkinter import messagebox

################## Define Variables ##################
# Get the current working user
username = getpass.getuser()
# Define a log file path
log_file_path = fr'C:\Users\{username}\browser_cleanup.log'
# Browsers dictionary with pathjs to browser data
browsers = {
    'Google Chrome': fr'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default',
    'Microsoft Edge': fr'C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default',
}
# Folders to delete (excluding history and bookmarks)
folders = [
    'Cache',
    'Code Cache',
    'Crashpad',
    'Crash Reports',
    'GPUCache',
    'Local Storage',
    'Media Cache',
    'Session Storage',
    'Service Worker',
    'Sessions',
    'Storage',
    'IndexedDB',
    'Extensions',
    'Extensions State',
    ]
# Files to delete (excluding history and bookmarks)
files = [
    'Cookies',
    'Cookies-journal',
    'Web Data',
    'Web Data-journal',
    'Favicons',
    'Login Data',
    'Login Data-journal',
    'Preferences',
    'QuotaManager',
    'QuotaManager-journal',
    ]

################## Setup Logging ##################
# Ensure the log file is created and set up logging
open(log_file_path, 'w').close()
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(
    filename=log_file_path,
    encoding='utf-8',
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )
logging.info('Browser Clean-Up started.')

##################### Prompt user for confirmation to perform the clean-up ##################
if messagebox.askyesno('Browser Clean-Up Request', 'Do you want to continue? All browser data will be deleted. This action does NOT delete History or Bookmarks. This action cannot be undone.'):
    logging.info('User confirmed the clean-up operation.')
    pass
else:
    logging.info('User confirmed the clean-up operation.')
    exit()

#################### Function to Delete Files and Folders ##################
def delete_files_and_folders(path):
    try:
        # Check if the browser path exists
        if os.path.isdir(path):
            shutil.rmtree(path)
            logging.info(f'Deleted folder: {path} --moving to the next path')
        elif os.path.isfile(path):
            os.remove(path)
            logging.info(f'Deleted file: {path} --moving to the next path')
        else:
            logging.warning(f'Path does not exist: {path} --moving to the next path')
    except Exception as e:
        logging.error(f'Error deleting {path}: {e} --moving to the next path')

#################### Perform Clean-Up ##################
try:
    os.system('taskkill /f /im chrome.exe /T')
    logging.info('Chrome process terminated if running.')
    time.sleep(1)
    os.system('taskkill /f /im msedge.exe /T')
    logging.info('Edge process terminated if running.')
    time.sleep(2
               )
    # Create a thread pool to delete files and folders concurrently
    if __name__ == '__main__':
        paths_to_delete = []
        for browser, path in browsers.items():
            for folder in folders:
                paths_to_delete.append(os.path.join(path, folder))
            for file in files:
                paths_to_delete.append(os.path.join(path, file))
        with ThreadPoolExecutor(max_workers=4) as executor:
            # Submit delete tasks to the thread pool
            logging.info('Starting concurrent clean-up process.')
            executor.map(delete_files_and_folders, paths_to_delete)
    else:
        logging.error('This script was not able to run as expected.')
        messagebox.showerror('Error', 'This script has failed to complete. Please perform the clean-up manually.')
except Exception as e:
    logging.error(f'An error occurred during the clean-up process: {e}')
finally:
    logging.info('Browser Clean-Up completed.')
    # Show completion message
    messagebox.showinfo('Browser Clean-Up Completed', 'Browser clean-up completed successfully. Please check the log file for any specifics.\n\n')
