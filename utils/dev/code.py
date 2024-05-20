import os
val = os.popen("cd /home/luo/asr/data/data_aishell/wav/dev; ls").readlines()

for n in val:
    os.system("cp /home/luo/asr/data/data_aishell/wav/dev/"+n.strip()+"/*"+" /home/luo/asr/wenet/examples/aishell/s1/utils/dev/devdata" )
