#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# process_raw_to_tiles_ACR_OPV                                                 #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a way of processing views of the ATLAS Control Room and OP   #
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

usage:
    program [options]

options:
    -h, --help                display help message
    --version                 display version and exit
    --skipexistingtiles=BOOL  skip existing tiles [default: false]
    --style1=BOOL             set style 1         [default: true]
    --style2=BOOL             set style 2         [default: false]
"""

name    = "process_raw_to_tiles_ACR_OPV"
version = "2016-03-28T1746Z"

import docopt
import os
import time

import shijian

def main(options):

    # access options and arguments
    skip_existing_tiles = shijian.string_to_bool(options["--skipexistingtiles"])
    engage_style_1      = shijian.string_to_bool(options["--style1"])
    engage_style_2      = shijian.string_to_bool(options["--style2"])

    list_of_files = shijian.ls_files()
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
    
    # Create tile images.
    raw_input("Press Enter to create tile images.")
    for index in range(0, number_of_tiled_images_to_create):
        filename_tile = "{index}_tile.png".format(index = index)
        if os.path.isfile(filename_tile) and skip_existing_tiles:
            print("skip existing file {filename}".format(
                filename = filename_tile
            ))
        else:
            print("create file {filename}".format(
                filename = filename_tile
            ))
            if engage_style_1:
                command_tile = \
                    "montage " + \
                    "logo_ATLAS_2.png " + \
                    "{timestamp}_ACR02.png " + \
                    "{timestamp}_ACR01.png " + \
                    "{timestamp}_LHC1.png "  + \
                    "{timestamp}_LHC_dashboard.png " + \
                    "null: " + \
                    "-mode Concatenate " + \
                    "-tile 3x3 " + \
                    "{index}_tile.png"
                command_tile = command_tile.format(
                    timestamp = list_of_timestamps_ordered[index],
                    index     = index
                )
                print(command_tile)
                os.system(command_tile)
            if engage_style_2:
                command_resize_ACR01 = \
                    "convert " + \
                    "-geometry x729 " + \
                    "{timestamp}_ACR01.png " + \
                    "{timestamp}_ACR01_tmp.png"
                command_resize_ACR01 = command_resize_ACR01.format(
                    timestamp = list_of_timestamps_ordered[index],
                )
                os.system(command_resize_ACR01)
                command_resize_ACR02 = \
                    "convert " + \
                    "-geometry x729 " + \
                    "{timestamp}_ACR02.png " + \
                    "{timestamp}_ACR02_tmp.png"
                command_resize_ACR02 = command_resize_ACR02.format(
                    timestamp = list_of_timestamps_ordered[index],
                )
                os.system(command_resize_ACR02)
                command_tile = \
                    "montage " + \
                    "{timestamp}_ACR02_tmp.png " + \
                    "{timestamp}_ACR01_tmp.png " + \
                    "{timestamp}_Atlantis.png " + \
                    "logo_ATLAS_3.png " + \
                    "{timestamp}_LHC1.png "  + \
                    "{timestamp}_LHC_dashboard.png " + \
                    "null: " + \
                    "-mode Concatenate " + \
                    "-tile 3x3 " + \
                    "-background black " + \
                    "{index}_tile.png"
                command_tile = command_tile.format(
                    timestamp = list_of_timestamps_ordered[index],
                    index     = index
                )
                print(command_tile)
                os.system(command_tile)

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
