#!/usr/bin/python
# -*- coding: utf-8 -*-

from search_engines import engines, get_config

import launch
import click
import sys

def exit_with_error(message):
    """ Display formatted error message and exit call """
    click.secho(message, err=True, bg='red', fg='white')
    sys.exit(0)


@click.command()
@click.option('--search-engine', '-e', default='google', help='Search engine.')
@click.option('--search-option', '-o', default='default',help='Optional search module.')
@click.option('--list-engines', '-l', is_flag=True, help='List all search engines with options.')
@click.argument('query', nargs=-1)
def main(search_engine, search_option, list_engines, query):
    """Quick search command tool for your terminal"""

    engine_data = {}
    if list_engines:
        for name in engines:
            conf = get_config(name)
            optionals = filter(lambda e: e != 'default', conf.keys())
            if optionals:
                click.echo('{command} -o {options}'.format(
                    command=name.replace('.json', ''),
                    options=', '.join(optionals)))
            else:
                click.echo(name.replace('.json', ''))
        sys.exit(0)

    for name in engines:
        if name.find(search_engine) == 0:
            engine_data = get_config(name)
            break

    # read from standard input if available
    if not sys.stdin.isatty():
        query = sys.stdin.read()

    if not query:
        exit_with_error('Query parameter is missing.')

    if not engine_data:
        exit_with_error('Engine ``{0}`` not found'.format(search_engine))

    if search_option not in engine_data:
        exit_with_error('Option ``{0}`` not available for engine ``{1}``'.\
                        format(search_option, search_engine))

    query = u' '.join(query) if isinstance(query, tuple) else query
    engine_url = engine_data.get(search_option)
    url = engine_url.format(query).encode('utf-8')
    launch.open(url)


if __name__ == '__main__':
    main()
