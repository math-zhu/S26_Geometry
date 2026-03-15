import os, xml.etree.ElementTree as ET
base = '/Users/yizhu/Documents/Github/S26_Geometry/Notes/images'

# SSS proof step 2:
# A=(70,165), B=(310,165), C=(140,30), D=(140,300)
# Dashed line CD. Arcs:
#   single arc at A for angle CAD:
#     A-to-C unit=(0.460,-0.888), A-to-D unit=(0.460,0.888)
#     pt on AC @25: (82,143), pt on AD @25: (82,187) -> sweep=1 (curves right, into angle)
#   single arc at D (left) for angle CDA:
#     D-to-C unit=(0,-1), D-to-A unit=(-0.460,-0.888)
#     pt on DC @20: (140,280), pt on DA @20: (131,282) -> sweep=0 (curves left)
#   double arc at C for angle BCD (toward B and D):
#     C-to-B unit=(0.783,0.622), C-to-D unit=(0,1)
#     inner @25: pt on CB=(160,46), pt on CD=(140,55) -> sweep=1
#     outer @29: pt on CB=(163,48), pt on CD=(140,59) -> sweep=1
#   double arc at D (right) for angle BDC:
#     D-to-B unit=(0.783,-0.622), D-to-C unit=(0,-1)
#     inner @25: pt on DB=(160,284), pt on DC=(140,275) -> sweep=0
#     outer @29: pt on DB=(163,282), pt on DC=(140,271) -> sweep=0
content_step2 = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 345">\n'
    '  <polygon points="70,165 310,165 140,300" fill="#ffeedd" stroke="#cc6600" stroke-width="2"/>\n'
    '  <polygon points="70,165 310,165 140,30"  fill="#ddeeff" stroke="#3366cc" stroke-width="2"/>\n'
    '  <line x1="70"  y1="165" x2="310" y2="165" stroke="#555555" stroke-width="2.5"/>\n'
    '  <line x1="140" y1="30"  x2="140" y2="300" stroke="#cc3333" stroke-width="1.8"'
    ' stroke-dasharray="6,4"/>\n'
    '  <text x="52"  y="183" font-family="serif" font-size="17" font-style="italic">A</text>\n'
    '  <text x="314" y="183" font-family="serif" font-size="17" font-style="italic">B</text>\n'
    '  <text x="133" y="20"  font-family="serif" font-size="17" font-style="italic">C</text>\n'
    '  <text x="133" y="320" font-family="serif" font-size="17" font-style="italic">D</text>\n'
    '  <path d="M 129,52 A 25,25 0 0,1 140,55"  fill="none" stroke="#3366cc" stroke-width="1.8"/>\n'
    '  <path d="M 140,280 A 20,20 0 0,0 131,282" fill="none" stroke="#3366cc" stroke-width="1.8"/>\n'
    '  <path d="M 160,46 A 25,25 0 0,1 140,55"  fill="none" stroke="#cc6600" stroke-width="1.8"/>\n'
    '  <path d="M 163,48 A 29,29 0 0,1 140,59"  fill="none" stroke="#cc6600" stroke-width="1.8"/>\n'
    '  <path d="M 160,284 A 25,25 0 0,0 140,275" fill="none" stroke="#cc6600" stroke-width="1.8"/>\n'
    '  <path d="M 163,282 A 29,29 0 0,0 140,271" fill="none" stroke="#cc6600" stroke-width="1.8"/>\n'
    '  <text x="200" y="340" text-anchor="middle" font-family="serif" font-size="15">'
    'Line CD drawn; &#x25B3;BCD and &#x25B3;ACD are isosceles</text>\n'
    '</svg>\n'
)
path2 = os.path.join(base, 'sss_congruence_theorem_proof_step2.svg')
with open(path2, 'w', encoding='ascii') as f:
    f.write(content_step2)
non_ascii = sum(1 for b in open(path2, 'rb').read() if b > 127)
ET.parse(path2)
print(f'sss_congruence_theorem_proof_step2.svg: {non_ascii} non-ASCII bytes — XML valid')

svgs = {}

svgs['isosceles_triangle_theorem_2.svg'] = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 260">\n'
    '  <polygon points="120,30 60,220 180,220" fill="#ddeeff" stroke="#3366cc" stroke-width="2"/>\n'
    '  <text x="113" y="20"  font-family="serif" font-size="17" font-style="italic">A</text>\n'
    '  <text x="42"  y="238" font-family="serif" font-size="17" font-style="italic">B</text>\n'
    '  <text x="182" y="238" font-family="serif" font-size="17" font-style="italic">C</text>\n'
    '  <path d="M 86,220 A 26,26 0 0,0 68,195" fill="none" stroke="#cc3333" stroke-width="1.8"/>\n'
    '  <path d="M 154,220 A 26,26 0 0,1 165,199" fill="none" stroke="#cc3333" stroke-width="1.8"/>\n'
    '  <line x1="120" y1="213" x2="120" y2="227" stroke="#3366cc" stroke-width="2"/>\n'
    '  <text x="248" y="138" font-family="serif" font-size="26">&#x2245;</text>\n'
    '  <polygon points="400,30 340,220 460,220" fill="#ffeedd" stroke="#cc6600" stroke-width="2"/>\n'
    '  <text x="393" y="20"  font-family="serif" font-size="17" font-style="italic">A</text>\n'
    '  <text x="322" y="238" font-family="serif" font-size="17" font-style="italic">C</text>\n'
    '  <text x="462" y="238" font-family="serif" font-size="17" font-style="italic">B</text>\n'
    '  <path d="M 366,220 A 26,26 0 0,0 348,195" fill="none" stroke="#cc3333" stroke-width="1.8"/>\n'
    '  <path d="M 434,220 A 26,26 0 0,1 452,195" fill="none" stroke="#cc3333" stroke-width="1.8"/>\n'
    '  <line x1="400" y1="213" x2="400" y2="227" stroke="#cc6600" stroke-width="2"/>\n'
    '  <text x="260" y="253" text-anchor="middle" font-family="serif" font-size="15">'
    '&#x2220;B = &#x2220;C,&#160;&#160;BC = CB,&#160;&#160;&#x2220;C = &#x2220;B'
    '&#160;&#160;&#x27F9;&#160;&#160;&#x25B3;ABC &#x2245; &#x25B3;ACB</text>\n'
    '</svg>\n'
)

