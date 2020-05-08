import json

def to_json(func):
    def wrapped(*args, **kwards):
        result = json.JSONEncoder().encode(func(*args, **kwards))
        return result
    return wrapped

@to_json
def get_data():
  return {
    'data': 42
  }


@to_json
def f(a, b, c):
    listing = []
    listing.append(a)
    listing.append(b)
    listing.append(c)
    return listing



if __name__ == '__main__':
    print(get_data())  # вернёт '{"data": 42}'

    res = f(1, 2, 4) # выход вот такой [1, 2, 4]
    print(type(res))
