testdata=/data/experiment/wenet/examples/aishell/s1/utils/commonvoice_test/data.list
# commonvoice/data/experiment/wenet/examples/aishell/s1/utils/commonvoice_test
# aishell2019/data/aishell2/eval-dataset/datalist/
# aishell1/data/experiment/wenet/examples/aishell/s1/test/data.list
# aishell2018/data/wenet/examples/aishell/s1/utils/test/data.list

python3 recognize.py \
      --gpu 1 \
      --mode "attention_rescoring" \
      --config /data/experiment/wenet/examples/aishell/s1/exp_gpu/train.yaml \
      --data_type 'raw' \
      --test_data $testdata \
      --checkpoint /data/experiment/wenet/examples/aishell/s1/exp_gpu/220.pt \
      --beam_size 10 \
      --batch_size 1 \
      --penalty 0.0 \
      --dict /data/experiment/wenet/examples/aishell/s1/utils/get_dict \
      --ctc_weight 0.5 \
      --reverse_weight 0.0 \
      --result_file  /data/experiment/wenet/examples/aishell/s1/decoder/220_CV_text \
