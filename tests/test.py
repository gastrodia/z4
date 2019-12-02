import sys
sys.path.append('./build/Debug')
import z4 
assert z4.__version__ == 'dev'
assert z4.add(1, 2) == 3
assert z4.subtract(1, 2) == -1
