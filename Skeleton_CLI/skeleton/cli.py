# Skeletion CLI program 
# Replace mymodule with your own code logic
# Try to keep output and CLI handling in cli.py
# Create a virtual environment with python -m venv venv
# Edit the setup.py and afterwards pip install --editable . 

import sys
import click

import skeleton.mymodule as mymodule

@click.command()
@click.option('-s', '--string', default='World',
    help='String')
@click.option('--debug', '-D', is_flag=True)
@click.option('--verbose', '-v', is_flag=True)
@click.option('--repeat', default=1)
@click.argument('out', type=click.File('w'), default='-') # defaults to stdout
def main(string, debug, verbose, repeat, out):
    """
    This script greets you\n
        - OUT is optional output file
    """

    while repeat > 0:
        click.echo(mymodule.hello(string), file=out) # click.echo is preferred over print
        repeat -= 1

if __name__ == '__main__':
    sys.exit(main())
