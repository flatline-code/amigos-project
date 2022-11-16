from amigos_project.services.utils.sort_files import sort_files


def stop():
    return 'Good bye!'


def greeting():
    return 'How can I help you?'


def handler_sort_files(path: str) -> str:
    return sort_files(path)
