from subprocess import run


def clone(path, name, repository):
    run(["rm", "-rf", path], capture_output=True)
    run(["git", "clone", repository, "{}/{}".format(path, name)],
        capture_output=True)


def checkout(path, name, ref):
    if ref is not None:
        run(["git", "checkout", ref], cwd="{}/{}".format(path, name),
            capture_output=True)
