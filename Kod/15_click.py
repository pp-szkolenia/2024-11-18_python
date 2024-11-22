import click

@click.group()
def cli():
    pass

@cli.group()
def db():
    pass

@cli.group()
def math():
    pass

@db.command()
def initdb():
    click.echo("Initialized the database")

@db.command()
def dropdb():
    click.echo("Dropped the database")

@math.command()
def add():
    click.echo("Adding numbers")

@math.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.option("--multiply-result", type=int, default=1)
@click.option("-v", is_flag=True, help="Verbosity flag")
def subtract(a, b, multiply_result, v):
    result = (a - b) * multiply_result

    if v:
        click.echo(f"The result is {result}")
    else:
        click.echo(result)


if __name__ == "__main__":
    cli()
