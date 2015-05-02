#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# SCX1_OPVLHC1-view-1                                                          #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a way of recording views of the ATLAS Control Room and OP    #
# Vistars pages.                                                               #
#                                                                              #
# copyright (C) 2015 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

name    = "SCX1_OPVLHC1-view-1"
version = "2015-04-07T2245Z"

def smuggle(
    moduleName = None,
    URL        = None
    ):
    if moduleName is None:
        moduleName = URL
    try:
        module = __import__(moduleName)
        return(module)
    except:
        try:
            moduleString = urllib.urlopen(URL).read()
            module = imp.new_module("module")
            exec moduleString in module.__dict__
            return(module)
        except: 
            raise(
                Exception(
                    "module {moduleName} import error".format(
                        moduleName = moduleName
                    )
                )
            )
            sys.exit()

import urllib
import imp
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
shijian = smuggle(
    moduleName = "shijian",
    URL = "https://rawgit.com/wdbm/shijian/master/shijian.py"
)

def main():

    URL1 = "https://atlasop.cern.ch/ATLASview/ACR.htm"
    URL2 = "https://atlasop.cern.ch/ATLASview/webpic/ACR01.jpg"
    URL3 = "https://atlasop.cern.ch/ATLASview/webpic/ACR02.jpg"
    URL4 = "http://vistar-capture.web.cern.ch/vistar-capture/lhc1.png"

    driver = webdriver.Firefox()

    driver.get(URL1)

    raw_input("Log into CERN and then press Enter to continue.")

    while True:

        #driver.get(URL1)
        #img = driver.find_element_by_xpath("/html/body/div[1]/img[1]")
        #src = img.get_attribute("src")
        #driver.get(src)
        #driver.save_screenshot(shijian.proposeFileName(fileName = "ACR01.png"))

        driver.get(URL2)
        driver.save_screenshot(shijian.proposeFileName(fileName = "ACR01.png"))

        driver.get(URL3)
        driver.save_screenshot(shijian.proposeFileName(fileName = "ACR02.png"))

        urllib.urlretrieve(
            URL4,
            shijian.proposeFileName(
                fileName = shijian.time_UTC() + "lhc1.png"
            )
        )

        time.sleep(60)

    driver.close()

if __name__ == "__main__":
    main()
