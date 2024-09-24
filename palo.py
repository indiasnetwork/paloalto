import paramiko
import time
import os


def firewallpal(ip):
     try:
          ssh = paramiko.SSHClient()
          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          ssh.connect(ip,port='22',username='YourUser',password='YourPassword')
          conn = ssh.invoke_shell()
          output = conn.recv(6655000000)

          conn.send("set cli pager off\n")
          conn.send("show running security-policy\n")
          conn.send("show system info\n")
          conn.send("conf t\n")
	  conn.send("show deviceconfig system\n")
          conn.send("show address\n")
          conn.send("show address-group\n")


          time.sleep(50)          
          if conn.recv_ready():
               output = conn.recv(6555555500)
          print(output)

                               
          os.chdir("C:\\Users\\1606182\\Desktop\\Core\\")
          f = open(ip+".txt", 'a')
          f.write(output)
          f.close()

      except paramiko.AuthenticationException:
           print(ip+" password wrong")

firewallpal("172.25.136.113")
firewallpal("172.25.136.111")
firewallpal("172.25.136.197")
firewallpal("172.25.136.122")