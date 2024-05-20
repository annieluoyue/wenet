#这是为了把所有音频的序号找到
import re   #导入re
 
# 去除文字内空格
with open("/home/luo/asr/wenet/examples/aishell/s1/utils/dev/wav.scp", "r") as f:      # 打开文件

    for line in f.readlines():#读每一行
        idx = line.split(" ")[0]#通过空格对字符串进行切片，分割第一个
        print(idx)#合并起来
        pass