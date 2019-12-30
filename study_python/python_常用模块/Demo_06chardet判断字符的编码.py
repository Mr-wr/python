import chardet

data = '离离原上草，一岁一枯荣'.encode('gbk')
chardet.detect(data)
#{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}