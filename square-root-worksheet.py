import random

mathml = "<html><body><font size=\"+3\">"
problems = [[str(i**2) for i in range(1,33)]]
random.shuffle(problems[0]) 

mathml += "<math>"
mathml += "<mtable>"
for i in range(0,32,4):
  mathml += "<mtr>"
  for j in range(i,i+4):
    mathml += "<mtd><msqrt>" + problems[0][j] + "</msqrt>"
    mathml += "<mo>=</mo><mspace width='1cm'/>" 
    if j!=8:
      mathml += " "
    mathml += "</mtd>"
  mathml += "</mtr>\n"
mathml += "</mtable>\n"


mathml += "\n</math><br>\n</br><math>\n"

problems = [[str(i) for i in range(1,33)]]
random.shuffle(problems[0]) 

mathml += "<mtable>"
for i in range(0,32,4):
  mathml += "<mtr>"
  for j in range(i,i+4):
    mathml += "<mtd><msup><mi>" + problems[0][j] + "</mi><mn>2</mn></msup>"
    mathml += "<mo>=</mo><mspace width='1cm'/>" 
    if j!=8:
      mathml += " "
    mathml += "</mtd>"
  mathml += "</mtr>\n"
mathml += "</mtable>\n"

mathml += "</math>\n"
mathml += "</font></body></html>"

print(mathml)


