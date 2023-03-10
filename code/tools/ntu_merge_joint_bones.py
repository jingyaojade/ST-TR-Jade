import os
import numpy as np

'''
Function adapted from: https://github.com/kenziyuliu/Unofficial-DGNN-PyTorch 
'''



sets = {
    'val', 'train'
}

# datasets= {'kinetics'} if kinetics is used
datasets = {
    'xsub', 'xview'
}

for dataset in datasets:
    for set in sets:
        print(dataset, set)
        data_jpt = np.load('../data/ntu/{}/{}_data_joint.npy'.format(dataset, set))
        print(len(data_jpt))
        data_bone = np.load('../data/ntu/{}/{}_data_bone.npy'.format(dataset, set))
        print(len(data_bone))
        N, C, T, V, M = data_jpt.shape
        data_jpt_bone = np.concatenate((data_jpt, data_bone), axis=1)
        with open('../data/ntu/{}/{}_data_joint_bones.npy'.format(dataset, set), 'wb') as f:
            np.save(f, data_jpt_bone)
