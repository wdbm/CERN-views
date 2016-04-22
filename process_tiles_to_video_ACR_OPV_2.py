#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# process_tiles_to_video_ACR_OPV_2                                             #
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

name    = "process_tiles_to_video_ACR_OPV_2"
version = "2016-04-22T1215Z"

import os
import time
import re
from   moviepy.editor import *

def main():

    list_of_files = shijian.ls_files()
    list_of_tile_image_files = [filename for filename in list_of_files \
        if "_tile.png" in filename
    ]
    list_of_tile_image_files = shijian.natural_sort(list_of_tile_image_files)
    number_of_tiled_images = len(list_of_tile_image_files)

    list_of_tile_image_files = list_of_tile_image_files[:number_of_tiled_images - 2]
    #for image in list_of_tile_image_files:
    #    print(image)

    video = ImageSequenceClip(list_of_tile_image_files, fps = 10)

    #raw_input("Press Enter to write video.")

    ## no sound and low quality:
    #video.write_videofile(
    #    "video.mp4",
    #    fps         = 10,
    #    codec       = "mpeg4",
    #    audio_codec = "libvorbis"
    #)

    ## sound and high quality:
    #sound_track = AudioFileClip("sound_track.wav")
    #video = video.set_audio(sound_track)
    video.write_videofile(
        "video.avi",
        fps   = 10,
        codec = "png",
        audio = False #True
    )

if __name__ == "__main__":
    main()
