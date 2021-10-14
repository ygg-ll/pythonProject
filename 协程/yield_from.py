myllist = [1, 2, 3]

my_dict = {
    "bobby1": "proedu",
    "bobby2": "imooc.comu",
}


# from itertools import chain
# for value in chain(myllist, my_dict, range(5, 10)):
#     print(value)


def my_chain(*args, **kwargs):
    for iterable in args:
        yield from iterable
        # for i in iterable:
        #     yield i


for value in my_chain(myllist, my_dict, range(5, 10)):
    print(value)


