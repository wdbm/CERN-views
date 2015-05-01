#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# SCX1_OPVLHC1-process-2                                                       #
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

name    = "SCX1_OPVLHC1-process-2"
version = "2015-05-01T1045Z"

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
    
    # Create tile images.
    raw_input("Press Enter to create tile images.")
    for index in range(0, numberOfTiledImagesToCreate):
        commandTile = \
            "montage " + \
            "logo.png " + \
            "{timestamp}_ACR02.png " + \
            "{timestamp}_ACR01.png " + \
            "{timestamp}_LHC1.png "  + \
            "{timestamp}_LHC_dashboard.png " + \
            "null: " + \
            "-mode Concatenate " + \
            "-tile 3x3 " + \
            "{index}_tile.png"
        commandTile = commandTile.format(
            timestamp = listOfTimestampsOrdered[index],
            index     = index
        )
        print(commandTile)
        os.system(commandTile)

    # Create animation of tile images.
    commandAnimation = \
        "convert -layers optimize -delay 35 -loop 0 *_tile.png " + \
        "{fileBaseName}.gif"
    commandAnimation = commandAnimation.format(
        fileBaseName = shijian.time_UTC() + "_animation"
    )
    raw_input("Press Enter to create animation.")
    os.system(commandAnimation)

if __name__ == "__main__":
    main()
