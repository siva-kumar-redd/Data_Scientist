class InvalidMarksError(Exception):
    pass

marks = int(input())

if marks<0:
    raise InvalidMarksError("invalid marks")
if marks>100:
    raise InvalidMarksError("invalid marks")

print("Valid marks")

