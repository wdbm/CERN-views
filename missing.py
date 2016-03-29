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

usage:
    program [options]

options:
    -h, --help      display help message
    --version       display version and exit
    --report=BOOL   report on missing information [default: true]
    --address=BOOL  address missing information   [default: false]
"""

name    = "missing"
version = "2016-03-29T1219Z"

import docopt
import os
import time

import shijian

def main(options):

    # access options and arguments
    engage_report  = shijian.string_to_bool(options["--report"])
    engage_address = shijian.string_to_bool(options["--address"])

    list_of_files = shijian.ls_files()
    list_of_image_files = [filename for filename in list_of_files \
        if ".png" in filename
    ]
    list_of_LHC1_image_files = [filename for filename in list_of_image_files \
        if "LHC1" in filename
    ]
    list_of_timestamps = [
        filename.split("_")[0] for filename in list_of_LHC1_image_files
    ]
    list_of_timestamps_ordered       = sorted(list_of_timestamps)
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
            "{timestamp}_LHC2.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_LHC3.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_LHC_BSRT.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_LHC_CTF3.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_LHC_dashboard.png".format(
                timestamp = list_of_timestamps_ordered[index]
            ),
            "{timestamp}_LHC_dashboard-hd.png".format(
                timestamp = list_of_timestamps_ordered[index]
            )
        ]
        for filename in list_of_file_classifications:
            if not os.path.isfile(filename):
                if engage_report and not engage_address:
                    print("expected file nonexistent: {filename}".format(
                        filename = filename
                    ))
                if engage_report and engage_address:
                    print("expected file nonexistent, creating blank: {filename}".format(
                        filename = filename
                    ))
                    if "ACR01" in filename:
                        command = "cp blank_ACR01.png {filename}"
                        os.system(command.format(filename = filename))
                    if "ACR02" in filename:
                        command = "cp blank_ACR02.png {filename}"
                        os.system(command.format(filename = filename))
                    if "Atlantis" in filename:
                        command = "cp blank_Atlantis.png {filename}"
                        os.system(command.format(filename = filename))
                    if "LHC1" in filename:
                        command = "cp blank_LHC1.png {filename}"
                        os.system(command.format(filename = filename))
                    if "LHC2" in filename:
                        command = "cp blank_LHC2.png {filename}"
                        os.system(command.format(filename = filename))
                    if "LHC3" in filename:
                        command = "cp blank_LHC3.png {filename}"
                        os.system(command.format(filename = filename))
                    if "LHC_BSRT" in filename:
                        command = "cp blank_LHC_BSRT.png {filename}"
                        os.system(command.format(filename = filename))
                    if "LHC_CTF3" in filename:
                        command = "cp blank_LHC_CTF3.png {filename}"
                        os.system(command.format(filename = filename))
                    if "LHC_dashboard" in filename:
                        command = "cp blank_LHC_dashboard.png {filename}"
                        os.system(command.format(filename = filename))
                    if "LHC_dashboard-hd" in filename:
                        command = "cp blank_LHC_dashboard-hd.png {filename}"
                        os.system(command.format(filename = filename))

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
