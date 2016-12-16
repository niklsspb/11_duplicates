import os


def are_files_duplicates(file_path1, file_path_2):
    files_dir_2 = []
    for d, dirs, files in os.walk(file_path_2):
        for f in files:
            path = os.path.join(d, f)
            files_dir_2.append(path)

    files_dir_1 = []
    for d, dirs, files in os.walk(file_path1):
        for f in files:
            path = os.path.join(d, f)
            files_dir_1.append(path)

    for f1 in files_dir_1:
        (dirname, fname) = os.path.split(f1)
        size = os.path.getsize(os.path.join(dirname, fname))
        for f2 in files_dir_2:
            try:
                (dirname1, fname1) = os.path.split(f2)

                size2 = os.path.getsize(os.path.join(dirname1, fname1))
                if fname == fname1:
                    if size == size2:
                        print(fname, size)
                        print("Дубликат файла удален {0}".format(os.path.join(dirname1, fname1)))
                        os.remove(os.path.join(dirname1, fname1))
            except FileNotFoundError:
                pass
folder_one = input()
folder_two = input()
are_files_duplicates(folder_one, folder_two)
if __name__ == '__main__':
    pass
