from os.path import exists
from typing import Optional
from pathlib import Path

from app.consts import ROOT_DIR


def get_environment_type() -> str:
    if exists(ROOT_DIR / '.env'):
        return 'env'
    if exists(ROOT_DIR / '.env.test'):
        return 'test'
    if exists(ROOT_DIR / '.env.prod'):
        return 'prod'
    raise EnvironmentError('Environment not found.')

def get_environment_file_path(env: Optional[str] = None) -> Path:
    environment_type = env or get_environment_type()
    environments = {
        'env': ROOT_DIR / '.env',
        'test': ROOT_DIR / '.env.test',
        'prod': ROOT_DIR / '.env.prod',
    }

    return environments[environment_type]
