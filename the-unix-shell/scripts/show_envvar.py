#!/usr/bin/env python
import sys

def find_variable_value(argv=sys.argv):
    if len(argv) < 2:
        sys.stderr.write('ERROR: This python script must get the name of the variable as a parameter.')
    elif sys.stdin.isatty():  # are we in a pipe?
        sys.stderr.write('ERROR: This python script must be called on a pipe.')
    else:
        var_name = argv[1]      # argv[1] is first parameter of the program
        for line in sys.stdin.readlines():
            if var_name + '=' in line:
                var_value = line.partition(var_name + '=')[2].partition(' ')[0]
                sys.stdout.write(var_value)
                sys.exit(0)
    exit(1)

#
# Regular expressions double-trouble
#import re
#    var_search = re.search(var_re, line)
#        if var_search:
#            var_value = var_search.group(1)
#            sys.stdout.write(var_value)
#            sys.exit(0)
#        var_re = re.compile('%s=(.*)(\s)' % var_name)
#

if __name__ == "__main__":
    try:
        find_variable_value(sys.argv)
    except KeyboardInterrupt:
        pass
