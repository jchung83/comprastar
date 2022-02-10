
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
time.sleep(5)

list =[1]

for idx, val in enumerate(list):

  print(idx,val)

  demo1.test(driver,idx) # Esta funcion trae todos los elementos de la paginacion 1 itera 24 veces numero de productos


  print(" pasa por aqui")
  time.sleep(5)
    