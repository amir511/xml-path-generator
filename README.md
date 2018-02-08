# xml-path-generator
A very handy small script utilizing the lxml python library in order to quickly get the xpath of any element 
in an xml tree
Will save you a lot of precious time when you are inheriting Odoo modules, As xml views inheritance heavily depends on xpath insertion.
usage: create 'xml_file.xml' file in the same directory and paste the xml tree
put a tag <here/> in the  place you wish to get the xpath
run the script, you will notice the here tag xpath is highlighted in red
* Dependencies:
    colorama
    termcolor
