#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# SCX1-view                                                                    #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a way of recording views of the ATLAS Control Room.          #
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

name    = "SCX1-view"
version = "2015-02-27T2307Z"

import urllib
import time
import shijian

def main():

    while True:
        urllib.urlretrieve(
            "https://atlasop.cern.ch/ATLASview/webpic/ACR01.jpg",
            shijian.proposeFileName(
                fileName = shijian.time_UTC() + "_SCX1_ACR01.jpg"
            )
        )
        urllib.urlretrieve(
            "https://atlasop.cern.ch/ATLASview/webpic/ACR02.jpg",
            shijian.proposeFileName(
                fileName = shijian.time_UTC() + "_SCX1_ACR02.jpg"
            )
        )
        time.sleep(60)

if __name__ == "__main__":
    main()
