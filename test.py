
#from distutils import bcppcompiler
from tracemalloc import stop
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
#driver = webdriver.Chrome("D:\\GIT\\SMC\\chromedriver.exe")
#driver.maximize_window()

clicks =  'driver.find_element(By.XPATH, "//body/div[4]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[9]/a[1]")'
web = 'driver.get("https://shopstar.pe/tecnologia/televisores")'
cli = 'clicks.click()'
dem = 'demo1.test(driver,0)'
 
def clicking(i,x):
  for i in range(1,10):
      if i<x:
        stop
        driver.find_element(By.XPATH, "//body/div[4]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[9]/a[1]").click()
        time.sleep(5)

      




def shopstar(i,x,j):

    driver.get("https://shopstar.pe/tecnologia/televisores")
    time.sleep(5)
    clicking(i,x)
    demo1.test(driver,j)


shopstar(0,0,0)  # PAGINA INCIAL
print("primera pagina")
shopstar(1,2,24)  # SEGUNDA PAGINA
print("segunda pagina")
shopstar(1,3,48)   # TERCERAPAGINA
print("tercera pagina")
shopstar(1,4,72) 
print("tercera pagina")
shopstar(1,5, 96)
print("cuarta pagina")
shopstar(1,6,120)
print("quinta pagina")
shopstar(1,7,144)
shopstar(1,8,168)
shopstar(1,9,192)
shopstar(1,10,216)
shopstar(1,11,240)


