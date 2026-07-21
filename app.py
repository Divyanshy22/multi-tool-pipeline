"""A simple greeting utility module."""


def greet(name):
    """Return and print a greeting message for the given name."""
    message = "Hello, " + name + "!"
    print(message)
    return message


if __name__ == "__main__":
    greet("Divyansh")
