#!/usr/bin/env python
from __future__ import print_function
"""
################################################################################
#                                                                              #
# record_ACR_OPV_auto-SSO                                                      #
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

name    = "record_ACR_OPV_auto-SSO"
version = "2015-06-03T1146Z"

import smuggle
import urllib
import imp
import os
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
shijian = smuggle.smuggle(
    moduleName = "shijian",
    URL = "https://rawgit.com/wdbm/shijian/master/shijian.py"
)

URLlogin  = "https://login.cern.ch"

URL_ACR   = "https://atlasop.cern.ch/ATLASview/ACR.htm"
URL_ACR01 = "https://atlasop.cern.ch/ATLASview/webpic/ACR01.jpg"
URL_ACR02 = "https://atlasop.cern.ch/ATLASview/webpic/ACR02.jpg"
URL_ATLAS_detector_status = \
    "https://atlasop.cern.ch/overview/dcs/snapshots/ATLAS.png"
URL_Atlantis = "https://atlas-live.cern.ch/event_files/MinBias/latest.png"
URL_LHC1  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc1.png"
URL_LHC2  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc2.png"
URL_LHC3  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc3.png"
URL_LHC_dashboard = "http://lhcdashboard-images.web.cern.ch/" + \
    "lhcdashboard-images/images/lhc/prod/dashboard.png"
URL_LHC_dashboard_hd = "http://lhcdashboard-images.web.cern.ch/" + \
    "lhcdashboard-images/images/lhc/prod/dashboard-hd.png"
URL_LHC_BSRT = "http://cs-ccr-www3.cern.ch/vistar_capture/lhcbsrt.png"
URL_LHC_CTF3 = "http://cs-ccr-www3.cern.ch/vistar_capture/ctfgen.png"

def main():

    print("\n" + name + "\n")

    global identification
    global passcode

    identification = getpass.getpass(prompt = "enter username: ")
    passcode       = getpass.getpass(prompt = "enter passcode: ")

    global driver

    driver = webdriver.Firefox()

    authenticate()

    # Create clocks, one to define the total recording time, another to define
    # the duration between running authentication procedures and another to
    # define the time between recording "snapshots".

    recording_duration_in_seconds      = 604800 # 1 week
    authentication_duration_in_seconds = 600    # 10 minutes
    snapshot_duration_in_seconds       = 60     # 1 minute

    clock_recording_duration = shijian.Clock(
        name = "recording duration"
    )
    clock_authentication_duration = shijian.Clock(
        name = "authentication duration"
    )
    clock_snapshot_duration = shijian.Clock(
        name = "snapshot duration"
    )

    print("start recording -- Ctrl C to stop")

    while clock_recording_duration.time() <= recording_duration_in_seconds:

        if clock_authentication_duration.time() > authentication_duration_in_seconds:
            authenticate()
            clock_authentication_duration.reset()
            clock_authentication_duration.start()

        if clock_snapshot_duration.time() >= snapshot_duration_in_seconds:

            print("\rtake snapshot", end = "")

            timestamp = str(shijian.time_UNIX())

            # access ACR

            driver.set_window_size(801, 674)

            driver.get(URL_ACR01)
            time.sleep(2)
            driver.save_screenshot(shijian.proposeFileName(
                fileName = timestamp + "_ACR01.png"
            ))

            driver.get(URL_ACR02)
            time.sleep(2)
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

            urllib.urlretrieve(
                URL_LHC_BSRT,
                shijian.proposeFileName(
                    fileName = timestamp + "_LHC_BSRT.png"
                )
            )

            urllib.urlretrieve(
                URL_LHC_CTF3,
                shijian.proposeFileName(
                    fileName = timestamp + "_LHC_CTF3.png"
                )
            )

            # access ATLAS detector status

            driver.set_window_size(865, 942)

            driver.get(URL_ATLAS_detector_status)
            time.sleep(2)
            driver.save_screenshot(shijian.proposeFileName(
                fileName = timestamp + "_ATLAS_detector_status.png"
            ))

            # access Atlantis

            driver.set_window_size(933, 800)

            driver.get(URL_Atlantis)
            time.sleep(2)
            driver.save_screenshot(shijian.proposeFileName(
                fileName = timestamp + "_Atlantis.png"
            ))

            clock_snapshot_duration.reset()
            clock_snapshot_duration.start()

        else:

            print("\rtime to next snapshot: {timeToNextSnapshot} s".format(
                timeToNextSnapshot =\
                    snapshot_duration_in_seconds -\
                    int(clock_snapshot_duration.time()
                ),
                end = "")
            )
            time.sleep(1)

    driver.close()

def authenticate():

    print("authenticate")

    driver.get(URLlogin)

    time.sleep(6)

    if "authentication" in driver.title.lower() and "management" not in driver.title.lower():

        inputLogin = driver.find_element_by_name("ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$txtFormsLogin")
        inputLogin.send_keys(identification)

        inputPasscode = driver.find_element_by_name("ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$txtFormsPassword")
        inputPasscode.send_keys(passcode)
        inputPasscode.send_keys(Keys.RETURN)

    time.sleep(3)

if __name__ == "__main__":
    main()
