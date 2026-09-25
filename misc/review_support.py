"""Portable metadata for exported training configurations and checkpoints."""
from __future__ import annotations

import os
from pathlib import PurePath


def portable_metadata(value):
    """Retain hyperparameters, recording review paths as portable placeholders."""
    if isinstance(value, dict):
        return {key: portable_metadata(item) for key, item in value.items()}
    if isinstance(value, list):
        return [portable_metadata(item) for item in value]
    if isinstance(value, tuple):
        return tuple(portable_metadata(item) for item in value)
    if isinstance(value, (str, PurePath)):
        result = str(value)
        roots = {key: val.rstrip('/') for key, val in os.environ.items()
                 if key.startswith('ELDOR_') and val.startswith('/') and len(val.rstrip('/')) > 1}
        for key, root in sorted(roots.items(), key=lambda pair: -len(pair[1])):
            if result == root or result.startswith(root + '/'):
                return '${' + key + '}' + result[len(root):]
        if result.startswith('/'):
            return '${EXTERNAL_PATH}/' + result.rstrip('/').rsplit('/', 1)[-1]
        return result
    return value
