import lxml.etree as et

root = et.Element('knights')

with open('DATA/knights.txt') as k_in:
    for raw_line in k_in:
        line = raw_line.rstrip()
        knight_name, knight_title, knight_color, knight_quest, knight_comment = line.split(':')
        knight = et.SubElement(root, 'knight', title=knight_title)
        color = et.SubElement(knight, 'color')
        color.text = knight_color
        et.SubElement(knight, 'quest').text = knight_quest
        et.SubElement(knight, 'comment').text = knight_comment

doc = et.ElementTree(root)
doc.write('knights.xml', xml_declaration=True, pretty_print=True)


xml = et.tostring(root, xml_declaration=True, pretty_print=True).decode()
print(xml)



