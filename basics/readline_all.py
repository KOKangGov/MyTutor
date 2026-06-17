# readline_all.py

f = open("/home/kang7/Work/MyTutor/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
