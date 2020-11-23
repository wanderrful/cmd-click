import click
from cmd_click.cats.burmese import Burmese


class Cats(click.Group):
    """Group for cat-related commands."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.name = "cats"
        self.help = Cats.__doc__

        burmese = Burmese()

        self.commands = {
            burmese.name: burmese
        }
