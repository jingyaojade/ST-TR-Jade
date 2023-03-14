import numpy as np
import pickle

data_path = "D:/publication1/ST-TR/data/qualisys/xsub/train_data_joint_bones.npy"
label_path = 'D:/publication1/ST-TR/data/qualisys/xsub/train_label.pkl'

# sample = np.load(data_path)
# print(sample)

with open(label_path) as f:
    sample_name, label = pickle.load(f)
print(sample_name[1])