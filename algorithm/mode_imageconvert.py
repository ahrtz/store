import os

def removeAllFile(filePath):
    try:
        if not(os.path.isdir(filePath)):
            os.makedirs(os.path.join(filePath))
    except:
        pass

    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
    
    return '모든 파일 삭제 완료!'