import os

main_path = ''


extensions = {

    'Video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv',
              'rm', 'swf', 'vob'],

    'Data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml'],

    'Audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],

    'Image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],

    'Archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

    'Text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

    '3D': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],

    'Presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

    'Spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

    'Font': ['otf', 'ttf', 'fon', 'fnt'],

    'Gif': ['gif'],

    'Exe': ['exe'],

    'Bat': ['bat'],

    'Apk': ['apk']
}



def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            os.rmdir(p)


def sorter(main_path = ''):
        try:
            create_folders_from_list(main_path, extensions)
            sort_files(main_path)
            remove_empty_folders(main_path)
            print(f" Files in {main_path} have been sorted")
        except FileNotFoundError:
            print(f'Path {main_path} is incorrect. Please enter correct path')