
# Browser Clean-Up Script

## Running Instructions   
1. Place the .exe file found in the "dist" folder on your local device. 
2. After starting the .exe, select "yes" after reading and confirming the pop-up disclaimer
3. Once the script completes there will be an additional acknowledgement pop-up

> [!NOTE]
> - The file has no prerequisite configuration or setup required.  
> - The script only takes a few seconds to run  
> - To verify what specific actions were completed or failed, review the log file found at "C:\Users\{username}\browsercleanup.log"
<br/>

>[!TIP]  
>For a breakdown of the code that is running, review the Browser_Clean-Up.py file.  
<br/>

## Key Functionality  
- Logging is enabled and set to a standard local dir. The process is designed to create this log file and continue to rewrite over the same file for each run. 
- The script prompts the user to confirm the action and acknowledge once the script has completed. 
- It kills any running instances of Chrome & Edge so it can delete the files utilized by those processes.
- The script is designed to run multiple delete actions simultaneously to optimize the process for speed. 
- A configuration file is intentionally not used to keep the script as lightweight as possible. 


## Screenshots
#### Launch the .exe file
<img width="627" height="171" alt="image" src="https://github.com/user-attachments/assets/33b6eb19-fc5b-4ac3-aca0-f995429d934f" />
  
#### Confirm the pop-up
<img width="475" height="219" alt="image" src="https://github.com/user-attachments/assets/d84c86c5-b18d-42d4-8ce6-84bc6307d763" />
  
#### Acknowledge the popup
<img width="488" height="245" alt="image" src="https://github.com/user-attachments/assets/9b430ae3-d950-4ede-ac7b-0f660ed5e245" />
  
#### Check the logs if required

  
> [!IMPORTANT]
> The script searches for and deletes the following files if they exist.
>
> ```
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Cache
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Code Cache
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Crashpad
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Crash Reports
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\GPUCache
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Local Storage
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Media Cache
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Session Storage
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Service Worker
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Sessions
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Storage
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\IndexedDB
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Extensions
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Extensions State
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Cookies
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Cookies-journal
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Web Data
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Web Data-journal
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Favicons
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Login Data
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Login Data-journal
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Preferences
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\QuotaManager
>C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\QuotaManager-journal
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Cache
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Code Cache
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Crashpad
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Crash Reports
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\GPUCache
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Local Storage
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Media Cache
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Session Storage
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Service Worker
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Sessions
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Storage
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\IndexedDB
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Extensions
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Extensions State
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Cookies
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Cookies-journal
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Web Data
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Web Data-journal
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Favicons
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data-journal
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Preferences
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\QuotaManager
>C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\QuotaManager-journal
> ```
___
