import sys

def linux_interaction():
    assert ('darwin' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

print("Feature 1 ##########")
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
        print(read_data)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
