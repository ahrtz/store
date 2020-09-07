from tika import parser

print("텍스트 파일을 추출할 PDF파일명을 입력하세요.")
PDFfileName = input()

inputpath = PDFfileName
parsed = parser.from_file(PDFfileName)
temp = parsed["content"]

while True:
   cnt = temp.count('\n\n\n')
   if cnt == 0:
      break

   temp = temp.replace('\n\n\n', '\n\n')

fileOut = open('output.txt', 'w', encoding='utf-8')
print(temp, file=fileOut)
fileOut.close()


