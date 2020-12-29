def attr_error_catcher(func, default='Unknown'):
    def wrapper(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
        except Exception as e:
            data = default
            print(f'Error: {e}')

        return data
    return wrapper
