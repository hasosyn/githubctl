from enum import Enum


class OutputOptions(str, Enum):
    json = "json"
    csv = "csv"
    table = "table"
