#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# process_tiles_to_video_ACR_OPV                                            #
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
"""

name    = "process_tiles_to_video_ACR_OPV"
version = "2015-05-09T1407Z"

import os
import time
import re
from   moviepy.editor import *

def ls_files(
    path = "."
    ):
    return([fileName for fileName in os.listdir(path) if os.path.isfile(
        os.path.join(path, fileName)
    )])

def sort_alphanumeric(
    unsortedList = None
    ): 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanumericKey = lambda key: [
        convert(c) for c in re.split('([0-9]+)', key)
    ]
    return(sorted(unsortedList, key = alphanumericKey))

def main():

    listOfFiles = ls_files()
    listOfTileImageFiles = [fileName for fileName in listOfFiles \
        if "_tile.png" in fileName
    ]
    listOfTileImageFiles = sort_alphanumeric(listOfTileImageFiles)
    #numberOfTiledImages = len(listOfTileImageFiles)

    video = ImageSequenceClip(listOfTileImageFiles, fps = 20)

    ## no sound and low quality:
    #video.write_videofile(
    #    "video.mp4",
    #    fps         = 10,
    #    codec       = "mpeg4",
    #    audio_codec = "libvorbis"
    #)

    ## sound and high quality:
    #soundTrack = AudioFileClip("soundtrack.wav")
    #video = video.set_audio(soundTrack)
    video.write_videofile(
        "video.avi",
        fps         = 10,
        codec       = "png",
        audio       = False#True
    )

if __name__ == "__main__":
    main()
