import click

@click.command(help="This is just a hello app.It does nothing")
@click.option("--name", prompt="I need your name", help="Need name")
@click.option("--color", prompt="I need your color", help= "This is your color")
def hello(name, color):
    if name == "Thor":
        click.echo("Thor your are always red")
        click.echo(click.style(f"Hello World {name}", fg="red"))
    else:
        pass

if __name__ == "_main_":
    hello()
        