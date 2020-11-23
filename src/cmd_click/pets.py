from typing import List, Dict, Callable

import click

from cmd_click.cats import Cats
from cmd_click.dogs import Dogs


def run(*args, **kwargs) -> None:
    """Primary app entry point."""
    dogs = Dogs()
    cats = Cats()

    cli = click.Group(
        help="Demonstration of a nested CLI app using Click!",
        commands={
            dogs.name: dogs,
            cats.name: cats
        }
    )

    cli(*args, **kwargs)
