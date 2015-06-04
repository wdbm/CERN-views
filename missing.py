#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# missing                                                                      #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a way of assessing and addressing missing data.              #
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

name    = "missing"
version = "2015-06-03T1357Z"

import smuggle
import os
import time
shijian = smuggle.smuggle(
    moduleName = "shijian",
    URL = "https://rawgit.com/wdbm/shijian/master/shijian.py"
)

def ls_files(
    path = "."
    ):
    return([fileName for fileName in os.listdir(path) if os.path.isfile(
        os.path.join(path, fileName)
    )])

def main():

    listOfFiles = ls_files()
    listOfImageFiles = [fileName for fileName in listOfFiles \
        if ".png" in fileName
    ]
    listOfACR01ImageFiles = [fileName for fileName in listOfImageFiles \
        if "ACR01" in fileName
    ]
    listOfTimestamps = [
        fileName.split("_")[0] for fileName in listOfACR01ImageFiles
    ]
    listOfTimestampsOrdered = sorted(listOfTimestamps)
    numberOfTiledImagesToCreate = len(listOfTimestamps)

    for index in range(0, numberOfTiledImagesToCreate):
        listOfFileClassifications = [
            "{timestamp}_ACR01.png".format(
                timestamp = listOfTimestampsOrdered[index]
            ),
            "{timestamp}_ACR02.png".format(
                timestamp = listOfTimestampsOrdered[index]
            ),
            "{timestamp}_Atlantis.png".format(
                timestamp = listOfTimestampsOrdered[index]
            ),
            "{timestamp}_LHC1.png".format(
                timestamp = listOfTimestampsOrdered[index]
            ),
            "{timestamp}_LHC_dashboard.png".format(
                timestamp = listOfTimestampsOrdered[index]
            )
        ]
        for fileName in listOfFileClassifications:
            if not os.path.isfile(fileName):
                print("expected file nonexistent, creating blank: {fileName}".format(
                    fileName = fileName
                ))
                if "ACR01" in fileName:
                    command = "cp blank_ACR01.png {fileName}"
                if "ACR02" in fileName:
                    command = "cp blank_ACR02.png {fileName}"
                if "Atlantis" in fileName:
                    command = "cp blank_Atlantis.png {fileName}"
                if "LHC1" in fileName:
                    command = "cp blank_LHC1.png {fileName}"
                if "LHC_dashboard" in fileName:
                    command = "cp blank_LHC_dashboard.png {fileName}"
                os.system(command.format(fileName = fileName))

if __name__ == "__main__":
    main()
