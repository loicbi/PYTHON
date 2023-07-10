import paramiko
import datetime

# Define connection parameters
hostname = jv_server
username = 'ScottDirectories'
pwd = jv_pwd_scotts

path = jv_path

try:
    transport = paramiko.Transport(hostname, 22)
    transport.connect(username=username, password=pwd)
    sftp = transport.open_sftp_client()

    actual_date = datetime.datetime.today()
    # get the list of files and folders in the specified directory
    myListSftp = sftp.listdir(path)

    # filter the list to only have csv files
    csv_files = [f for f in myListSftp if f.endswith('.csv')]

    # get the modification date of each file
    for f in csv_files:
        file_name = path + '/' + f
        file_attr = sftp.stat(file_name)
        date_modified = datetime.datetime.fromtimestamp(file_attr.st_mtime)
        date_format = date_modified.strftime('%Y-%m-%d')
        number_days = (actual_date - date_modified).days

        # Delete the file if number_days == jv_save_days
        if number_days == 0:
            sftp.remove(file_name)
        else:
            print('save')

        print('file_name :', file_name)
        print('number_days :', number_days)

    # close sftp connexion
    sftp.close()
    transport.close()


except paramiko.ssh_exception.SSHException as e:
    print('SSH error, you need to add the public key of your remote in your local known_hosts file first.', e)
