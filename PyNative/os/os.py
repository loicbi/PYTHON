import shutil

import os

# Get the list of all files and directories
# in the root directory
path_working_gs1 = os.getcwd()

directory = "CANADA_DATAHUB/MATILLION_PROJECT/DEV/GS1/MEDIA"
path_working_gs1 = os.path.join(path_working_gs1, directory)
print(f'path_working_gs1:{path_working_gs1}')
# mode
mode = 0o666
# create folder GS1

if os.path.exists(path_working_gs1) is False:
    os.makedirs(path_working_gs1, mode)
print("Directory '% s' created" % directory)

dir_list = os.listdir(path_working_gs1)

print("Files and directories in '", path_working_gs1, "' :")

# print the list
print(dir_list)



def delete(path):
    """path could either be relative or absolute. """
    # check if file or directory exists
    if os.path.isfile(path) or os.path.islink(path):
        # remove file
        os.remove(path)
    elif os.path.isdir(path):
        # remove directory and all its content
        shutil.rmtree(path)
    else:
        raise ValueError("Path {} is not a file or dir.".format(path))
print(path_working_gs1)
delete(path_working_gs1)
