# 创建cmvn
train_config=./conf/train_conformer.yaml
./tools/compute_cmvn_stats.py --num_workers 8 --train_config $train_config \
    --in_scp ./utils/train/wav.scp \
    --out_cmvn ./utils/train/global_cmvn
