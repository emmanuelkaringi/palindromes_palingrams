"""Load a text file as a list."""

import sys

def load(file):
    """Open a text file and return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt

    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e,file))
        sys.exit(1)