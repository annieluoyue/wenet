# wav.scp:IC0936W0004 /mnt/d/ASR/wenet/examples/aishell/AISHELL-2-sample/iOS/data/wav/C0936/IC0936W0004.wav
# wav.scp:BAC009S0002W0122 /home/luo/asr/wenet/examples/aishell/s1/data/aishell/BAC009S0002W0122.wav
# 这是为了写wav.scp

import os
with open("wav.scp",'w',encoding="utf-8") as file:

    for item in os.listdir("/data/experiment/wenet/examples/aishell/s1/utils/train/traindata"):
        file.write(item.split(".")[0]+" /data/experiment/wenet/examples/aishell/s1/utils/train/traindata/"+item+"\n")
        pass

    pass
   
