#
'''
This tool is designed to 
1. Take in a list of CXIDs
2. Check these via Charters validation tool to see if they have been previously validated
3. return a list of validated and unvalidated cxids
'''


'''
REMEMBER TO INSERT SOMETHING TO HANDLE 'No Clients Found'
'''

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# GLOBAL VARIABLES
cxidURL = 'https://main.cxid.spectrumtoolbox.com/'
'''
These are the XPaths/Classnames/IDs of all the relevant elements of the site such as the search bar, expand arrow, CXID name, etc.
If the dev team makes changes to the CXID tool it may be necessary to reassign these VARIABLES
You can find Xpath/Classname/etc. via the Google Chrome inspector tool
'''
# Select the whole CXID container
cxidDivXPath = '/html/body/cxi-root/ng-component/div/main/cxi-card-container/div/div/section/cxi-card/ngk-card/div'
# This is only the section where CXID &  CXID Name is
cxidNameAndNumberSectionClassName = 'cxid-label-wrapper'
# Expand Arrow button
cxidExpandArrowClassName = 'main-chevron-utility-container'
# Just the text in each site
cxidSitePClassName = 'site-title'
#Search Bar
searchBarId = 'search'
#State Search
stateSearchBarXPath = '/html/body/cxi-root/ng-component/div/main/header/cxi-context-bar/div/div[1]/form/input[2]'
#validated text
validatedXpath = '/html/body/cxi-root/ng-component/div/main/cxi-card-container/div/div/section/cxi-card/ngk-card/div/div[2]/div[1]/section[2]/p'
'''
this is the path to the validated 
'''



cxid_list = []
while 1:
    user_input = input("Input an element (type stop when finished): ")
    if user_input == "stop":
        break
    cxid_list.append(user_input)






def BrowserSetup(numOfTabs):
    '''
    Initialize browser
    @Returns driver, cxidTab, nameTab, addressTabs
    '''
    # Chrome options to keep browser open
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # Attempt to get rid of errors in terminal
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    # chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Open Browser, goto CXID Tool
    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    driver.get(cxidURL)
    time.sleep(1)

    # Open search tab, go to CXID Tool
    
    driver.execute_script(f"window.open('{cxidURL}');")

    # Assigning each open tab to its own variable for easy access
    cxidTab = driver.window_handles[0]

    return driver, cxidTab

def SearchCXID(driver):
    '''
    Search CXID in first tab
    '''
    # We ask for input here so we can recurse the function if CXID does not load
    cxidNumberInput = cxid_list

    #Switch Tab
    driver.switch_to.window(cxidTab)

    #Search the Data
    elem = driver.find_element_by_id(searchBarId)
    elem.clear()
    elem.send_keys(f'{cxidNumberInput}')
    elem.send_keys(Keys.RETURN)
    time.sleep(0.5)

    # Wait for CXID element to pop up
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, cxidDivXPath)))

    # If CXID doesnt show up, recurse
    except:
        cxidNumberInput = SearchCXID(driver)

    # Click on expand arrow
    expandArrowElement = driver.find_element_by_class_name(cxidExpandArrowClassName)
    expandArrowElement.click()
    time.sleep(0.5)


if __name__ == "__main__":
    while True:


        for cxid in cxid_list:

        if validatedElem == True





#tells the script to find the validated text within tool 
validatedElem = driver.find_element_by_xpath(validatedXpath)


#print(cxid_list)



#other ideas   
    #pull names as well for new xcids to be pasted onto smartsheet
