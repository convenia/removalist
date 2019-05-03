from os import getcwd


def json(filename, extension='rcl'):
    from json import load
    from json import JSONDecodeError

    filepath = "{}/{}.{}".format(getcwd(), filename, extension)
    try:
        with open(filepath) as data:
            try:
                return load(data)

            except JSONDecodeError:
                return None

    except FileNotFoundError:
        return None


def yaml(filename, extension='yml'):
    from yaml import safe_load
    from yaml.parser import ParserError

    filepath = "{}/{}.{}".format(getcwd(), filename, extension)
    try:
        with open(filepath) as data:
            try:
                return safe_load(data)

            except ParserError:
                return None

    except FileNotFoundError:
        return None
