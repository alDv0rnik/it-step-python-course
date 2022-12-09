def doubled(function):
    def Wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return (result, result)
    return Wrapper


@doubled
def get_hello():
    return 'Hello'


print(get_hello())
    
