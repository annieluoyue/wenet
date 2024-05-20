import os

data_path = "/data/experiment/wenet/examples/aishell/s1/utils/test/testdata"
save_path = "/data/experiment/wenet/examples/aishell/s1/utils/test"
wav_scp = open(os.path.join(save_path, "wav.scp"), "w", encoding="utf-8")

for file_name in os.listdir(data_path):
    # 跳过非.wav文件
    if not file_name.endswith(".wav"):
        continue

    # 获取文件的基本名称（无扩展名）
    ids = file_name.split(".")[0]
    # 写入wav.scp文件
    wav_scp.write(ids + " " + os.path.join(data_path, ids + ".wav") + "\n")

wav_scp.close()

print("wav.scp 文件已生成。")


