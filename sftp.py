import pysftp
import paramiko

# Define connection parameters or already have?
hostname = 'sftp.mckesson.ca'
username = 'ScottDirectories'
password = '48G69Yfm'
port = 80
private_key = 'gggg'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

class My_Connection(pysftp.Connection):
    def __init__(self, *args, **kwargs):
        self._sftp_live = False
        self._transport = None
        super().__init__(*args, **kwargs)

from datetime import datetime

try:
    with My_Connection(hostname, username=username, password=password, cnopts=cnopts) as sftp:
        myListSftp = sftp.listdir()
        print(f'myListSftp ===',myListSftp)

except paramiko.ssh_exception.SSHException as e:
    print('SSH error, you need to add the public key of your remote in your local known_hosts file first.', e)




# # connect to the server
# with pysftp.Connection(host=hostname, username=username, password=password, port=port) as sftp:
# # Define the file path
# file_path = ''
#
# # delete the file from the server
# sftp.remove(file_path)
