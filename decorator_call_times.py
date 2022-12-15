def call_times(file_name):
    counts_dict = {}

    def inner(func):
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            counts_dict[func.__name__] = wrapper.count
            for func_name, count in counts_dict.items():
                with open(file_name, 'w') as f:
                    f.write(f"Function {func_name} was called {count} times.\n")
            return func
        wrapper.count = 0
        return wrapper
    return inner


@call_times('foo.txt')
def foo():
    pass


@call_times('foo.txt')
def boo():
    pass


@call_times('calls.txt')
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()
