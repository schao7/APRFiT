export scale=small
export lr=1e-4
export batch_size=64
export epochs=50
export dev_file=data/$scale/valid.buggy-fixed.buggy,data/$scale/valid.buggy-fixed.fixed
export test_file=data/$scale/test.buggy-fixed.buggy,data/$scale/test.buggy-fixed.fixed
export output_dir=saved_models/$scale/
export scheduler_fun=S5
export load_model_path="your_path/graphcodebert_bfp_small_or_medium.bin"

python run_aprfit.py --do_test --model_type roberta --model_name_or_path $pretrained_model --tokenizer_name microsoft/graphcodebert-base --config_name microsoft/graphcodebert-base --load_model_path $load_model_path --dev_filename $dev_file --test_filename $test_file --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --eval_batch_size $batch_size 2>&1| tee $output_dir/test.log
