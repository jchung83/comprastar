
from distutils import bcppcompiler
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import demo1

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome("D:\\GIT\\SMC\\chromedriver.exe",options=option)
driver.get("https://shopstar.pe/tecnologia/televisores")
time.sleep(15)

list =[1,2,3,4,5,6,7,8,9,10]

for idx, val in enumerate(list):

  demo1.test(driver,idx)


  print(" pasa por aqui")
  time.sleep(5)
    