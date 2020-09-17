# tika 서버 초기화 하기
import tika
tika.initVM()

from tika import parser

print("텍스트 파일을 추출할 PDF파일명을 입력하세요.")
PDFfileName = 'documents/' + input() + '.pdf'

inputpath = PDFfileName
parsed = parser.from_file(PDFfileName)
temp = parsed["content"]

fileOut = open('output.txt', 'w', encoding='utf-8')
print(temp, file=fileOut)
fileOut.close()
