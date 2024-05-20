# 读取 wav.scp 文件，并替换其中的路径部分
input_file = "/data/experiment/wenet/examples/aishell/s1/utils/train/wav.scp"  # 这里替换为您的 wav.scp 文件的实际路径
output_file = "/data/experiment/wenet/examples/aishell/s1/utils/train/new_wav.scp"  # 指定输出文件的路径

with open(input_file, "r") as file:
    lines = file.readlines()

with open(output_file, "w") as file:
    for line in lines:
        parts = line.split()  # 将每行按空格分割
        if len(parts) == 2:
            original_path = parts[1]
            # 替换路径部分
            modified_path = original_path.replace("/home/luo/asr/", "/data/experiment/")
            # 写入新的行
            file.write(parts[0] + " " + modified_path + "\n")

print("文件替换完成，结果保存在：" + output_file)

