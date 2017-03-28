# True Car Coding Challenge

* author | Zane Christenson
* date   | 3/27/17


## Files

* JsonSearch.py:

    python JsonSearch.py -f `<file>` `<key>` [OPTIONAL: `<value>`]

The main submission. It searches through a specificed json `<file>` for 
occurrences of the `<key>` and partial match or full match of `<value>` if 
supplied as an argument. Deep/nested search finds items even in nested 
json objects.

<br />

* JsonSearchNonRecursive.py:

Mostly the same as above but only searches through first layer of
json object (Non-deep search). Added both files since the spec did not 
specify search depth.


## Usage

Partial value search:

    > python JsonSearch.py -f example.json status ACTIV


    id: vmIGIGNrG0x7 status: ACTIVE
    id: hrTKBnilG0x7 status: ACTIVE
    Total 2 records found
    Total 2 records matched
    
Exact value search:

    > python JsonSearch.py -f example.json status ACTIVE
    
    id: vmIGIGNrG0x7 status: ACTIVE
    id: hrTKBnilG0x7 status: ACTIVE
    Total 2 records found
    Total 0 records matched


Deep search no value:

    > python JsonSearch.py -f example.json firstName

    id: vmIGIGNrG0x7 firstName: crazycatsadmin
    id: hrTKBnilG0x7 firstName: Goliath
    Total 2 records found
    Total 2 records matched



Note: python keyword may be left out on unix distributions
    
