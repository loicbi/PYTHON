import pysftp
import paramiko
from datetime import datetime

# Define connection parameters or already have?
hostname = 'sftp.mckesson.ca'
username = 'ScottDirectories'
password = '48G69Yfm'
port = 80
# private_key = 'gggg'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


class My_Connection(pysftp.Connection):
    def __init__(self, *args, **kwargs):
        self._sftp_live = False
        self._transport = None
        super().__init__(*args, **kwargs)


try:
    with My_Connection(hostname, username=username, password=password, cnopts=cnopts) as sftp:
        myListSftp = sftp.listdir()
        print(f'myListSftp ===', myListSftp)

        actual_date = datetime.today()

        for file_name in myListSftp:
            file_attr = sftp.stat(file_name)
            date_modified = datetime.fromtimestamp(file_attr.st_mtime)
            date_format = date_modified.strftime('%Y-%m-%d')
            number_days = (actual_date - date_modified).days
            print(
                f'file_name: {file_name} || date_modified: {date_modified} || date_format: {date_format} || number_days: {number_days},')
            if number_days == 58585858:
                # sftp.remove(file_name)
                print(f'remove file {file_name}')
            else:
                print('save')

                print('file_name :', file_name)
                print('number_days :', number_days)

                print('myListSftp :', myListSftp)

except paramiko.ssh_exception.SSHException as e:
    print('SSH error, you need to add the public key of your remote in your local known_hosts file first.', e)

# # connect to the server
# with pysftp.Connection(host=hostname, username=username, password=password, port=port) as sftp:
# # Define the file path
# file_path = ''
#
# # delete the file from the server
# sftp.remove(file_path)


# import pysftp
# import paramiko
# import datetime
#
# # Define connection parameters or already have?
# hostname = 'sftp.mckesson.ca'
# username = 'ScottDirectories'
# password = '48G69Yfm'
# port = 80
# #private_key = 'gggg'
#
# cnopts = pysftp.CnOpts()
# cnopts.hostkeys = None

# try:
#     with pysftp.Connection(hostname, username=username, password=password, cnopts=cnopts) as sftp:
#
#         actual_date = datetime.datetime.today()
#         myListSftp = sftp.listdir()
#
#         for file_name in myListSftp:
#             file_attr = sftp.stat(file_name)
#             date_modified = datetime.datetime.fromtimestamp(file_attr.st_mtime)
#             date_format = date_modified.strftime('%Y-%m-%d')
#             number_days = (actual_date - date_modified).days
#             if number_days == 0:
#                 sftp.remove(file_name)
#             else:
#                 print('save')
#
#                 print('file_name :', file_name)
#                 print('number_days :', number_days)
#
#                 print('myListSftp :', myListSftp)
#
# except paramiko.ssh_exception.SSHException as e:
#     print('SSH error, you need to add the public key of your remote in your local known_hosts file first.', e)
