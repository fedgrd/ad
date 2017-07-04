import time

print '\n' + "Hello Adele!" + '\n' + " " + '\n' + "Welcome to this script. In order to proceed you will be asked to answer five questions." + '\n'

x = raw_input("Type Y to continue N to close this program: ").lower()

print '\n'
if x == "y":
    print "Good, let me walk you through the first question." + '\n'
else:
    print "Goodbye, see you next time!"

print "1 fo 5" + '\n'
print "Given the following equation (x+3)(x-2)(x+5), please specify any of its roots." + "\n"

x_1 = raw_input("Type a value for one of the roots of the equation: ").lower()

if x_1 == "-3" or x_1 == "2" or x_1 == "-5":
    print " "
    print "Correct, good job!"
    print " "
    print "You will now proceed to the next question."
else:
    print "Wrong! Please start over."
