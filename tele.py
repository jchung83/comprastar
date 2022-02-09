from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By 
#import Data_reader
import demo1

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome("D:\\GIT\\SMC\\chromedriver.exe",options=option)
from demo1 import *

num =[]
for i in  range (2,51):
    
    url= "https://www.oechsle.pe/tecnologia/?&optionOrderBy=OrderByScoreDESC&optionOrderBy=OrderByScoreDESC&O=OrderByScoreDESC&optionOrderBy=OrderByScoreDESC&page="+str(i)
    num.append(url)


#print(num) 

list =["https://shopstar.pe/tecnologia/televisores"]
      # "https://www.oechsle.pe/tecnologia/?&optionOrderBy=OrderByScoreDESC&optionOrderBy=OrderByScoreDESC&O=OrderByScoreDESC&optionOrderBy=OrderByScoreDESC&page=3"]
#list =  num
print(list)




for idx, val in enumerate(list):
   
    print(idx, val)
   
    driver.get("https://shopstar.pe/tecnologia/televisores")
    #driver.get('%s' % val)
    
    print(val)
    driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

    demo1.test(driver, idx)