from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    # Make sure you have the newest chrome browser installed
    options = webdriver.ChromeOptions()
    # Setting the detach parameter to true will keep the browser open after the process has ended, 
    # So long as the quit command is not sent to the driver.
    #options.add_experimental_option("detach", True)
    # Removes the "Automation Warning"
    options.add_experimental_option("excludeSwitches", ['enable-automation']);
    # Headless makes the window not even appear.
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    # This is the URL of the Rumble live stream
    driver.get("https://rumble.com/CountryMusicRdo/live")

    # Thought I would need a wait timing, but did not need this.
    # if you need to use this make sure you have "import os" at the top
    #driver.implicitly_wait(0.5)

    # this is the class that holds number of current users on the live stream
    viewers_total = driver.find_element(By.CLASS_NAME, "live-video-view-count-status-count").text

    # Writing a text file that OBS can read
    # Added this to keep everything clean but its not needed
    #Going check if the file exists
    #if os.path.exists("rumble_viewer_count.txt"):
    #  os.remove("rumble_viewer_count.txt")
    #else:
    #  print("No file!")

    # Writing the file for OBS to read
    f = open("rumble_viewer_count.txt", "w")
    f.write(viewers_total)
    f.close()

    # Just a graphical output for debugging
    print("Printed the totals! - "+viewers_total)

    driver.quit()
except:
    exit()
