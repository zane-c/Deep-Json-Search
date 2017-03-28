#!/usr/bin/python

import json
import sys


def main(args):
    """
    Searches through json file for occurrences of the key
    and partial match of a value if supplied as an argument.
    Deep/nested search finds items even in nested json objects

    Ex:
    python JsonSearch.py -f <file_path> <key> [OPTIONAL: <value (partial or full)>]

    """
    try:
        # initialize cmd args
        flag = args[0]
        filename = args[1]
        search_key = args[2]
        search_value = None
        if len(args) == 4:
            search_value = args[3]

        # open file and prepare json obj
        file = open(filename, "r")
        contents = str(file.read())
        data = json.loads(contents)
        file.close()

        matches = 0
        found = 0

        # recursive helper to find nested keys
        def helper(id, key, jsn):
            nonlocal found, matches
            if type(jsn) != dict:
                if key == search_key and (search_value is None or search_value in jsn):
                    found += 1
                    if search_value != jsn:
                        matches += 1
                    s = 'id: {} {}: {}'.format(id, key, jsn)
                    print(s)
            else:
                for k in jsn:
                    helper(id, k, jsn[k])

        # search recursively
        for obj in data:
            helper(obj['id'], None, obj)

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
