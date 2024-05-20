import os
# response=os.system("bash;cd /home/luo/asr/wenet/examples/aishell/s1/data/aishell;ll")
# print (response)
# /home/luo/asr/data/data_aishell/wav/train
# /home/luo/asr/wenet/examples/aishell/s1/utils/train/traindata
# 这是为了合并train子集合的所有数据到traindata
val = os.popen("cd /data/aishell1/data_aishell/audio/train; ls").readlines()

for n in val:
    os.system("cp /data/aishell1/data_aishell/audio/train/"+n.strip()+"/*"+" /data/experiment/wenet/examples/aishell/s1/utils/train/traindata" )

# import os
# val = os.popen("cd /home/luo/asr/wenet/examples/aishell/s1/data/aishell; ls").readlines()

# for n in val:
#     os.system("cp /home/luo/asr/wenet/examples/aishell/s1/data/aishell/"+n.strip()+"/*"+" /home/luo/asr/wenet/examples/aishell/s1/data/aishell1" )
