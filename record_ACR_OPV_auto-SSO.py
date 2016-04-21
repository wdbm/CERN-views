#!/usr/bin/env python

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

usage:
    program [options]

options:
    -h, --help     display help message
    --version      display version and exit
    -v, --verbose  verbose logging
"""

from __future__ import print_function

name    = "record_ACR_OPV_auto-SSO"
version = "2016-04-21T0959Z"

import docopt
import getpass
import imp
import os
import retrying
import urllib
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import shijian

URL_login  = "https://login.cern.ch"

URL_ACR                   = "https://atlasop.cern.ch/ATLASview/ACR.htm"
URL_ACR01                 = "https://atlasop.cern.ch/ATLASview/webpic/ACR01.jpg"
URL_ACR02                 = "https://atlasop.cern.ch/ATLASview/webpic/ACR02.jpg"
URL_ATLAS_detector_status = "https://atlasop.cern.ch/overview/dcs/snapshots/ATLAS.png"
URL_Atlantis              = "https://atlas-live.cern.ch/event_files/MinBias/latest.png"
URL_LHC1                  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc1.png"
URL_LHC2                  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc2.png"
URL_LHC3                  = "http://vistar-capture.web.cern.ch/vistar-capture/lhc3.png"
URL_LHC_dashboard         = "http://lhcdashboard-images.web.cern.ch/lhcdashboard-images/images/lhc/prod/dashboard.png"
URL_LHC_dashboard_hd      = "http://lhcdashboard-images.web.cern.ch/lhcdashboard-images/images/lhc/prod/dashboard-hd.png"
URL_LHC_BSRT              = "http://cs-ccr-www3.cern.ch/vistar_capture/lhcbsrt.png"
URL_LHC_CTF3              = "http://cs-ccr-www3.cern.ch/vistar_capture/ctfgen.png"

URL_OD01                  = "https://atlasop.cern.ch/ATLASview/webpic/OD01.jpg"
URL_OD02                  = "https://atlasop.cern.ch/ATLASview/webpic/OD02.jpg"
URL_UX15SideA02HD         = "https://atlasop.cern.ch/ATLASview/webpic/UX15SideA02HD.jpg"
URL_UX15SideA04HD         = "https://atlasop.cern.ch/ATLASview/webpic/UX15SideA04HD.jpg"
URL_UX15SideC01HD         = "https://atlasop.cern.ch/ATLASview/webpic/UX15SideC01HD.jpg"
URL_UX15SideC03HD         = "https://atlasop.cern.ch/ATLASview/webpic/UX15SideC03HD.jpg"
URL_SX1HD01               = "https://atlasop.cern.ch/ATLASview/webpic/SX1HD01.jpg"

def main(options):

    verbose = options["--verbose"]

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

            print("\rtake snapshot")

            timestamp = str(shijian.time_UNIX())

            # access ACR

            save_screenshot(
                URL         = URL_ACR01,
                window_size = (801, 674),
                filename    = timestamp + "_ACR01.png"
            )

            save_screenshot(
                URL         = URL_ACR02,
                window_size = (801, 674),
                filename    = timestamp + "_ACR02.png"
            )

            # access LHC

            retrieve_from_URL(
                URL      = URL_LHC1,
                filename = timestamp + "_LHC1.png"
            )

            retrieve_from_URL(
                URL      = URL_LHC2,
                filename = timestamp + "_LHC2.png"
            )

            retrieve_from_URL(
                URL      = URL_LHC3,
                filename = timestamp + "_LHC3.png"
            )

            retrieve_from_URL(
                URL      = URL_LHC_dashboard,
                filename = timestamp + "_LHC_dashboard.png"
            )

            retrieve_from_URL(
                URL      = URL_LHC_dashboard_hd,
                filename = timestamp + "_LHC_dashboard-hd.png"
            )

            retrieve_from_URL(
                URL      = URL_LHC_BSRT,
                filename = timestamp + "_LHC_BSRT.png"
            )

            retrieve_from_URL(
                URL      = URL_LHC_CTF3,
                filename = timestamp + "_LHC_CTF3.png"
            )

            # access ATLAS detector status

            save_screenshot(
                URL         = URL_ATLAS_detector_status,
                window_size = (865, 942),
                filename    = timestamp + "_ATLAS_detector_status.png"
            )

            # access Atlantis

            save_screenshot(
                URL         = URL_Atlantis,
                window_size = (933, 800),
                filename    = timestamp + "_Atlantis.png"
            )

            clock_snapshot_duration.reset()
            clock_snapshot_duration.start()

        else:

            print("\rtime to next snapshot: {time_to_next_snapshot} s".format(
                time_to_next_snapshot =\
                    snapshot_duration_in_seconds -\
                    int(clock_snapshot_duration.time()
                )
            ))
            time.sleep(1)

    driver.close()

def authenticate():

    print("authenticate")

    driver.get(URL_login)

    time.sleep(6)

    if "authentication" in driver.title.lower() and "management" not in driver.title.lower():

        input_login = driver.find_element_by_name("ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$txtFormsLogin")
        input_login.send_keys(identification)

        input_passcode = driver.find_element_by_name("ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$txtFormsPassword")
        input_passcode.send_keys(passcode)
        input_passcode.send_keys(Keys.RETURN)

    time.sleep(3)

def retrieve_from_URL(
    URL      = None,
    filename = None
    ):

    code = retrying.retry(
        lambda: (
            print("access {URL}".format(URL = URL)),
            urllib.urlretrieve(
                URL,
                shijian.propose_filename(
                    filename = filename
                )
            )
        ),
        stop_max_delay = 10000 # 10 s
    ); code()

def save_screenshot(
    URL         = None,
    window_size = None,
    filename    = None
    ):

    driver.set_window_size(window_size[0], window_size[1])
    code = retrying.retry(
        lambda: (
            print("access {URL}".format(URL = URL)),
            driver.get(URL),
            time.sleep(2),
            driver.save_screenshot(shijian.propose_filename(
                filename = filename
            ))
        ),
        stop_max_delay = 10000 # 10 s
    ); code()

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
