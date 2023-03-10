python preprocess.py
echo "finish preprocess"

python tools/ntu_gen_bones.py
echo "finish gen_bones"

python tools/ntu_merge_joint_bones.py
echo "finish merge_joint_bones"