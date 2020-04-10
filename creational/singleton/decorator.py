"""Implement singleton using a Python decorator
This is a pretty good way to do it, however, MetaClass is more clean way
"""


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Database init called')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)