# import statistics
# print(statistics.mean([100,90,33,44,22,4]))

# import sys
# print(f"Hello my name is {sys.argv[1]} {sys.argv[2]}")
# print(sys.argv[0])

# import sys
# try:
#     print("Hello my name is ", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# import sys
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print(f"My name is {sys.argv[1]}")

# import sys
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) >2:
#     sys.exit("Too many arguments")

# print(f"Hello my name is {sys.argv[1]}")

import sys
if len(sys.argv)<2:
    sys.exit("Too few Arguments")

# for arg in sys.argv:
#     print("Hello my name is ", arg)

# print(sys.argv)

for arg in sys.argv[1:]:
    print("Hello my name is, ", arg)