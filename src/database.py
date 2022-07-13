import sqlite3
import os

from importlib_metadata import PackageNotFoundError


def connect(name: str = "grow_me_organic") -> sqlite3.Connection:
    """
    creates connection to SQLite3 database
    """

    # if "sqlite" not in os.listdir():
    #     raise PackageNotFoundError("sqlite directory not found")

    # if f"{name}" not in os.listdir("sqlite"):
    #     raise FileNotFoundError(f"{name} not found")

    return sqlite3.connect(name)