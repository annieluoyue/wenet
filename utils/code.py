import os
# response=os.system("bash;cd /home/luo/asr/wenet/examples/aishell/s1/data/aishell;ll")
# print (response)
val = os.popen("cd /home/luo/asr/wenet/examples/aishell/s1/data/aishell; ls").readlines()

for n in val:
    os.system("cp /home/luo/asr/wenet/examples/aishell/s1/data/aishell/"+n.strip()+"/*"+" /home/luo/asr/wenet/examples/aishell/s1/data/aishell1" )
