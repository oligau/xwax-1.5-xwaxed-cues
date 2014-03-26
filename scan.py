#!/usr/bin/python3

import taglib

import os, re, sys
from os.path import join, getsize

cre = re.compile('\.(ogg|oga|aac|cdaudio|mp3|flac|wav|aif|aiff|m4a|wma)$', flags=re.I)

for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        if cre.search(name):
            f = taglib.File(join(root, name))
            print(join(root,name), 
                [d for d in f.tags.get("ARTIST", "")], 
                [d for d in f.tags.get("TITLE", "")], 
                f.tags.get("BPM", "0"), sep='\t')
