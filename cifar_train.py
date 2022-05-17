#!/usr/bin/env bash

import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rank', type=str, default="0")
    parser.add_argument('--node', type=str, default="0015")
    opt = parser.parse_args()

    return opt
args = parse_args()

os.system(f"CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python cvtGanTrain.py \
--max_epoch 2 \
-gen_bs 128 \
-dis_bs 64 \
--dist-url 'tcp://localhost:11228' \
--dist-backend 'nccl' \
--world-size 1 \
--rank {args.rank} \
--dataset cifar10 \
--bottom_width 8 \
--img_size 32 \
--max_iter 500000 \
--gen_model cvtgan_generator \
--dis_model cvtgan_discriminator \
--df_dim 384 \
--d_heads 4 \
--d_depth 3 \
--g_depth 5,4,2 \
--dropout 0 \
--latent_dim 256 \
--gf_dim 1024 \
--num_workers 16 \
--g_lr 0.0001 \
--d_lr 0.0001 \
--optimizer adam \
--loss wgangp-eps \
--wd 1e-3 \
--beta1 0 \
--beta2 0.99 \
--phi 1 \
--eval_batch_size 8 \
--num_eval_imgs 50000 \
--init_type xavier_uniform \
--n_critic 4 \
--val_freq 1000000 \
--print_freq 50 \
--grow_steps 0 0 \
--fade_in 0 \
--patch_size 2 \
--ema_kimg 500 \
--ema_warmup 0.1 \
--ema 0.9999 \
--diff_aug translation,cutout,color \
--exp_name cifar_train")
