from amigos_project.services.utils.sort_files import sort_files


def stop():
    return 'Good bye!'


def greeting(commands):
    return f'How can I help you? This is list of commands {list(commands)}'


def handler_sort_files(path: str) -> str:
    return sort_files(path)
