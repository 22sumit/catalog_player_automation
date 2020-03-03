import paramiko
import libs.config as config


def ssh_connect(ip, username, password):
    global ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    print("ssh connection established !!")

def ssh_stop_service(stop_ip):
    sshCmd = "ssh mdmsadmin@" + stop_ip + "\n"
    print("Logging into " + sshCmd)
    global chan
    chan = ssh.invoke_shell()

    chan.send(sshCmd)
    buffRead = ''
    while not buffRead.endswith('\'s password: '):
        resp = chan.recv(9999).decode('utf-8')
        print(resp)
        buffRead += resp
        if (buffRead.__contains__("Are you sure you want to continue connecting (yes/no)?")):
            chan.send("yes\n")
            buffRead = ''

    chan.send('monaco1234\n')
    buffRead = ''
    mapConsole = ':~ #'
    while not buffRead.__contains__(mapConsole):
        resp = chan.recv(9999).decode('utf-8')
        print(resp)
        buffRead += resp.rstrip()

    cp_stop = "sudo service catalog_player_service stop\n"
    print("Stopping CPS : " + cp_stop)
    chan.send(cp_stop)
    # chan.send("sudo hostname\n")
    buffRead = ''
    while not buffRead.__contains__('password for mdmsadmin:'):
        resp = chan.recv(9999).decode('utf-8')
        buffRead += resp

    chan.send("monaco1234\n")
    buffRead = ''
    while not buffRead.__contains__(mapConsole):
        resp = chan.recv(9999).decode('utf-8')
        print(resp)
        buffRead += resp

def ssh_start_service():
    cp_start = "sudo service catalog_player_service start\n"
    print("Starting CPS : " + cp_start)
    chan.send(cp_start)
    # buffRead = ''
    # while not buffRead.__contains__('password for mdmsadmin:'):
    #     resp = chan.recv(9999).decode('utf-8')
    #     buffRead += resp
    #
    # chan.send("monaco1234\n")
    buffRead = ''
    mapConsole = ':~ #'
    while not buffRead.__contains__(mapConsole):
        resp = chan.recv(9999).decode('utf-8')
        print(resp)
        buffRead += resp

def ssh_close(ip, chan_ip):
    chan.close()
    print("Closing the terminal connection for ", chan_ip)

    print("Closing the SSH connection to the ", ip)
    ssh.close()