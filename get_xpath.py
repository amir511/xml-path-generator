#! /usr/bin/python
"""
Small script utilizing the lxml python library in order to quickly get the xpath of any element 
in an xml tree

usage: open the xml_file.xml file and paste the xml tree
put a tag <here/> in the  place you wish to get the xpath
run the script, you will notice the here tag is highlighted in red
author: amir anwar 30/10/2017
"""
from lxml import etree
import colorama
from termcolor import cprint
colorama.__init__

def iterate_tree(xml_tree):
    for i in xml_tree.iter():
        path = i.getroottree().getpath(i)
        if 'here' in path:
            cprint(path,'white','on_red')
        else:
            print path

with open('xml_file.xml','r') as f:
    xml_string = f.read()

try:
    xml_tree = etree.fromstring(xml_string)
    iterate_tree(xml_tree)
except:
    cprint('error!, please check the xml_file contents','white','on_red')



input('Script Finished, press enter to close window')