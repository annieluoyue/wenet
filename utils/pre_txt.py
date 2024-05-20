import re   #导入re
 
# 去除文字内空格
with open("/home/luo/asr/wenet/examples/aishell/s1/utils/aishell_transcript_v0.8.txt", "r") as f:      # 打开文件

    for line in f.readlines():
        line = line.strip()
        idx = line.split(" ")[0]
        text = "".join(line.split(" ")[1:])
        print(idx+" "+text)
        pass