# module = a file containing python code. May contain functions, classes, etc.
# used with module programming, which is to separate a program into parts

# import messages_module as msg

# msg.hello()
# msg.bye()

# Another way to import modules is:

from messages_module import hello,bye
# You can also use -> from modulename import * (I don't recommend this one for bigger programs because of naming conflicts)

hello()
bye()

# You can check all pre-made modules in python using:
help("modules")

