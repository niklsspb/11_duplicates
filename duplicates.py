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
    for f1 in dir_list_one:
        (dirname_list_one, fname_list_one) = os.path.split(f1)
        size_list_one = os.path.getsize(os.path.join(dirname_list_one, fname_list_one))
        for f2 in dir_list_two:
            try:
                (dirname_list_two, fname_list_two) = os.path.split(f2)
                size_list_two = os.path.getsize(os.path.join(dirname_list_two, fname_list_two))
                if fname_list_one == fname_list_two and size_list_one == size_list_two:
                    try:
                        full_name_one = os.path.join(dirname_list_one, fname_list_one)
                        full_name_two = os.path.join(dirname_list_two, fname_list_two)
                        print("Find duplicate dir_one = {0} where_delete_dir = {1} ".format(full_name_one, full_name_two))
                    except PermissionError:
                        pass
                    finally:
                        os.chmod(full_name_two, 0o666)
                        os.remove(full_name_two)
                        print("Duplicate removed {0}".format(full_name_two))
            except FileNotFoundError:
                pass


if __name__ == '__main__':
    folder_one = input()
    folder_two = input()
    are_files_duplicates(fill_list(folder_one), fill_list(folder_two))
