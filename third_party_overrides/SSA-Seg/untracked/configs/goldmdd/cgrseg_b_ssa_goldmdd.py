import os
_base_ = ['../cgrseg/cgrseg-b_ade20k_160k_ssa.py']

exec(
    compile(
        open((os.environ['ELDOR_THIRD_PARTY'] + '/SSA-Seg/configs/goldmdd/_base_/goldmdd_dataset.py'), 'rb').read(),
        (os.environ['ELDOR_THIRD_PARTY'] + '/SSA-Seg/configs/goldmdd/_base_/goldmdd_dataset.py'),
        'exec'))
exec(
    compile(
        open((os.environ['ELDOR_THIRD_PARTY'] + '/SSA-Seg/configs/goldmdd/_base_/goldmdd_runtime.py'), 'rb').read(),
        (os.environ['ELDOR_THIRD_PARTY'] + '/SSA-Seg/configs/goldmdd/_base_/goldmdd_runtime.py'),
        'exec'))

model = dict(
    backbone=dict(init_cfg=None),
    decode_head=dict(num_classes=14))
