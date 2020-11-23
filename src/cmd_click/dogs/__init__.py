import click

from cmd_click.dogs.golden_retriever import GoldenRetriever
from cmd_click.dogs.labrador import Labrador


class Dogs(click.Group):
    """Group for dog-related commands."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.name = "dogs"
        self.help = Dogs.__doc__

        labrador = Labrador()
        golden_retriever = GoldenRetriever()

        self.commands = {
            labrador.name: labrador,
            golden_retriever.name: golden_retriever,
        }
