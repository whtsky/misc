#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import glob
import os
import re
import shutil
import sys

from functools import reduce
from pathlib import Path


# Process
def process_dir(documents_path: Path):
    if not documents_path.exists():
        return

    documents = reduce(
        lambda a, ext: a + list(documents_path.glob("*." + ext)),
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
    for sdr_folder in documents_path.glob("*.sdr"):
        found = False
        for document in documents:
            if document.stem == sdr_folder.stem:
                found = True
        if not found:
            print("Remove {}".format(sdr_folder))
            shutil.rmtree(sdr_folder)
    for sub_path in documents_path.iterdir():
        if sub_path.is_dir():
            process_dir(sub_path)


# Execute
if __name__ == "__main__":
    process_dir(Path(__file__).parent / "documents")
