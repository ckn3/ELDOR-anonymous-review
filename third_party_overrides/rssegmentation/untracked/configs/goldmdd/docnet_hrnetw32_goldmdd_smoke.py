import os
_base_ = './docnet_hrnetw32_goldmdd.py'

exp_name = (os.environ['ELDOR_EXPERIMENT_ROOT'] + '/rsseg_docnet_hrnetw32_smoke')
epoch = 2

dataset_config = dict(
    data_root=(os.environ['ELDOR_ROOT'] + '/data-cropped-rsseg-smoke'),
    train_mode=dict(
        loader=dict(
            batch_size=4,
            num_workers=2,
            pin_memory=True,
            shuffle=True,
            drop_last=True,
        ),
    ),
    val_mode=dict(
        loader=dict(
            batch_size=4,
            num_workers=2,
            pin_memory=True,
            shuffle=False,
            drop_last=False,
        ),
    ),
    test_mode=dict(
        loader=dict(
            batch_size=4,
            num_workers=2,
            pin_memory=True,
            shuffle=False,
            drop_last=False,
        ),
    ),
)

optimizer_config = dict(
    scheduler=dict(
        max_epoch=epoch,
    ),
)
