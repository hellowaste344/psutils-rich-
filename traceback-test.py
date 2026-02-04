import traceback
import sys

###########
A = [1,2,3,4]

try:
    value = A[4]
except:
    traceback.print_exc()


print("end of program")
#############
a = 3
b = 0
try:
    a / b
except Exception as e:
    exc_type, exc_value, exc_tb = sys.exc_info()
    tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
    print(''.join(tb.format_exception_only()))
#######################3
def calla(f):
    callb(f)

def callb(f):
    f()

def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    print(''.join(summary.format()))

calla(f)