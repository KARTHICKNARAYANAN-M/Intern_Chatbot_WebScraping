from flask import Flask,render_template,request,jsonify
from chat import get_response

# Web Scraping Packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, render_template, request, jsonify
import time;

app=Flask(__name__)

@app.get("/")

def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    print(text)
    response=get_response(text)
    response1 = response.replace('\n', '<br>')
    message={"answer":response1}
    return jsonify(message)


#    Web Scraping Code 
#chrome driver application needs to be installed before using this command.
chrome_driver = r"C:/Users/mkart/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Make sure to include chromedriver.exe
options = Options()
options.headless = True

def scrape_edx_courses(branch):
    # Initialize the WebDriver with Chrome options
    print("********hi***********")
    browser = webdriver.Chrome(executable_path=chrome_driver,options=options)
        # Get the webpage

    if branch == "ComputerScience"or branch == "computerscience"or branch == "cse"or branch == "CSE":
        browser.get("https://www.edx.org/search?tab=course&subject=Computer+Science")

        #wait for the browser to render the website
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "base-card-wrapper")))
        time.sleep(20)


        # Get the page source after it has been loaded
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        links  = soup.find_all('a', {'class' : "base-card-link"})
        links_list =  [link['href'] for link in links]

        imgs = soup.find_all('img', {'class' : "pgn__card-image-cap show"})
        imgs_list = [img['src'] for img in imgs]

        titles = soup.find_all('div', {'class' : 'pgn__card-header-title-md'})
        titles_list = [title.find('span').text.strip() for title in titles]

        browser.quit()
    elif branch == "ECE"or branch == "ece"or branch == "Electronic Engineering"or branch == "Electronics":
        browser.get("https://www.edx.org/search?tab=course&subject=Electronics")

        #wait for the browser to render the website
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "base-card-wrapper")))
        time.sleep(20)


        # Get the page source after it has been loaded
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        links  = soup.find_all('a', {'class' : "base-card-link"})
        links_list =  [link['href'] for link in links]

        imgs = soup.find_all('img', {'class' : "pgn__card-image-cap show"})
        imgs_list = [img['src'] for img in imgs]

        titles = soup.find_all('div', {'class' : 'pgn__card-header-title-md'})
        titles_list = [title.find('span').text.strip() for title in titles]

        browser.quit() 
          
    elif branch == "civil"or branch == "CIVIL"or branch == "Civil Engineering":
        browser.get("https://www.edx.org/search?tab=course&page=1&skills.skill=Civil+Engineering&subject=Engineering")

        #wait for the browser to render the website
        wait = WebDriverWait(browser, 20)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "base-card-wrapper")))
        time.sleep(20)


        # Get the page source after it has been loaded
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        links  = soup.find_all('a', {'class' : "base-card-link"})
        links_list =  [link['href'] for link in links]

        imgs = soup.find_all('img', {'class' : "pgn__card-image-cap show"})
        imgs_list = [img['src'] for img in imgs]

        titles = soup.find_all('div', {'class' : 'pgn__card-header-title-md'})
        titles_list = [title.find('span').text.strip() for title in titles]

        browser.quit() 
        
    elif branch == "Mechanical"or branch == "mech"or branch == "MECH" or branch == "Mechanical Engineering":
        browser.get("https://www.edx.org/search?tab=course&page=1&skills.skill=Mechanical+Engineering&subject=Engineering")

        #wait for the browser to render the website
        wait = WebDriverWait(browser, 20)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "base-card-wrapper")))
        time.sleep(20)


        # Get the page source after it has been loaded
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        links  = soup.find_all('a', {'class' : "base-card-link"})
        links_list =  [link['href'] for link in links]

        imgs = soup.find_all('img', {'class' : "pgn__card-image-cap show"})
        imgs_list = [img['src'] for img in imgs]

        titles = soup.find_all('div', {'class' : 'pgn__card-header-title-md'})
        titles_list = [title.find('span').text.strip() for title in titles]

        browser.quit() 
        
    elif branch == "AI"or branch == "ai"or branch == "artificial intelligence"or branch == "Artificial Intelligence":
        browser.get("https://www.edx.org/search?tab=course&page=1&skills.skill=Artificial+Intelligence&subject=Engineering")

        #wait for the browser to render the website
        wait = WebDriverWait(browser, 20)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "base-card-wrapper")))
        time.sleep(20)


        # Get the page source after it has been loaded
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        links  = soup.find_all('a', {'class' : "base-card-link"})
        links_list =  [link['href'] for link in links]

        imgs = soup.find_all('img', {'class' : "pgn__card-image-cap show"})
        imgs_list = [img['src'] for img in imgs]

        titles = soup.find_all('div', {'class' : 'pgn__card-header-title-md'})
        titles_list = [title.find('span').text.strip() for title in titles]

        browser.quit() 
    
    elif branch == "Data Analysis"or branch == "Data Science"or branch == "data analysis"or branch == "Data Analytics":
        browser.get("https://www.edx.org/search?skills.skill=Data+Analysis")

        #wait for the browser to render the website
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "base-card-wrapper")))
        time.sleep(20)


        # Get the page source after it has been loaded
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        links  = soup.find_all('a', {'class' : "base-card-link"})
        links_list =  [link['href'] for link in links]

        imgs = soup.find_all('img', {'class' : "pgn__card-image-cap show"})
        imgs_list = [img['src'] for img in imgs]

        titles = soup.find_all('div', {'class' : 'pgn__card-header-title-md'})
        titles_list = [title.find('span').text.strip() for title in titles]

        browser.quit() 
        
    elif branch == "Full Stack "or branch == "Full Stack Development"or branch == "Web Development":
        browser.get("https://www.edx.org/search?skills.skill=Full+Stack+Development")

        #wait for the browser to render the website
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "base-card-wrapper")))
        time.sleep(20)


        # Get the page source after it has been loaded
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        links  = soup.find_all('a', {'class' : "base-card-link"})
        links_list =  [link['href'] for link in links]

        imgs = soup.find_all('img', {'class' : "pgn__card-image-cap show"})
        imgs_list = [img['src'] for img in imgs]

        titles = soup.find_all('div', {'class' : 'pgn__card-header-title-md'})
        titles_list = [title.find('span').text.strip() for title in titles]

        browser.quit() 

    print(titles_list)
    print("*************************")
    print(links_list)
    print("******************")
    print(imgs_list)
    return titles_list, links_list, imgs_list

@app.route('/')
@app.get("/")

@app.post("/scraping")
def scrape():
    branch=request.get_json().get("branch")
    title, link, img  = scrape_edx_courses(branch)
    data = {"title" : title, "link" : link, "img" : img}
    print(data)
    return jsonify(data)
 
if __name__=="__main__":
    app.run(debug=True)