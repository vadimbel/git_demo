import functions_module as fm


def main():
    import sys

    file_content = sys.argv
    fm.passwords_to_check(file_content[1:])


main()
