import torch
from torch.autograd import Variable
import argparse

import os
from torchvision import transforms
from torchvision.utils import save_image
from PIL import Image


from PIL import Image
import os, io, sys
import numpy as np
import glob
import random
import os
import numpy as np

import torch.nn as nn
import torch.nn.functional as F
import torch
from torchvision.models import vgg19
import math

import torch
from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms

# Normalization parameters for pre-trained PyTorch models

import torch
from torch.autograd import Variable
import argparse

import os
from torchvision import transforms
from torchvision.utils import save_image
from PIL import Image
import pickle
mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean, std)])


def denormalize(tensors):
    """ Denormalizes image tensors using mean and std """
    for c in range(3):
        tensors[:, c].mul_(std[c]).add_(mean[c])
    return torch.clamp(tensors, 0, 255)


def to_tensor(img):
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean, std)])
    image_tensor = Variable(transform(img)).to(device).unsqueeze(0)
    return image_tensor

