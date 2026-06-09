import logging

logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR
)

class InvalidMarkError(Exception):
    pass

student_name = input("Enter Student Name: ")

try:
    mark = int(input("Enter Student Mark: "))

    if mark < 0 or mark > 100:
        raise InvalidMarkError("Marks must be between 0 and 100")

    if mark >= 50:
        print(student_name, "has PASSED")
    else:
        print(student_name, "has FAILED")

except InvalidMarkError as e:
    print("Error:", e)
    logging.error(e)

except ValueError:
    print("Please enter numbers only.")
    logging.error("Invalid mark entered")