#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# https://github.com/bookfere/BookFere-Tools/blob/dc855679e8badb243050357831c19292d71c966e/bookfere-tools/bin/sdr-cleaner/sdr_cleaner.py

import glob
import os
import re
import shutil
import sys

from functools import reduce
from pathlib import Path


# Process
def onProcess(kindlePath):
    documentsPath = kindlePath + "/documents"

    if not os.path.exists(documentsPath):
        return

    list_dirs = os.walk(documentsPath)

    # Clean SDR Folder
    for root, dirs, files in list_dirs:
        if dirs:
            os.chdir(root)

            sdr = glob.glob(r"*.sdr")
            # todo: use set
            documents = reduce(
                lambda a, ext: a + glob.glob(r"*." + ext),
                [
                    "azw",
                    "azw3",
                    "pdf",
                    "txt",
                    "prc",
                    "mobi",
                    "pobi",
                    "epub",
                    "azw4",
                    "kfs",
                    "kfx",
                ],
                [],
            )
            format_sdr = False

            for sdr_folder in sdr:
                found = False
                for document in documents:
                    if Path(document).stem == Path(sdr_folder).stem:
                        found = True
                        break
                if not found:
                    print("Remove {}".format(sdr_folder))
                    shutil.rmtree(sdr_folder)
                break


# Execute
if __name__ == "__main__":
    onProcess(os.path.dirname(os.path.realpath(__file__)))
