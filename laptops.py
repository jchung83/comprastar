
#from distutils import bcppcompiler
from calendar import c
from tracemalloc import stop
from selenium import webdriver
from openpyxl import Workbook
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import demo1
from openpyxl import workbook, load_workbook

#option = webdriver.ChromeOptions()
#option.add_argument('headless')
#driver = webdriver.Chrome("D:\\GIT\\SMC\\chromedriver.exe",options=option)
driver = webdriver.Chrome("D:\\GIT\\shopstar\\chromedriver.exe")
driver.maximize_window()

filepath = 'D:\\GIT\\shopstar\\laptop.xlsx' #  VARIABLE donde se ubica el excel
wb = load_workbook(filepath) # FUNCION OPENYXL Abre el excel

 

#-------- CLICKA NEXT  PARA CMABIAR DE PAGINACION ------------------- 
def clicking(i,x):
  for i in range(1):
      
        driver.find_element(By.XPATH, "//body/div[4]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[9]/a[1]").click()
                                        
        time.sleep(6)
        print(i,x)

def clicking2(i,x):
  for i in range(1):
      
        driver.find_element(By.XPATH, "//body/div[4]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[8]/a[1]").click()
        time.sleep(6)                 

      
#---------------- FUNCION ITERACION DE RPRODUCTOS DE UNA SOLAO PAGINACION + FUNCION CLCICK SIQUIENTE PAGINA ----------------------------
def shopstar(i,x,j):

    
    clicking(i,x)
    print("     HACE CLICK  PAGINA    " +  str(x))
    print(i,x)
    time.sleep(5)
    demo1.test(driver,j)

def shopstar2(i,x,j):

  
    clicking2(i,x)
    print("     HACE CLICK  PAGINA    " +  str(x))
    #time.sleep(1)
    demo1.test(driver,j)



#----------------- INCIO DE CAPTURADE LA PRIMERA PAGINA SIN ITERACION DE LAS DEMAS PROQUE ES LA INICIAL, NO NECESITA EL CLICK DEK NEXT--------------
def shopstar_home(driver,j):
    
       demo1.test(driver,j)


#-------------- COMIEMNZA EL CODIGO DE LA CAPTURA DE 10 PAGINAS DE SHOPSTAR TELEVISOR O LO QEU SEA  ---------------------


number_pages = 12 #  NUMERO DE PAGINAS 
web_site = "https://shopstar.pe/tecnologia/computo/laptops"



driver.get(str(web_site)) # abre eel navegador 
time.sleep(15) # tiempo de espera para que el navegador cargue completo


shopstar_home(driver,0) # PAGINA INCIAL

a=1

for i in range(7):
  #b=b+1
  c=24*(i+1)
 
  print(a,a,c)  # b es el numero de next, c es que celda comienza a incertar la data en el excel 24 en 24 filas
  
  shopstar(a,a,c) 

for i in range(7,number_pages):
  #b=b+1
  c=24*(i+7)
 
  print(a,a,c)  # b es el numero de next, c es que celda comienza a incertar la data en el excel 24 en 24 filas
  
  shopstar2(a,a,c) 
 



 


