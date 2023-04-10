""" configurations for this project

author baiyu
"""
import os
from datetime import datetime

#CIFAR100 dataset path (python version)
#CIFAR100_PATH = '/nfs/private/cifar100/cifar-100-python'

#mean and std of cifar100 dataset
CIFAR100_TRAIN_MEAN = (0.5070751592371323, 0.48654887331495095, 0.4409178433670343)
CIFAR100_TRAIN_STD = (0.2673342858792401, 0.2564384629170883, 0.27615047132568404)

CIFAR10_TRAIN_MEAN = (0.49139968, 0.48215827 ,0.44653124)
CIFAR10_TRAIN_STD =  (0.24703233, 0.24348505, 0.26158768)

MNIST_TRAIN_MEAN = (0.13062754273414612,0.13062754273414612,0.13062754273414612) 
MNIST_TRAIN_STD = (0.30810779333114624,0.30810779333114624,0.30810779333114624)

CALTECH256_TRAIN_MEAN = (0.485, 0.456, 0.406)
CALTECH256_TRAIN_STD = (0.229, 0.224, 0.225)

FASHIONMNIST_TRAIN_MEAN = (0.13062754273414612,0.13062754273414612,0.13062754273414612) 
FASHIONMNIST_TRAIN_STD = (0.30810779333114624,0.30810779333114624,0.30810779333114624)

CUB_TRAIN_MEAN = (0.485, 0.456, 0.406)
CUB_TRAIN_STD = (0.229, 0.224, 0.225)

#CIFAR100_TEST_MEAN = (0.5088964127604166, 0.48739301317401956, 0.44194221124387256)
#CIFAR100_TEST_STD = (0.2682515741720801, 0.2573637364478126, 0.2770957707973042)

#directory to save weights file
CHECKPOINT_PATH = 'checkpoint'

#total training epoches
EPOCH = 1
MILESTONES = [60, 120, 160]

#initial learning rate
#INIT_LR = 0.1

DATE_FORMAT = '%A_%d_%B_%Y_%Hh_%Mm_%Ss'
#time of we run the script
TIME_NOW = datetime.now().strftime(DATE_FORMAT)

#tensorboard log dir
LOG_DIR = 'runs'

#save weights file per SAVE_EPOCH epoch
SAVE_EPOCH = 10








