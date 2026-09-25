# Source this file from the review repository root after activating a model environment.
if [ ! -f ./misc/semseg_common.py ]; then
    echo "Run: cd /path/to/review-code && source scripts/review_env.sh" >&2
    return 1
fi
export ELDOR_ROOT="${ELDOR_ROOT:-$PWD}"
export ELDOR_THIRD_PARTY="${ELDOR_THIRD_PARTY:-$ELDOR_ROOT/third_party}"
export ELDOR_DATA_ROOT="${ELDOR_DATA_ROOT:-$ELDOR_ROOT/data}"
export ELDOR_PATCH_ROOT="${ELDOR_PATCH_ROOT:-$ELDOR_ROOT/data-cropped}"
export ELDOR_EXPERIMENT_ROOT="${ELDOR_EXPERIMENT_ROOT:-$ELDOR_ROOT/experiments}"
export ELDOR_PRETRAINED="${ELDOR_PRETRAINED:-$ELDOR_ROOT/pretrained}"
