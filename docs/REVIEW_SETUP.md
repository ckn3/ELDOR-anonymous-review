# Portable review setup

Activate one of the model-specific environments described in `ENV_SETUP.md`.
From the root of this repository, run:

```bash
source scripts/review_env.sh
```

The scripts and third-party configurations use these environment variables:

| Variable | Default location |
|---|---|
| `ELDOR_ROOT` | This code repository |
| `ELDOR_THIRD_PARTY` | `third_party/` |
| `ELDOR_DATA_ROOT` | `data/` (released aligned images and labels) |
| `ELDOR_PATCH_ROOT` | `data-cropped/` |
| `ELDOR_EXPERIMENT_ROOT` | `experiments/` |
| `ELDOR_PRETRAINED` | `pretrained/` (upstream pretrained models) |

Set any override before sourcing the script. Keep this environment active when
changing into a third-party project directory. Configure the model environment
separately; no personal Conda installation directory is required.

Clone the upstream repositories and check out the revisions in
`THIRD_PARTY_LOCKS.md`. Apply the included overrides with:

```bash
bash scripts/apply_overrides.sh "$ELDOR_THIRD_PARTY"
```

Supply locally available aligned source image/label pairs under
`ELDOR_DATA_ROOT/{train,val,test}/{image,label}/`. This code release does not
include dataset files or trained checkpoints. Cropped patches can be generated with:

```bash
python misc/build_cropped_dataset.py --workers 4
```

The crop output must be a new directory: the script refuses to overwrite an
existing crop dataset unless `--overwrite` is explicitly supplied.

The raw-label rebuilding script additionally requires the original annotation
source through `ELDOR_SOURCE_DATA`; it is not needed to use the released labels.
Site-map generation uses the spatial table in `GoldMDD_dataset_README.md`.

Training commands and method settings are documented in `TRAINING_PROTOCOL.md`
and `METHOD_SOURCES.md`. For example, inspect the SegFormer arguments with:

```bash
python misc/train_semseg_segformer.py --help
```

Exported training metadata uses `${ELDOR_*}` placeholders for machine-dependent
paths. Evaluation should use the local paths supplied by command-line arguments.
Tensor parameters, label mappings, splits, and reported metrics are unchanged.
