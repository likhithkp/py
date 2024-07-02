import pyjokes

def get_joke():
    joke = pyjokes.get_joke()
    print(joke)
    return

get_joke()