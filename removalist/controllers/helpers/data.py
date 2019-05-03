def root(data):
    try:
        return data["_removalist"]["extends"]
    except KeyError:
        return None


def dependencies(data):
    try:
        return data["_removalist"]["dependencies"]
    except KeyError:
        return []


def repository(data):
    try:
        return data["repository"]
    except KeyError:
        return None


def name(data):
    try:
        return data["name"]
    except KeyError:
        return None


def version(data):
    try:
        return data["version"]
    except KeyError:
        return None


def merge(root, node):
    from deepmerge import always_merger

    if root is None:
        return node

    return always_merger.merge(root, node)


def cleanup(data):
    del data["_removalist"]
    return data
