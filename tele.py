from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By 
#import Data_reader
from demo1 import *

option = webdriver.ChromeOptions()
option.add_argument('headless')
#driver = webdriver.Chrome("D:\\GIT\\SMC\\chromedriver.exe",options=option)
driver = webdriver.Chrome("D:\\GIT\\SMC\\chromedriver.exe")



 

def clicks():                           # FUNCIIONE DE CLICKS 
  for i in  range (1,11):
     print("hace click " + str(i))
    
     driver.find_element(By.XPATH, "//body/div[4]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[9]/a[1]").click()
     driver.maximize_window()

def urls(g):                             # FUNCION URL DE PAGIAN WEB 
    print("esta es la variable que deberia crecer" +str(g))
    driver.get("https://shopstar.pe/tecnologia/televisores")
    time.sleep(15)
       
     
    time.sleep(6)
    
    #print( "numero de la iteracion web " + i)

list =[1,2,3,4,5,6,7,8,9,10]
g=0
for idx, val in enumerate(list):
    
    g=idx+2
    #print(idx, val)
  
    urls(g)
    #print( "esta es la paginacion numero " +str(idx+1))
    #print(urls(i))
      # MODELO NOMBRE
    #driver.get('%s' % val)
    
    
    
    #print(val)
    driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

    demo1.pag_bucle(driver,idx)
    #demo1.test(driver, idx)
