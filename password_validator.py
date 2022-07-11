
import functions_module as fm


def main():
    import sys

    # this part checks if the second argument is '-f' -> we should read the passwords from a file
    if len(sys.argv) > 1 and sys.argv[1] == "-f":
        # there is a file path
        if len(sys.argv) == 3:
            # second argument is '-f' , third argument supposed to be a valid path to a text file
            try:
                file = open(sys.argv[2])
            except OSError:
                print(f"Could not open/read file: {sys.argv[2]}")
                sys.exit()

            file_input = file.read()
            file_input_split = file_input.split()
            fm.passwords_to_check(file_input_split)
            sys.exit()
    else:
        file_content = sys.argv
        fm.passwords_to_check(file_content[1:])
        sys.exit()


main()
