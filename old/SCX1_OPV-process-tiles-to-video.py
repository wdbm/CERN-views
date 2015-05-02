#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# SCX1_OPV-process-tiles-to-video                                              #
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

name    = "SCX1_OPV-process-tiles-to-video"
version = "2015-05-01T2010Z"

import smuggle
import os
import time
from   moviepy.editor import *
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
    listOfTileImageFiles = [fileName for fileName in listOfFiles \
        if "_tile.png" in fileName
    ]
    numberOfTiledImages = len(listOfTileImageFiles)

    # Create a video clip for each image.
    videoClips = []
    imageDurations = []
    for imageNumber in range(0, numberOfTiledImages):
        imageImageFileName = str(imageNumber) + "_tile.png"
        imageClip = ImageClip(imageImageFileName)
        duration  = 0.1
        videoClip = imageClip.set_duration(duration)
        # Determine the image start time by calculating the sum of the durations
        # of all previous images.
        if imageNumber != 0:
            videoStartTime = sum(imageDurations[0:imageNumber])
        else:
            videoStartTime = 0
        videoClip = videoClip.set_start(videoStartTime)
        videoClips.append(videoClip)
        imageDurations.append(duration)
    fullDuration = sum(imageDurations)
    video = concatenate(videoClips)
    video.write_videofile(
        "video.mp4",
        fps         = 30,
        codec       = "mpeg4",
        audio_codec = "libvorbis"
    )

if __name__ == "__main__":
    main()
