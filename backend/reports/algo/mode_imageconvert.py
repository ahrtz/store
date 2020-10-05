import fitz
import os

def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
    
    return '모든 파일 삭제 완료!'

def printAllFile(filePath):
    removeAllFile("images/")
    doc = fitz.open(filePath)

    '''
    temp = []
    for y in range(len(doc)):
        temp.append(doc.getPageImageList(y))

    result = []
    for y in range(len(temp)):
        cnt = 0
        for x in range(len(temp)):
            if temp[y] == temp[x]:
                cnt += 1
        
        if cnt == 1:
            result.append(y)
    
    cnt = 0
    for x in range(len(doc)):
        if x in result:
            cnt += 1
            for img in doc.getPageImageList(x): 
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                if pix.n < 5:
                    pix.writePNG("images/%s.png" % (cnt))
                else:
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.writePNG("images/%s.png" % (cnt))
                    pix1 = None
                pix = None
    '''
    cnt = 0
    for x in range(len(doc)):
        cnt += 1
        for img in doc.getPageImageList(x): 
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:
                pix.writePNG("images/%s.png" % (cnt))
            else:
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG("images/%s.png" % (cnt))
                pix1 = None
            pix = None