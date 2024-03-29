A simple project that uses Selenium and Python to screen scrape a rumble live stream to get the live user count and post it to a text file for OBS to read.

I run this on a windows machine using Task Scheduler and in a batch file. I have found the script runs in just under 10secs in CMD and PowerShell. I run the script every minute to update the text file.

INSTALLATION;
just need to install Python - https://www.python.org/
and install Selenium - https://www.selenium.dev/
  - you want the web driver, there docs are here; https://www.selenium.dev/documentation/webdriver/ the easiest thing to do here, is just install the latest version of the web browser chrome.
  - basically from PowerShell i type; pip install selenium
  - after that you should be good to go on running the script

If you find this useful, please feel to buy me a beer @GoChadTV (Venmo) - $GoChadTV (CashApp) - https://ko-fi.com/gochadtv 

To see a working example of this, goto; https://rumble.com/CountryMusicRdo/live
