from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_selenium_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    
    service= Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)

    return driver

if __name__=="__main__":
    driver = create_selenium_driver()
    driver.get("https://www.google.com/")
    print(driver.title)