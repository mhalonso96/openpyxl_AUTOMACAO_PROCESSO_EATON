import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestScrapingService():
    def __init__(self):

        # options = Options()
        # options.add_argument("--disable-gpu")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    
        # #driver_service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    

    def start_scraping(self,url):
               
        self.driver.get(url)
        time.sleep(2)
        #button =  WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "py-2")))
       #self.driver.execute_script("arguments[0].click();", button)
        time.sleep(15)
        products = self.driver.find_elements(By.XPATH, '//*[@id="video-title"]')
        print(products)
       
            
        for product in range(0,len(products)):
            data = [
                products[product].text      
                ]
            print(data)