svgs['sss_congruence_theorem.svg'] = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 295">\n'
    '  <polygon points="50,200 220,200 70,70" fill="#ddeeff" stroke="#3366cc" stroke-width="2"/>\n'
    '  <text x="34"  y="218" font-family="serif" font-size="17" font-style="italic">A</text>\n'
    '  <text x="224" y="218" font-family="serif" font-size="17" font-style="italic">B</text>\n'
    '  <text x="63"  y="58"  font-family="serif" font-size="17" font-style="italic">C</text>\n'
    '  <line x1="135" y1="193" x2="135" y2="207" stroke="#3366cc" stroke-width="2"/>\n'
    '  <line x1="148" y1="129" x2="140" y2="139" stroke="#3366cc" stroke-width="2"/>\n'
    '  <line x1="151" y1="131" x2="143" y2="141" stroke="#3366cc" stroke-width="2"/>\n'
    '  <line x1="64"  y1="140" x2="54"  y2="138" stroke="#3366cc" stroke-width="2"/>\n'
    '  <line x1="65"  y1="136" x2="55"  y2="134" stroke="#3366cc" stroke-width="2"/>\n'
    '  <line x1="66"  y1="132" x2="56"  y2="130" stroke="#3366cc" stroke-width="2"/>\n'
    '  <text x="240" y="152" font-family="serif" font-size="26">&#x2245;</text>\n'
    '  <polygon points="457,113 287,113 437,243" fill="#ffeedd" stroke="#cc6600" stroke-width="2"/>\n'
    '  <text x="462" y="110" font-family="serif" font-size="17" font-style="italic">D</text>\n'
    '  <text x="270" y="110" font-family="serif" font-size="17" font-style="italic">E</text>\n'
    '  <text x="432" y="261" font-family="serif" font-size="17" font-style="italic">F</text>\n'
    '  <line x1="372" y1="106" x2="372" y2="120" stroke="#cc6600" stroke-width="2"/>\n'
    '  <line x1="360" y1="184" x2="368" y2="174" stroke="#cc6600" stroke-width="2"/>\n'
    '  <line x1="357" y1="182" x2="365" y2="172" stroke="#cc6600" stroke-width="2"/>\n'
    '  <line x1="453" y1="175" x2="443" y2="173" stroke="#cc6600" stroke-width="2"/>\n'
    '  <line x1="452" y1="179" x2="442" y2="177" stroke="#cc6600" stroke-width="2"/>\n'
    '  <line x1="451" y1="183" x2="441" y2="181" stroke="#cc6600" stroke-width="2"/>\n'
    '  <text x="260" y="278" text-anchor="middle" font-family="serif" font-size="15">'
    'AB = DE,&#160;&#160;BC = EF,&#160;&#160;CA = FD&#160;&#160;&#x27F9;&#160;&#160;'
    '&#x25B3;ABC &#x2245; &#x25B3;DEF</text>\n'
    '</svg>\n'
)

svgs['sss_congruence_theorem_proof_step1.svg'] = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 345">\n'
    '  <polygon points="70,165 310,165 140,300" fill="#ffeedd" stroke="#cc6600" stroke-width="2"/>\n'
    '  <polygon points="70,165 310,165 140,30"  fill="#ddeeff" stroke="#3366cc" stroke-width="2"/>\n'
    '  <line x1="70" y1="165" x2="310" y2="165" stroke="#555555" stroke-width="2.5"/>\n'
    '  <text x="52"  y="183" font-family="serif" font-size="17" font-style="italic">A</text>\n'
    '  <text x="314" y="183" font-family="serif" font-size="17" font-style="italic">B</text>\n'
    '  <text x="133" y="20"  font-family="serif" font-size="17" font-style="italic">C</text>\n'
    '  <text x="133" y="320" font-family="serif" font-size="17" font-style="italic">D</text>\n'
    '  <text x="200" y="340" text-anchor="middle" font-family="serif" font-size="15">'
    '&#x25B3;ABC and &#x25B3;ABD share side AB</text>\n'
    '</svg>\n'
)

for fname, content in svgs.items():
    path = os.path.join(base, fname)
    with open(path, 'w', encoding='ascii') as f:
        f.write(content)
    non_ascii = sum(1 for b in open(path, 'rb').read() if b > 127)
    try:
        ET.parse(path)
        valid = 'XML valid'
    except Exception as e:
        valid = f'XML ERROR: {e}'
    print(f'{fname}: {non_ascii} non-ASCII bytes — {valid}')
