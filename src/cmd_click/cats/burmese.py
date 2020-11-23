import click


@click.command()
def calico():
    """Command for calico burmese cats."""
    print("You called the 'burmese calico' command!")


@click.command()
def marmalade():
    """Command for marmalade burmese cats."""
    print("You called the 'burmese marmalade' command!")


class Burmese(click.Group):
    """Group for burmese cats."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.name = "burmese"

        self.commands = {
            calico.name: calico,
            marmalade.name: marmalade,
        }
