#!/usr/bin/env python3


import os
import sys
import fileinput

path=os.listdir('DEFS/')#weg zum Ordner


def add(file_path):
    encodings = ["utf-8", "utf-16", "ansi"]#Formate der Textdateien
    for encode in encodings: # hier geht er in encodings rein um die verschiedene Formate einzeln durchzugehen
        try:#wenn der richtige Format gefunden ist, dann wird die Datei bearbeitet
            with open (file_path,'r',encoding=encode) as file:
                lines=file.readlines()#liest den File ein
    
            fixed_lines = []
            for line in lines:
                if "=" in line and not line.strip().endswith('"'):
                    fixed_line = line.strip().split("=")
                    
                    if "A" in fixed_line[1]:
                        fixed_line[-1] = fixed_line[-1].strip()
                    elif "M" in fixed_line[1]:
                        fixed_line[-1] = fixed_line[-1].strip()
                    else:
                        fixed_line[-1] = '"' + fixed_line[-1] + '"'
                    fixed_line = "=".join(fixed_line)
                    fixed_lines.append(fixed_line)
                
                else:
                    fixed_lines.append(line.strip())


            
            with open(file_path, "w",encoding=encode) as file:# fügt die umschriebene Zeilen in die Datei hinzu
                file.write("\n".join(fixed_lines))
            break 
            
        except UnicodeDecodeError:
            pass
        
'''
          for line in lines:
                if "=" in line and not line.strip().endswith('"'):#die Bestimmung wenn es keine Anführungszeichen hat nach den =
                    fixed_line = line.strip().split("=")# hier wird er geteilt
                    
                    fixed_line[-1] = '"' + fixed_line[-1] + '"'
                    fixed_line = "=".join(fixed_line)
                    fixed_lines.append(fixed_line)
                
                else:
                    fixed_lines.append(line.strip())
'''
def check_Klammer(file_path):
    encodings = ["utf-8", "utf-16", "ansi"]
    for encode in encodings:
        try:
            with open (file_path,'r',encoding=encode) as file:
                lines=file.readlines()
    
            fixed_lines = []
            for line in lines:
                fixed_line = line.strip()
                open_parentheses = fixed_line.count("(")
                close_parentheses = fixed_line.count(")")
                if open_parentheses > close_parentheses:
                    fixed_line += ")" * (open_parentheses - close_parentheses)
                fixed_lines.append(fixed_line)
            
            with open(file_path, "w",encoding=encode) as file:
                file.write("\n".join(fixed_lines))


            break 
        except UnicodeDecodeError:
            pass
'''

'''      
def remove(file_path):
    encodings = ["utf-8", "utf-16", "ansi"]#Formate der Textdateien
    for encode in encodings: # hier geht er in encodings rein um die verschiedene Formate einzeln durchzugehen
        try:#wenn der richtige Format gefunden ist, dann wird die Datei bearbeitet
            with open (file_path,'r',encoding=encode) as file:
                lines=file.readlines()#liest den File ein
    
            fixed_lines = []
            for line in lines:
                if "=" in line:#die Bestimmung wenn es keine Anführungszeichen hat nach den =
                    fixed_line = line.strip().split("=")# hier wird er geteilt
                    fixed_line[-1] = fixed_line[-1].replace("'", '"')
                    fixed_line = "=".join(fixed_line)
                    fixed_lines.append(fixed_line)
                
                else:
                    fixed_lines.append(line.strip())
            
            with open(file_path, "w",encoding=encode) as file:# fügt die umschriebene Zeilen in die Datei hinzu
                file.write("\n".join(fixed_lines))
            break
            
        except UnicodeDecodeError:
            pass

for file in path:
    input = 'DEFS/'+file
    remove(input)
    check_Klammer(input)
    add(input)



