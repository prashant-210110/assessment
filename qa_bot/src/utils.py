import os
import shutil

from src.config import (
    VECTOR_DB_PATH
)


def clear_vector_database():

    if os.path.exists(
            VECTOR_DB_PATH
    ):
        shutil.rmtree(
            VECTOR_DB_PATH
        )