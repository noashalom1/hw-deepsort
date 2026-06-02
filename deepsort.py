def deep_sorted(x: any) -> str:
    if isinstance(x, dict):
        sorted_keys = sorted(x.keys())
        items = [f'"{k}": {deep_sorted(x[k])}' for k in sorted_keys]
        return "{" + ", ".join(items) + "}"
    elif isinstance(x, list):
        items = sorted(deep_sorted(e) for e in x)
        return "[" + ", ".join(items) + "]"
    elif isinstance(x, tuple):
        items = sorted(deep_sorted(e) for e in x)
        if len(items) == 1:
            return "(" + items[0] + ",)"
        return "(" + ", ".join(items) + ")"
    elif isinstance(x, set):
        items = sorted(deep_sorted(e) for e in x)
        return "{" + ", ".join(items) + "}"
    elif isinstance(x, str):
        return x
    else:
        return str(x)



if __name__ == '__main__':
    # x=eval(input())
    # print(deep_sorted(x))
    import doctest
    print (doctest.testmod())
