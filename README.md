# APRFiT

In this codebase we provide instructions for reproducing our results from the paper. We hope that this work can be useful for future research on automated program repair.

# Datasets and Models
We provide [datasets](https://figshare.com/s/4e679d03b0bd8cd27a69) and [pre-trained models](https://figshare.com/s/627164c54ea31fa6d577) fine-tuned by our approach to verify the results.

# Dependency
- Pytorch 1.7.1
- tensorboard 2.4.1
- transformers 4.6.1
- tree-sitter 0.2.2

# Usage
## Running CodeT5 Experiments of APRFiT
- Download the [dataset](https://figshare.com/s/4e679d03b0bd8cd27a69) and place it in the following folder
	- `mkdir ./APRFiT4CodeT5/data`
- Go to `sh` folder, set the `WORKDIR` in `exp_with_args.sh` to be your cloned repository path.
- Download pre-trained model [here](https://figshare.com/s/627164c54ea31fa6d577), and pass its path to load at [here](https://github.com/schao7/APRFiT/blob/297fb9cbc51667d20dcab39b4fcacfaa709933c5/APRFiT4CodeT5/run_apr.py#L366), e.g., `file = "APRFiT4CodeT5/codet5_bfp_small.bin"`
- Evaluation
	- For Bugs2Fix small dataset, please use `codet5_bfp_small.bin`, and run the program: `python run_aprfit.py --model_tag codet5_base --task refine --sub_task small`
	- For Bugs2Fix medium dataset, please use `codet5_bfp_medium.bin`, and run the program: `python run_aprfit.py --model_tag codet5_base --task refine --sub_task medium`

## Running GraphCodeBERT Experiments of APRFiT
- Download the [dataset](https://figshare.com/s/4e679d03b0bd8cd27a69) and place it in this folder.
	- `mkdir ./APRFiT4GraphCodeBERT/data`
- Download pre-trained model  [here](https://figshare.com/s/627164c54ea31fa6d577), and pass its path to load at [here](https://github.com/schao7/APRFiT/blob/297fb9cbc51667d20dcab39b4fcacfaa709933c5/APRFiT4GraphCodeBERT/run_aprfit.sh#L9), e.g., `file = "APRFiT4GraphCodeBERT/graphcodebert_bfp_small.bin"`
- Evaluation
	- For Bugs2Fix small dataset, please use `graphcodebert_bfp_small.bin`, change the `scale` variables value in script files to `small` and run the program: `bash run_aprfit.sh`
	- For Bugs2Fix medium dataset, please use `graphcodebert_bfp_medium.bin`, change the `scale` variables value in script files to `medium`, and run the program: `bash run_aprfit.sh`

### Tree-sitter (optional)

If the built file "parser/my-languages.so" doesn't work for you, please rebuild as the following command:

```shell
cd parser
bash build.sh
cd ..
```

# Acknowledgement
The implementation of this repo relies on resources from [GraphCodeBERT](https://github.com/microsoft/CodeBERT/tree/master/GraphCodeBERT/refinement) and [CodeT5](https://github.com/salesforce/CodeT5) . The code is implemented using PyTorch. We thank the original authors for their open-sourcing.
