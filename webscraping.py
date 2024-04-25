from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver = r"C:/Users/mkart/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Make sure to include chromedriver.exe
options = Options()
options.headless = True

# Initialize the WebDriver with Chrome options
browser = webdriver.Chrome(executable_path=chrome_driver)

#service = Service(executable_path=chrome_driver)
#options = webdriver.ChromeOptions()
#browser = webdriver.Chrome(service=service, options=options)

# Get the webpage
browser.get("https://www.edx.org/search?tab=course&subject=Computer+Science")

wait = WebDriverWait(browser, 20)  # Adjust the timeout as needed
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "base-card-wrapper")))


time.sleep(3)

# Wait for the page to load, you can use explicit wait if necessary

# Get the page source after it has been loaded
soup = BeautifulSoup(browser.page_source, 'html.parser')



#titles = soup.find_all('div', class_='pgn__card-header-title-md')
#links = soup.find_all("a", class_= "base-card-link")
#subtitles = soup.find_all('div',{'class':'pgn__card-header-subtitle-md'})


links  = soup.find_all('a', {'class' : "base-card-link"})
links_list =  [link['href'] for link in links]


imgs = soup.find_all('img', {'class' : "pgn__card-image-cap show"})
imgs_list = [img['src'] for img in imgs]

titles = soup.find_all('div', {'class' : 'pgn__card-header-title-md'})
titles_list = [title.find('span').text.strip() for title in titles]












# Wait for the element to be present on the page
#element = WebDriverWait(browser, 10)


# Close the browser
browser.quit()