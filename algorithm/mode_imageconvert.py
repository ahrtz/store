import os

def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
    
    return '모든 파일 삭제 완료!'