#!/usr/bin/env python
import os
import argparse


def get_cmd(task, sub_task, model_tag, gpu, data_num, bs, lr, source_length, target_length, patience, epoch, warmup,
            model_dir, summary_dir, res_fn, max_steps=None, save_steps=None, log_steps=None):
    if max_steps is None:
        cmd_str = 'bash exp_with_args.sh %s %s %s %d %d %d %d %d %d %d %d %d %s %s %s' % \
                  (task, sub_task, model_tag, gpu, data_num, bs, lr, source_length, target_length, patience, epoch,
                   warmup, model_dir, summary_dir, res_fn)
    else:
        cmd_str = 'bash exp_with_args.sh %s %s %s %d %d %d %d %d %d %d %d %d %s %s %s %d %d %d' % \
                  (task, sub_task, model_tag, gpu, data_num, bs, lr, source_length, target_length, patience, epoch,
                   warmup, model_dir, summary_dir, res_fn, max_steps, save_steps, log_steps)
    return cmd_str


def get_args_by_task_model(task, sub_task, model_tag):
    if task == 'refine':
        if sub_task == 'small':
            src_len = 130
            trg_len = 120
        elif sub_task == 'medium':
            src_len = 240
            trg_len = 240
        epoch = 50
        patience = 5
    
    if 'codet5_small' in model_tag:
        bs = 32
        if (task == 'refine' and sub_task == 'small'):
            bs = 64
    elif 'codet5_large' in model_tag:
        bs = 8
    else:
        bs = 32
    lr = 5
    return bs, lr, src_len, trg_len, patience, epoch


def run_one_exp(args):
    bs, lr, src_len, trg_len, patience, epoch = get_args_by_task_model(args.task, args.sub_task, args.model_tag)
    print('============================Start Running==========================')
    cmd_str = get_cmd(task=args.task, sub_task=args.sub_task, model_tag=args.model_tag, gpu=args.gpu,
                      data_num=args.data_num, bs=bs, lr=lr, source_length=src_len, target_length=trg_len,
                      patience=patience, epoch=epoch, warmup=1000,
                      model_dir=args.model_dir, summary_dir=args.summary_dir,
                      res_fn='{}/{}_{}.txt'.format(args.res_dir, args.task, args.model_tag))
    print('%s\n' % cmd_str)
    os.system(cmd_str)


def get_sub_tasks(task):
    if task == 'refine':
        sub_tasks = ['small', 'medium']
    return sub_tasks


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_tag", type=str, default='codet5_base',
                        choices=['roberta', 'codebert', 'bart_base', 'codet5_small', 'codet5_base', 'codet5_large'])
    parser.add_argument("--task", type=str, default='refine')
    parser.add_argument("--sub_task", type=str, default='small')
    parser.add_argument("--res_dir", type=str, default='results', help='directory to save fine-tuning results')
    parser.add_argument("--model_dir", type=str, default='saved_models', help='directory to save fine-tuned models')
    parser.add_argument("--summary_dir", type=str, default='tensorboard', help='directory to save tensorboard summary')
    parser.add_argument("--data_num", type=int, default=-1, help='number of data instances to use, -1 for full data')
    parser.add_argument("--gpu", type=int, default=0, help='index of the gpu to use in a cluster')
    args = parser.parse_args()

    if not os.path.exists(args.res_dir):
        os.makedirs(args.res_dir)

    assert args.sub_task in get_sub_tasks(args.task)
    run_one_exp(args)
