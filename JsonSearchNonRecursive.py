#!/usr/bin/python

import json
import sys


def main(args):
    """
    Searches through json file for occurrences of the key
    and partial match of a value if supplied as an argument.

    Ex:
    python JsonSearch.py -f <file_path> <key> [OPTIONAL: <value (partial or full)>]

    Does not support Nested/Deep search. See JsonSearch.py for 
    recursive deep search.

    """
    try:
        # initialize cmd args
        flag = args[0]
        filename = args[1]
        key = args[2]
        value = None
        if len(args) == 4:
            value = args[3]

        # open file and prepare json obj
        file = open(filename, "r")
        contents = str(file.read())
        data = json.loads(contents)
        file.close()

        matches = 0
        found = 0

        # get json data
        for obj in data:
            for k in obj:
                if k == key and (value is None or value in obj[k]):
                    found += 1
                    if value != obj[k]:
                        matches += 1
                    s = 'id: {} {}: {}'.format(obj['id'], key, obj[k])
                    print(s)

        # print search details
        print('Total {} records found'.format(found))
        print('Total {} records matched'.format(matches))

    # handle exceptions
    except IndexError:
        print("Insufficient command line arguments given")
    except json.decoder.JSONDecodeError:
        print("Unable to read json file")
    except FileNotFoundError:
        print("Unable to open file ")

if __name__ == "__main__":
    main(sys.argv[1:])
