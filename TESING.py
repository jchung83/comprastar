from tracemalloc import stop
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path="D:\\GIT\\SMC\\chromedriver.exe")



def clicking(i,x):
  for i in range(1,10):
      if i<x:
          print(i)


def clicking(i,x):
  for i in range(1,10):
      if i<x:
        stop
        driver.find_element(By.XPATH, "//body/div[4]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[9]/a[1]").click()
        time.sleep(8)


#driver.execute_script("window.scrollTo(0, 1200)")


driver.get("https://shopstar.pe/tecnologia/televisores")
driver.maximize_window()

time.sleep(8)
clicking(1,2)
print(" esta es la segunda pagina")
clicking(1,3)
print(" esta es la pagina 3")
clicking(1,4)
print(" esta es la pagina 4")
clicking(1,5)
print(" esta es la pagina 5")
clicking(1,6)
print(" esta es la  pagina 6")
clicking(1,7)
print(" esta es la  pagina 7")
clicking(1,8)
print(" esta es la  pagina 8")
clicking(1,9)
print(" esta es la  pagina 9")

