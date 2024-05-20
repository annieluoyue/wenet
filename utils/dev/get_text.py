#这是为了按照序号来寻找对应文字
# -*- coding: utf-8 -*-
import re   #导入re
 
with open("/home/luo/asr/data/data_aishell/transcript/aishell_transcript_v0.8.txt", "r") as f:      # 打开文本文件

    for line in f.readlines():#读每一行
        idx1 = line.split(" ")[0]
        line = line.strip()
        text = "".join(line.split(" ")[1:])
        
        with open("/home/luo/asr/wenet/examples/aishell/s1/utils/dev/code_text", "r") as f:      # 打开生成的序号文件
            for line in f.readlines():#读每一行
                line = line.strip()
                idx2 = line.split(" ")[0]
                if idx2 == idx1:# 判断序号是否相等
                    print(idx2+" "+text)#合并起来

        pass
    