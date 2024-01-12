import random

mathml = "<html><body><font size=\"+3\">"
problems = [[str(i) for i in range(1,31)]]
random.shuffle(problems[0]) 

width=5
mathml += "<math>"
mathml += "<mtable>"

for i in range(0,30,width):
  mathml+="<mtr>"
  for j in range(i,i+width):
    mathml += "<mtd><mfrac><mn>1</mn><mn>"
    mathml = mathml + problems[0][j] +"</mn></mfrac>"
    mathml += "<mo>=</mo><mspace width='1cm'/>" 
    if j!=width:
      mathml += " "
    mathml += "</mtd>"
  mathml+="</mtr><mtr><mspace depth=\"40px\" height=\"40px\" width=\"100px\"/></mtr>\n"

mathml += "</mtable></math>\n"
mathml += "</font></body></html>"

print(mathml)


