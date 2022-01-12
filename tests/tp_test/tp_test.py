def greet_with_name(name):
    return "Hello everyone, it's " + name


def test_greet_with_name():
    assert greet_with_name("Gil") == "Hello everyone, it's Gil"