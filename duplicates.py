import os


def fill_list(path_to_file):
    list_files = []
    if not os.path.exists(path_to_file):
        return None
    for path_to_directory, folder, files in os.walk(path_to_file):
        for file_name in files:
            path = os.path.join(path_to_directory, file_name)
            list_files.append(path)
    return list_files


def are_files_duplicates(filled_list_one, filled_list_two):
    duplicate_list = []
    for file_names_list_one in filled_list_one:
        (directory_list_one, file_name_list_one) = os.path.split(file_names_list_one)
        size_list_one = os.path.getsize(os.path.join(directory_list_one, file_name_list_one))
        for file_names_list_two in filled_list_two:
            try:
                (directory_list_two, file_name_list_two) = os.path.split(file_names_list_two)
                size_list_two = os.path.getsize(os.path.join(directory_list_two, file_name_list_two))
                if file_name_list_one == file_name_list_two and size_list_one == size_list_two:
                    full_name_file_two = os.path.join(directory_list_two, file_name_list_two)
                    duplicate_list.append(full_name_file_two)
            except FileNotFoundError:
                pass
    return duplicate_list


def remove_duplicate(list_of_duplicate_files):
    try:
        for file_name in list_of_duplicate_files:
            os.remove(file_name)
            print("Дубликат удален который хранился по следующему пути = {0}".format(file_name))
    except PermissionError:
        pass


def chmod_file(list_of_duplicate_files):
    try:
        for file_name in list_of_duplicate_files:
            os.chmod(file_name, 0o666)
    except PermissionError:
        pass


if __name__ == '__main__':
    folder_one = input()
    folder_two = input()
    files_in_folder_one = fill_list(folder_one)
    files_in_folder_two = fill_list(folder_two)
    duplicates = are_files_duplicates(files_in_folder_one, files_in_folder_two)
    chmod_file(duplicates)
    remove_duplicate(duplicates)
