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
version = "2016-03-25T1049Z"

import smuggle
import os
import time
import shijian

def ls_files(
    path = "."
    ):
    return([filename for filename in os.listdir(path) if os.path.isfile(
        os.path.join(path, filename)
    )])

def main():

    list_of_files = ls_files()
    list_of_image_files = [filename for filename in list_of_files \
        if ".png" in filename
    ]
    list_of_ACR01_image_files = [filename for filename in list_of_image_files \
        if "ACR01" in filename
    ]
    list_of_timestamps = [
        filename.split("_")[0] for filename in list_of_ACR01_image_files
    ]
    list_of_timestamps_ordered = sorted(list_of_timestamps)
    number_of_tiled_images_to_create = len(list_of_timestamps)

    for index in range(0, number_of_tiled_images_to_create):
        list_of_file_classifications = [
            "{timestamp}_ACR01.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_ACR02.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_Atlantis.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_LHC1.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_LHC_dashboard.png".format(
                timestamp = list_of_timestamps_ordered[index]
            )
        ]
        for filename in list_of_file_classifications:
            if not os.path.isfile(filename):
                print("expected file nonexistent, creating blank: {filename}".format(
                    filename = filename
                ))
                if "ACR01" in filename:
                    command = "cp blank_ACR01.png {filename}"
                if "ACR02" in filename:
                    command = "cp blank_ACR02.png {filename}"
                if "Atlantis" in filename:
                    command = "cp blank_Atlantis.png {filename}"
                if "LHC1" in filename:
                    command = "cp blank_LHC1.png {filename}"
                if "LHC_dashboard" in filename:
                    command = "cp blank_LHC_dashboard.png {filename}"
                os.system(command.format(filename = filename))

if __name__ == "__main__":
    main()
