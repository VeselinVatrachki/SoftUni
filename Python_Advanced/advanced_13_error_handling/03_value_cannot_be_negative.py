class ValueCannotBeNegative(Exception):
    pass


for i in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative


#TEST CODE                              RESULT
# 1                                  Traceback (most recent call last):
# 4                                      File ".\value_cannot_be_negative.py", line 8, in <module>
# -5                                         raise ValueCannotBeNegative
# 3                                      __main__.ValueCannotBeNegative
# 10
