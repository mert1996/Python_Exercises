import sys
import xml.etree.ElementTree as etree
k=[]
def get_attr_number(node):
    for elem in node.iter():
        k.append(len(elem.attrib))
    return sum(k)
#return sum([len(elem.items()) for elem in node.iter()])

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
