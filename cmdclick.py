import cmd

import click

from cmd_click import pets


def ignore_exit(f):
    def _f(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except SystemExit:
            pass

    return _f


class CmdClick(cmd.Cmd):
    intro = "Welcome to CmdClick!"
    prompt = click.style("CmdClick > ", fg="blue")

    def do_exit(self, arg) -> bool:
        """Exit program."""
        print("Thank you for using CmdClick.")
        return True

    @ignore_exit
    def do_pets(self, arg) -> None:
        """Run click fart command."""
        if arg:
            pets.run(arg.split())
        else:
            pets.run()


if __name__ == "__main__":
    CmdClick().cmdloop()
