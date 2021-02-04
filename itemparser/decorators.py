from functools import wraps


def attr_error_catcher(func, default='Unknown'):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
        except Exception as e:
            data = default
            print(f'Error: {e}; Args:{args}; Kwargs:{kwargs}; Func name: {func.__name__}')

        return data
    return wrapper
