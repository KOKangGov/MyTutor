# zipfile_test.py

import zipfile

# 파일 합치기
with zipfile.ZipFile('my_study.zip', 'w') as myzip:
    myzip.write('try_else.py')
    myzip.write('try_except.py')
    myzip.write('try_finally.py')

#해제하기
with zipfile.ZipFile('my_study.zip') as myzip:
    myzip.extract()

# 압축하여 묶기
with zipfile.ZipFile('my_study.zip', 'w', compression=zipfile.Zip_LZMA, compresslevel=9) as myzip:
    