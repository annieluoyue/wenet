# wav.scp:IC0936W0004 /mnt/d/ASR/wenet/examples/aishell/AISHELL-2-sample/iOS/data/wav/C0936/IC0936W0004.wav
# wav.scp:BAC009S0002W0122 /home/luo/asr/wenet/examples/aishell/s1/data/aishell/BAC009S0002W0122.wav

import os
with open("wav.scp",'w',encoding="utf-8") as file:

    for item in os.listdir("/home/luo/asr/wenet/examples/aishell/s1/utils/test/testdata"):
        file.write(item.split(".")[0]+" /home/luo/asr/wenet/examples/aishell/s1/utils/test/testdata/"+item+"\n")
        pass

    pass
   

