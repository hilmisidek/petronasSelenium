# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:47:54 2021

@author: hilmisidek@hotmail.com
"""

import pytest
from selenium import webdriver
import unittest
#from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#from datetime import date
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

Query=input("insert search query")
browser = webdriver.Chrome()  # using chrome
browser.get("https://www.petronas.com")

def test_petronas_title():
    #browser = webdriver.Chrome()  # using chrome
    #browser.get("https://www.petronas.com")

    tajuk = browser.title.lower()
    tajuko=tajuk.split(" ")
    print (tajuko)
   # assert(tajuk.startswith("petronas"))
    assert "petronas" in tajuko

def test_petronas_search():
    # browser = webdriver.Chrome()  # using chrome
    # browser.get("https://www.petronas.com")

    searhBtn=browser.find_element(By.XPATH,"//*[@id='page']/div[2]/div/div[2]/div[2]/div/div/button")
    searhBtn.click()
    query=browser.find_element(By.NAME,"search_query")
    query.send_keys(Query)
    browser.find_element(By.XPATH,"// *[ @ id = 'searchoverlay'] / div / div / div[2] / div / div / div / form / div "
                                  "/ div / input").click()

   # result=browser.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[2]/section/div[2]/div/div[3]/div/div/div/div/div/div/div[1]/a[1]/div/h3")
    result=browser.find_elements(By.CSS_SELECTOR,"#st-results-container > a")
    lengt=len(result)
    print (f"\nlength of result is {lengt}")
    #i=0
    for i in result:
        print (i.text + "\n")
        #tester=[]
        tester=i.text.lower().split(" ")
        assert Query in tester
        print (f"\n{Query} count in snippet :")
        print (tester.count(Query))
        print ("\n")
    browser.close()
   # print (result.len())

    #    assertIn
    #assertEqual()




