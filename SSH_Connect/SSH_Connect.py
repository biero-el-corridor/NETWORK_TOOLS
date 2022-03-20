# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 10:10:41 2022

@author: ecordier
Name: Automated Remote Ssh Command Testing  ARSCT

Nedeed: 
    argpars for:
        port connetions
https://phoenixnap.com/kb/install-pip-windows
"""

from ast import arg
import paramiko
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-DBfile', help='put the DB file name',type=str)
parser.add_argument('-o', help='put the name of the output fie',type=str)
args = parser.parse_args()

def Connect_Try(ip,user,pwd,port,command):
    CountCMDLine = 0
    TotalCMDline = len(command)
    try:
        #connections sur la machine distante
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=user, password=pwd, timeout=4)
    except:
        print("cannot reatch the ip or ssh service of the IP \n")    
    
    stdin, stdout, stderr = ssh.exec_command("id")
    lines = stdout.readlines()
    print(f' the IP {ip} can connect. Here your id {lines} \n')
    
    with open(args.o, "a") as res: 
        res.write("\n")
        res.write("*******************************************")
        res.write("\n")
        res.write(f'begening of the command impout on the IP :{ip}\n')
        res.write("*******************************************")
        res.write("\n")
        if (len(command) != 1):
            
            #si il y a plusieur command
            while(CountCMDLine != TotalCMDline): 
                stdin, stdout, stderr = ssh.exec_command(str(command[CountCMDLine]))
                lines = stdout.readlines()
                print(lines)
                #va écrire dans le fichier le résultat de la commande
                res.write(f'result of the {str(command[CountCMDLine])} command on the IP: {ip}\n')
                res.write(str(lines))
                res.write("\n")
                res.write("\n")

                CountCMDLine += 1

        else: 
            #si il n'y a qu'une commande donnée en paramétre
            stdin, stdout, stderr = ssh.exec_command(str(command[0]))
            lines = stdout.readlines()
            print(lines)
            res.write(f'result of the {str(command)} command on the IP: {ip}\n')
            res.write(str(lines))

##1er test avec seulement la list des ip
if __name__ == "__main__":
    with open(args.DBfile, "r") as DBfile: 
        lines = DBfile.readlines()
        
        for line in lines: 
            #line.split("||")
            line = str(line).split("||")
            Name = line[0]
            IP = line[1]
            CRED = line[2]
            CRED = CRED.split(";")
            USER = CRED[0]
            PWD = CRED[1]
            PORT = line[3]
            Command = line[4:-1]
            print(len(Command))
            
            #sanitize chek of the IP string
            if "." not in IP and IP[0].isdigit() == False :
                
                print("your input dont have the standart IP format.")
            try:
                Connect_Try(IP,USER,PWD,PORT,Command)
            except: 
                print(f'the password / username number  is not the good for this ip adress')