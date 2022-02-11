
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

 

#-------- CLICKA NEXT  PARA CMABIAR DE PAGINACION ------------------- 
def clicking(i,x):
  for i in range(1,10):
      if i<x:
        stop
        driver.find_element(By.XPATH, "//body/div[4]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[9]/a[1]").click()
        time.sleep(5)

def clicking2(i,x):
  for i in range(1,10):
      if i<x:
        stop
        driver.find_element(By.XPATH, "//body/div[4]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[8]/a[1]").click()
        time.sleep(8)

      
#---------------- FUNCION ITERACION DE RPRODUCTOS DE UNA SOLAO PAGINACION + FUNCION CLCICK SIQUIENTE PAGINA ----------------------------
def shopstar(i,x,j):

    driver.execute_script("window.scrollTo(0, 1200)")
    clicking(i,x)
    time.sleep(4)
    demo1.test(driver,j)

def shopstar2(i,x,j):

    driver.execute_script("window.scrollTo(0, 1200)")
    clicking2(i,x)
    time.sleep(4)
    demo1.test(driver,j)



#----------------- INCIO DE CAPTURADE LA PRIMERA PAGINA SIN ITERACION DE LAS DEMAS PROQUE ES LA INICIAL, NO NECESITA EL CLICK DEK NEXT--------------
def shopstar_home(j):
    
       demo1.test(driver,j)


#-------------- COMIEMNZA EL CODIGO DE LA CAPTURA DE 10 PAGINAS DE SHOPSTAR TELEVISOR O LO QEU SEA  ---------------------
driver.get("https://shopstar.pe/tecnologia/televisores")

time.sleep(10)
print("pagina Home   DEBERIA SER  Televisor Samsung Crystal 4K 60' UN60AU700... ")
shopstar_home(0)
print("segunda pagina DEBERIA SER Televisor PANASONIC LED 32' HD Smart TV T...   ")
shopstar(1,2,24)  # PAGINA INCIAL
print("tercera pagina  DEBERIA SER   TELEVISOR SAMSUNG 55 MOD: UN55AU7000GXPE")
shopstar(1,3,48)  # SEGUNDA PAGINA
print("cuarta pagina DEBERIA SER Televisor LG OLED 65'' 4K ThinQ AI OLED65G...")
shopstar(1,4,72)   # TERCERAPAGINA
print("quinta pagina DEBERIA SER  COMBO Televisor Qled 50 MAS Máquina de pop ... ")
shopstar(1,5,96) 
print("sexta pagina DEBERIA SER Televisor Sony 65 OLED 4K UHD Google TV S... ")
shopstar(1,6, 120)
print("septima pagina DEBERIA SER Televisor LG NanoCell 4K ThinQ AI 55 55NA...")
shopstar(1,7,144)
print("octava pagina DEBERIA SER  Televisor SAMSUNG LED 75 Ultra HD / 4K Sm...")
shopstar2(1,8,168)
print("novena pagina DEBERIA SER Televisor LG OLED 65 4K ThinQ AI OLED65G1...")
shopstar2(1,9,192)
print("decima pagin DEBERIA SER Televisor SAMSUNG 50 QN50Q60TAGXPE")
shopstar2(1,10,216)


    