# creating, reading, and writing the file
def main():
    # 1. open a file for writing and creating it, id it does not exist
    createFile = open("newFile.txt", "w+")

    # We can append the lines in existing file
    appendFile = open("newFile.txt", "a+")

    # Read file mode "r"

    readFile = open("newFile.txt", "r")

    # write some line of code for writing the data in file

    for i in range(10):
        createFile.write("This is appended line %d\r\n" % (i + 1))

    # close the file when it done writing
    createFile.close()

    if readFile.mode == "r":
        # use the read function to read the file
        contents = readFile.read()
        print(contents)
    

if __name__ == "__main__":
    main()