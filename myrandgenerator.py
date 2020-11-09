def my_random_generator(iterable):
    import random
    my_iterable = list(iterable)
    random.shuffle(my_iterable)

    while len(my_iterable) > 0:
        yield my_iterable.pop()

mri = my_random_generator('hello')
for item in mri:
  print(item)
