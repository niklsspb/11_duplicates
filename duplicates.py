import os


def fill_list(file_path):
    file = []
    if not os.path.exists(file_path):
        return None
    for d, dirs, files in os.walk(file_path):
        for f in files:
            path = os.path.join(d, f)
            file.append(path)
    return file


def are_files_duplicates(dir_list_one, dir_list_two):
    duplicate = []
    for f1 in dir_list_one:
        (dirname_list_one, fname_list_one) = os.path.split(f1)
        size_list_one = os.path.getsize(os.path.join(dirname_list_one, fname_list_one))
        for f2 in dir_list_two:
            try:
                (dirname_list_two, fname_list_two) = os.path.split(f2)
                size_list_two = os.path.getsize(os.path.join(dirname_list_two, fname_list_two))
                if fname_list_one == fname_list_two and size_list_one == size_list_two:
                    full_name_two = os.path.join(dirname_list_two, fname_list_two)
                    duplicate.append(full_name_two)
            except FileNotFoundError:
                pass
    return duplicate


def remove_duplicate(file):
    try:
        print(file)
        for f in file:
            os.chmod(f, 0o666)
            os.remove(f)
            print("Дубликат удален который хранился по следующему пути = {0}".format(f))

    except PermissionError:
        print("PermissionError")
        print("Try chmod 666")

if __name__ == '__main__':
    folder_one = input()
    folder_two = input()
    files_in_folder_one = fill_list(folder_one)
    files_in_folder_two = fill_list(folder_two)
    duplicates = are_files_duplicates(files_in_folder_one, files_in_folder_two)
    remove_duplicate(duplicates)
