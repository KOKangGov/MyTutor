# add_data.py

f = open("/home/kang7/Work/MyTutor/새파일.txt", 'a')
for i in range(11, 20):
    data = f"{i}번째 줄일까요?\n"
    f.write(data)
f.close()
