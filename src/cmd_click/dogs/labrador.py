import click


@click.command()
def yellow() -> None:
    """Command for yellow lab."""
    print("You called the 'yellow lab' command!")


@click.command()
def black() -> None:
    """Command for black lab."""
    print("You called the 'black lab' command!")


@click.command()
def chocolate() -> None:
    """Command for chocolate lab."""
    print("You called the 'chocolate lab' command!")


class Labrador(click.Group):
    """Group for labradors."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.name = "labrador"

        self.commands = {
            yellow.name: yellow,
            black.name: black,
            chocolate.name: chocolate
        }
