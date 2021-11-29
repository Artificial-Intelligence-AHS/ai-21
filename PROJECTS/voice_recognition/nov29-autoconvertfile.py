"""
Program converts a file on the github to the format required by Google Cloud Platform - wav file 
"""

import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://audio.online-convert.com/convert-to-wav")               # Open the website

# Make sure that file is in the directory and ends with ?raw=true
audioFileGithubLink = "https://github.com/Artificial-Intelligence-AHS/ai-21/blob/\
                       voice_recognition/PROJECTS/voice_recognition/audioFiles/\
                       1.mp3?raw=true"                                      # Link to the audio file on github

driver.find_element_by_id("externalUrlButton").click()                      # Click the external url button
driver.find_element_by_id("remoteUrlInput").send_keys(audioFileGithubLink)  # Enter the link
driver.find_element_by_id("addRemoteUrlButton").click()                     # Click the add remote url button

select = Select(driver.find_element_by_id('frequency'))                     # Select the frequency
select.select_by_value('16000')                                             # 16000 Hz
select2 = Select(driver.find_element_by_id('channels'))                     # Select the channels
select2.select_by_value('mono')                                             # Mono


driver.find_element_by_xpath("/html/body/div[4]/div[6]/div[1]/button").click() # Click the convert button

                                                                            # Constantly checks if the file is converted
while True:                                                                 # Loop until the file is converted                       
    try:                                
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div[1]/div[6]/div[2]/div/div/div[3]/div/a").click()
        break
    except:
        time.sleep(1)

driver.quit()                                                               # Close the browser

def getmostrecentwavfile(directory = "/Users/kunal/Downloads"):
    listofWavFiles = []
    for i in reversed(os.listdir(directory)):                               # Loop through the files in the directory
        if i.endswith(".wav"):                                              # If the file is a wav file
            listofWavFiles.append(directory + "/"+ i)                       # Append the file to the list
    return max(listofWavFiles, key=os.path.getctime)                        # Return the most recently made file


print(getmostrecentwavfile())