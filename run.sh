# wav.scp text
train_config=./conf/train_conformer.yaml
checkpoint=

# # 创建cmvn
# tools/compute_cmvn_stats.py --num_workers 16 --train_config $train_config \
#     --in_scp ./utils/kaldi_file/wav.scp \
#     --out_cmvn ./global_cmvn

# #dict

# #data.list
#   tools/make_raw_list.py ./utils/kaldi_file/wav.scp ./utils/kaldi_file/text \
#         ./data.list
#训练
python3 wenet/bin/train.py \
      --config $train_config \
      --data_type "raw" \
      --symbol_table ./utils/get_dict \
      --train_data ./train_data.list \
      --cv_data ./dev_data.list \
      ${checkpoint:+--checkpoint $checkpoint} \
      --model_dir ./exp \
      --num_workers 1 \
      --cmvn ./global_cmvn

#测试

# python3 recognize.py \
#       --gpu 0 \
#       --mode "ctc_greedy_search" \
#       --config /mnt/d/ASR/wenet/examples/aishell/s1/ly/exp/train.yaml \
#       --data_type 'raw' \
#       --test_data ./data.list \
#       --checkpoint /mnt/d/ASR/wenet/examples/aishell/s1/ly/exp/init.pt \
#       --beam_size 10 \
#       --batch_size 1 \
#       --penalty 0.0 \
#       --dict /mnt/d/ASR/wenet/examples/aishell/s1/data/lang_dict1 \
#       --ctc_weight 0.5 \
#       --reverse_weight 0.0 \
#       --result_file /mnt/d/ASR/wenet/examples/aishell/s1/ly/exp/decoder/text \

# #计算WER
#  python3 tools/compute-wer.py --char=1 --v=1 ../data/text ./exp/decoder/text
 
# #导出模型
# python3 export_jit.py \
#       --config /mnt/d/ASR/wenet/examples/aishell/s1/ly/exp/20210815_unified_conformer_exp/train.yaml \
#       --checkpoint /mnt/d/ASR/wenet/examples/aishell/s1/ly/exp/20210815_unified_conformer_exp/final.pt \
#       --output_file /mnt/d/ASR/wenet/examples/aishell/s1/ly/exp/20210815_unified_conformer_exp/export/final.zip \
#       --output_quant_file /mnt/d/ASR/wenet/examples/aishell/s1/ly/exp/20210815_unified_conformer_exp/export/final_quant.zip \


