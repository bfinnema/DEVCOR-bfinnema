import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

print("##########")
try:
    linux_interaction()
except:
    print('Linux function was not executed')