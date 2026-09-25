import os
_base_ = ['../segnext/segnext_tiny_512x512_160k_4x4_ade20k.py']

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
