DEBUG = False

def print_list(items):
    if items:
        print('[')
        for item in items:
            print(item)
        print(']')

def check_is_list_of(data, the_type):
    if data:
        if type(data) is list:
            for item in data:
                assert type(item) is the_type, 'expected type {}, but seen type {}'.format(the_type, type(item))

def list_by_filter(fun, filter_str, the_type):
    print ('Filter: {}...\n'.format(filter_str))
    res = fun(filter=filter_str)
    if DEBUG:
        print_list(res.items)
    check_is_list_of(res.items, the_type)
    return res

def list_and_sort(fun, sort_key, the_type):
    print ('\nSORT by {}'.format(sort_key))
    res = fun(sort=sort_key, limit=10)
    if DEBUG:
        print_list(res.items)
    check_is_list_of(res.items, the_type)
    return res


def list_by_start(fun, start_key, the_type):
    print ('\nSTART by {}'.format(start_key))
    res = fun(start=start_key)
    if DEBUG:
        print_list(res.items)
    check_is_list_of(res.items, the_type)
    return res


def list_by_limit(fun, limit_key, the_type):
    print ('\nLIMIT is {}'.format(limit_key))
    res = fun(limit=limit_key, _return_http_data_only="False")
    if DEBUG:
        print_list(res.items)
    check_is_list_of(res.items, the_type)
    return res


def list_by_token(fun, token_key, the_type):
    print ('\nTOKEN is {}'.format(token_key))
    res = fun(token=token_key)
    if DEBUG:
        print_list(res.items)
    check_is_list_of(res.items, the_type)
    return res
