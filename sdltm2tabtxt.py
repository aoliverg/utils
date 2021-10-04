import sys
import sqlite3
import xml.etree.ElementTree as etree
import codecs



sdltmfile=sys.argv[1]
tabtxt=sdltmfile.replace(".sdltm",".txt")


sortida=codecs.open(tabtxt,"w",encoding="utf-8")


conn=sqlite3.connect(sdltmfile)
cur = conn.cursor() 
cur.execute('select source_segment,target_segment from translation_units;')
data=cur.fetchall()
for d in data:
    ssxml=d[0]
    tsxml=d[1]
    try:
        rootSL = etree.fromstring(ssxml)
        for text in rootSL.iter('Value'):
            sltext="".join(text.itertext()).replace("\n"," ")
        rootTL = etree.fromstring(tsxml)
        for text in rootTL.iter('Value'):
            tltext="".join(text.itertext()).replace("\n"," ")
        if not sltext=="" and not tltext=="":
            cadena=sltext+"\t"+tltext
            sortida.write(cadena+"\n")
    except:
        print("ERROR")
        
