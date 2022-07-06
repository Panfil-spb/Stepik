def info_kwargs(**kwargs):
    keys = sorted(kwargs)
    for key in keys:
        print(key + ': ' + str(kwargs[key]))
info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')