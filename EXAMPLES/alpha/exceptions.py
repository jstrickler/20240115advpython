import logging

logging.basicConfig(
    level=logging.DEBUG,
)

file_path = "DATA/dingdong.txt"

try:
    logging.debug("file path is %s", file_path)
    with open(file_path) as file_in:
        contents = file_in.read()
except (FileNotFoundError, PermissionError) as err:
    logging.error(err)
except NotADirectoryError as err:
    pass

nums = [800, 80, 1000, 0, 32, -4, 255, -8, 400, 5, 5000]

for num in nums:
    logging.debug("Number is %d", num)
    try:
        result = 37 / num
    except ZeroDivisionError as err:
        logging.error(err)
    else:  # if no exceptions
        print(result)


print("ALL DONE")

