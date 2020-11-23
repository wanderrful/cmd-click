import click


@click.command()
def blondie_brownie():
    """Command for blondie-brownie."""
    print("You called the 'golden retriever blondie-brownie' command!")


@click.command()
def toasted_marshmallow():
    """Command for toasted marshmallow."""
    print("You called the 'golden retriever toasted-marshmallow' command!")


@click.command()
def condensed_milk():
    """Command for condensed milk."""
    print("You called the 'golden retriever condensed milk' command!")


@click.command()
def copper():
    """Command for copper."""
    print("You called the 'golden retriever copper' command!")


class GoldenRetriever(click.Group):
    """Group for golden retrievers."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.name = "golden"

        self.commands = {
            blondie_brownie.name: blondie_brownie,
            toasted_marshmallow.name: toasted_marshmallow,
            condensed_milk.name: condensed_milk,
            copper.name: copper,
        }
