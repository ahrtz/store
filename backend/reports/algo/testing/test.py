import pdftotree

html = pdftotree.parse('documents/KCI_FI002188537.pdf')

fileOut = open('output.html', 'w', encoding='utf-8')
print(html, file=fileOut)
fileOut.close()