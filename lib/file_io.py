# write
def write_file(file_name, file_content):
    file_name = file_name.with_suffix(".txt")
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(file_content)


# append
def append_file(file_name, append_content):
    file_name = file_name.with_suffix(".txt")
    with open(file_name, mode="a", encoding="utf-8") as file:
        file.write(append_content)


# read
def read_file(file_name):
    file_name = file_name.with_suffix(".txt")
    with open(file_name, mode="r", encoding="utf-8") as file:
        return file.read()
