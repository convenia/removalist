from .data_tools import cleanup


def json(data, filename='template', extension='json'):
    from os import getcwd
    from json import dump

    filepath = "{}/{}.{}".format(getcwd(), filename, extension)
    with open(filepath, 'w') as file:
        data = cleanup(data)
        dump(data, file)
