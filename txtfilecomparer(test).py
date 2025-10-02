#!/usr/bin/env python3


import os
import sys
import fileinput

def read_file(file_path):
    open("D:\\myfiles\welcome.txt", "r")
    with open (file_path,'r') as file:
        lines=file.readlines()
    
    quoted_lines=[]
    for line in lines:
        parts=line.split('=')
        if len(parts)==2:
            if not (parts[1].startswith('"')and parts[1].endswith('"')):
                quoted_lines.append(f'{parts[0]}="{parts[1].strip()}"')
        else:
            quoted_lines.append(line)
    
    quoted_contents='\n'.join(quoted_lines)
    
    with open (file_path,'w') as file:
        file.write(quoted_contents)
    
read_file("Dokumente\ext_file.txt")
    
    
    
    