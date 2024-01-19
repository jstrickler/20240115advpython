import lxml.etree as et

doc = et.parse('DATA/solar.xml')

root = doc.getroot()
print(f"{root = }")

for subelement in root:
    # print(subelement.tag)
    if subelement.tag.endswith('planets'):
        for planet in subelement:
            print(planet.get('planetname'))
            for moon in planet:
                print(f"    {moon.text}")


