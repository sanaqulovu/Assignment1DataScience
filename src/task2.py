def typeBasedTransformer(**kwargs):
    new_kwargs = dict()
    for key, value in kwargs.items():
        if type(value) == int or type(value) == float:
            new_value = value ** 2
            new_kwargs[key] = new_value

        elif type(value) == str:
            new_value = value[::-1]
            new_kwargs[key] = new_value
        
        elif type(value) == bool:
            new_value = not value
            new_kwargs[key] = new_value
        
        elif type(value) == list or type(value) == tuple:
            new_value = value[::-1]
            new_kwargs[key] = new_value
        
        elif type(value) == dict:
            new_value = {v: k for k, v in value.items()}
            new_kwargs[key] = new_value
        
        else:
            new_kwargs[key] = value

    return new_kwargs
