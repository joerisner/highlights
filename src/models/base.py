"""
Base class for all models. All methods defined here are class methods, to expose
subclass behavior similar to Rails' ActiveRecord query behavior for models.
"""

import json
from pathlib import Path
from typing import Any


class Base:
    DATA_FILE: str

    @classmethod
    def _load_data(cls) -> dict[str, Any] | None:
        """
        Load JSON data from a class's data file. Not meant to be called directly from subclasses.
        """
        filepath = Path(__file__).parent.parent / "data" / cls.DATA_FILE
        try:
            with open(filepath) as file:
                return json.load(file)
        except FileNotFoundError as e:
            print(f"Could not find data file {e.filename}")

    @classmethod
    def find_all(cls) -> list[dict[str, Any]]:
        """
        Finds all records from the class's JSON data file.

        Returns:
            A list with each record represented as a dictionary.
        """
        data = cls._load_data()

        if not data:
            return []

        class_key = f"{cls.__name__.lower()}s"
        return data[class_key]

    @classmethod
    def find(cls, id: int) -> dict[str, Any] | None:
        """
        Find a record by id from the class's JSON data file.

        Returns:
            A record represented as a dictionary, if found. If not found, returns None.
        """
        records = cls.find_all()
        return next((record for record in records if record["id"] == id), None)
