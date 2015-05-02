#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# SCX1_OPVLHC1-view-3                                                          #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a way of recording views of the ATLAS Control Room and OP    #
# Vistars pages for a certain time period.                                     #
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

name    = "SCX1_OPVLHC1-view-3"
version = "2015-05-01T1641Z"

import smuggle
import urllib
import imp
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
shijian = smuggle.smuggle(
    moduleName = "shijian",
    URL = "https://rawgit.com/wdbm/shijian/master/shijian.py"
)

def main():

    URL_ACR   = "https://atlasop.cern.ch/ATLASview/ACR.htm"
    URL_ACR01 = "https://atlasop.cern.ch/ATLASview/webpic/ACR01.jpg"
    URL_ACR02 = "https://atlasop.cern.ch/ATLASview/webpic/ACR02.jpg"
    URL_LHC1  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc1.png"
    URL_LHC2  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc2.png"
    URL_LHC3  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc3.png"
    URL_LHC_dashboard = "http://lhcdashboard-images.web.cern.ch/" + \
        "lhcdashboard-images/images/lhc/prod/dashboard.png"
    URL_LHC_dashboard_hd = "http://lhcdashboard-images.web.cern.ch/" + \
        "lhcdashboard-images/images/lhc/prod/dashboard-hd.png"

    driver = webdriver.Firefox()

    driver.get(URL_ACR)

    raw_input("Log into CERN and then press Enter to continue.")

    timeToRunInSeconds = 28000 # 8 hours
    clock = shijian.Clock(name = "clock")

    while clock.time() <= timeToRunInSeconds:

        timestamp = str(shijian.time_UNIX())

        # access ACR
        
        driver.set_window_size(801, 674)
        
        driver.get(URL_ACR01)
        driver.save_screenshot(shijian.proposeFileName(
            fileName = timestamp + "_ACR01.png"
        ))

        driver.get(URL_ACR02)
        driver.save_screenshot(shijian.proposeFileName(
            fileName = timestamp + "_ACR02.png"
        ))

        # access LHC

        urllib.urlretrieve(
            URL_LHC1,
            shijian.proposeFileName(
                fileName = timestamp + "_LHC1.png"
            )
        )

        urllib.urlretrieve(
            URL_LHC2,
            shijian.proposeFileName(
                fileName = timestamp + "_LHC2.png"
            )
        )

        urllib.urlretrieve(
            URL_LHC3,
            shijian.proposeFileName(
                fileName = timestamp + "_LHC3.png"
            )
        )

        urllib.urlretrieve(
            URL_LHC_dashboard,
            shijian.proposeFileName(
                fileName = timestamp + "_LHC_dashboard.png"
            )
        )

        urllib.urlretrieve(
            URL_LHC_dashboard_hd,
            shijian.proposeFileName(
                fileName = timestamp + "_LHC_dashboard-hd.png"
            )
        )

        time.sleep(60)

    driver.close()

if __name__ == "__main__":
    main()
