from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the WebDriver executable
webdriver_path = r"C:/Users/mkart/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Start a Chrome WebDriver session (make sure you have downloaded chromedriver)
driver = webdriver.Chrome(executable_path=webdriver_path)

# Load the webpage
url = 'https://www.edx.org/search?tab=course&subject=Computer+Science'
driver.get(url)

# Wait for the dynamic content to load

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'base-card-link'))
)


# Extract the content
elements = driver.find_elements(By.CLASS_NAME, 'base-card-link')
print(elements)

# Close the browser
driver.quit()