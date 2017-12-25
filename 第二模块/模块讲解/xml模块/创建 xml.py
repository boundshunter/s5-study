#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import xml.etree.ElementTree as ET


new_xml = ET.Element("personinfolist")
personinfo = ET.SubElement(new_xml,"personinfo",attrib={"enrolled":"yes"})
age = ET.SubElement(personinfo,"age",attrib={"checked":"no"})
sex = ET.SubElement(personinfo,"sex")
age.text = '33'
personinfo2 = ET.SubElement(new_xml,"personinfo",attrib={"enrolled":"no"})
age = ET.SubElement(personinfo2,"age")
age.text = '19'

et = ET.ElementTree(new_xml) #生成文档对象
et.write("test.xml", encoding="utf-8",xml_declaration=True)

ET.dump(new_xml) #打印生成的格式

