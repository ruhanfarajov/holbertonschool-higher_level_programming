#!/usr/bin/python3
'''
this is creating a txt file and ml file
'''
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')

    for key, value in my_dict.items():
        child = Et.SubElement(root,key)
        child.text = str(value)

    tree = Et.Element(root, key)
    tree.write("output.xml", encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
     if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    root = ET.Element("data")

    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
