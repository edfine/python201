#from calculate_module import calculate
import calculate_module as cm

import sys
if len(sys.argv) >= 4:
    print(cm.calculate(sys.argv[1], sys.argv[2], sys.argv[3]))
else:
    print("Usage: {} operand1 operand2 operator".format(sys.argv[0]))
