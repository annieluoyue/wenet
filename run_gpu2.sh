
stage=4
stop_stage=4

export CUDA_VISIBLE_DEVICES="0"
train_config=./conf/train_conformer.yaml

dir=exp_gpu

if [ ${stage} -le 4 ] && [ ${stop_stage} -ge 4 ]; then
  mkdir -p $dir
  # You have to rm `INIT_FILE` manually when you resume or restart a
  # multi-machine training.
  INIT_FILE=$dir/ddp_init
  init_method=file://$(readlink -f $INIT_FILE)
  echo "$0: init method is $init_method"
  num_gpus=$(echo $CUDA_VISIBLE_DEVICES | awk -F "," '{print NF}')
  # Use "nccl" if it works, otherwise use "gloo"
  dist_backend="gloo"
  world_size=`expr $num_gpus \* $num_nodes`
  echo "total gpus is: $world_size"

  for ((i = 0; i < $num_gpus; ++i)); do
  {
    gpu_id=$(echo $CUDA_VISIBLE_DEVICES | cut -d',' -f$[$i+1])
    # Rank of each gpu/process used for knowing whether it is
    # the master of a worker.
    rank=`expr $node_rank \* $num_gpus + $i`
    python train.py --gpu $gpu_id \
      --config $train_config \
      --data_type 'raw' \
      --symbol_table './utils/get_dict' \
      --train_data ./train_data.list  \
      --cv_data ./dev_data.list  \
      ${checkpoint:+--checkpoint $checkpoint} \
      --model_dir exp_gpu/ \
      --num_workers 1 \
      --cmvn ./global_cmvn \
      --pin_memory
  } &
  done
  wait
fi


if [ ${stage} -le 5 ] && [ ${stop_stage} -ge 5 ]; then
  echo "stage 5 eval"
  python3 recognize.py \
      --gpu 2 \
      --mode "ctc_greedy_search" \
      --config /home/luo/asr/wenet/examples/aishell/s1/exp_gpu/train.yaml \
      --data_type 'raw' \
      --test_data ./test_data.list \
      --checkpoint /home/luo/asr/wenet/examples/aishell/s1/exp_gpu/207.pt \
      --beam_size 10 \
      --batch_size 1 \
      --penalty 0.0 \
      --dict /home/luo/asr/wenet/examples/aishell/s1/utils/get_dict \
      --ctc_weight 0.5 \
      --reverse_weight 0.0 \
      --result_file /home/luo/asr/wenet/examples/aishell/s1/exp_gpu/decoder/text 
fi

if [ ${stage} -le 6 ] && [ ${stop_stage} -ge 6 ]; then
  echo "stage 6 compute wer"
python3 tools/compute-wer.py --char=1 --v=1 ./utils/test/text ./exp_gpu/decoder/text
fi

