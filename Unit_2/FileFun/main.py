# 1. Open the file
# 2. Process the file (read, write, append)
# 3. Close the file
#

def load_lines_from_file(filename):
    # filename is a path to a file to open (string)
    # absolute path start with a drive, C:\, and go down
    # relative path is relative to the current working dir

    # open file
    infile = open(filename, "r")
    # reads all the lines into a list
    lines = infile.readlines()

    infile.close()
    return lines


def clean_lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()  # override because strings are imunable
    return lines


# nested list time
def restructure_data_into_table(lines):
    data = []  # going to be a 2d list
    for line in lines:
        values = line.split(", ")
        # print(values)
        data.append(values)
    return data


def pretty_print(data):
    for line in data:
        for obj in line:
            print(obj, end=" ")
        print()


def remove_whitespaces(data):
    for line in data:
        for i in range(len(line)):
            line[i] = line[i].strip()


def convert_column_to_numeric(data, column_index):
    for row in data:
        row[column_index] = float(row[column_index])


lines = load_lines_from_file("data.csv")
clean_lines = clean_lines(lines)
data = restructure_data_into_table(clean_lines)


remove_whitespaces(data)
print(data)
pretty_print(data)

# task: write a pretty_print() that prints any 2d list in a grid fashion
# task: write a remove_whitespaces(data)

header = data.pop(0)
print("header:", header)
print("data:", data)
convert_column_to_numeric(data, 2)
print("after numeric column2", data)
