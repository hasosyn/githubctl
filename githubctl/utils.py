import json
from typing import List
import csv
import sys
from rich import print_json
from rich.table import Table
from rich.console import Console

from options import OutputOptions


def print_beauty(list_of_dict: List[dict], output_format: OutputOptions):
    if output_format == OutputOptions.csv:
        fieldnames = list_of_dict[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_of_dict)

    elif output_format == OutputOptions.json:
        print_json(json.dumps(list_of_dict))

    elif output_format == OutputOptions.table:
        table = Table()

        headers = list_of_dict[0].keys()
        table.add_column("")

        for header in headers:
            table.add_column(str(header))

        for repo in list_of_dict:
            table.add_row(*[str(list_of_dict.index(repo) + 1)] + [str(r) for r in repo.values()])

        console = Console()
        console.print(table)
