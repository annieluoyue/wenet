import os
val = os.popen("cd /home/luo/asr/data/data_aishell/wav/test; ls").readlines()

for n in val:
    os.system("cp /home/luo/asr/data/data_aishell/wav/test/"+n.strip()+"/*"+" /home/luo/asr/wenet/examples/aishell/s1/utils/test/testdata" )
