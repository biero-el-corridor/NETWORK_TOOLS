# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 10:10:41 2022

@author: ecordier

Name: Automated Remote Ssh Command Testing  ARSCT

Nedeed: 
    argpars for:
        port connetions

"""

import paramiko
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-IPfile', '--IPfile' , help='put the absolute or relative path to the file that contain your IP list',type=str)
parser.add_argument('-PWDfile', '--PWDfile' , help='put the absolute or relative path to the file that contain your Password ',type=str)
parser.add_argument('-CMDfile', '--CMDfile' , help='put the absolute or relative path to the file that contain your command',type=str)

args = parser.parse_args()


#use a funtions to open the file 
def Readlines(FileName, Type):
    
    #this table containe eatch line of the file
    FTable = []
    
    with open(FileName, Type) as Flist:
        Flines = Flist.readlines()
        
        for Fline in Flines:
            #the tab is going to be fill with the lines of the file
            FTable.append(Fline)
            
        
        return FTable
            

def Connect_Try(IP,user,pas,command):
    host = IP
    username = user
    password = pas
    port = "22"
    command = command
    host = host.replace("\n", '')
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, port, username, password)
        
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print("")
        print(f' the IP {host} can connect. Here your id {lines} \n')
        
        
        #####################################################"
        ############CMDFile read sections####################
        #####################################################
        CMDline = Readlines(args.CMDfile, "r")
        CountCMD  = 0
        LenOfCMDLines = len(CMDline)
        #####################################################
        #####################################################
        
        while CountCMD != LenOfCMDLines:
            
            stdin, stdout, stderr = ssh.exec_command(CMDline[CountCMD])
            lines = stdout.readlines()
            
            print(f' (root)# {CMDline[CountCMD]} \n')
            print(str(lines))
            print('\n')
            
            CountCMD += 1
        
    except:
        print("cannot reatch the ip or ssh service of the IP \n")
        


            

##1er test avec seulement la list des ip
if __name__ == "__main__":
    #####################################################"
    ############IPFile read sections#####################
    #####################################################

    IPlines = Readlines(args.IPfile, "r")
    CountIPLen  = 0
    LenOfIPLines = len(IPlines)
    
    ######################################################
    ######################################################
    
    #####################################################"
    ############PWDFile read sections#####################
    #####################################################   
    
    PWDlines = Readlines(args.PWDfile, "r")
    CountPWDLen  = 0
    LenOfPWDLines = len(PWDlines)
    
    ######################################################
    ######################################################
    
    while CountIPLen != LenOfIPLines:
        IPline = IPlines[CountIPLen]
        IPline = IPline.replace("\n", '')
        
        #sanitize chek of the IP string
        if "." not in IPline and IPline[0].isdigit() == False :
            
            print("your input dont have the standart IP format.")
            break
        
        while CountPWDLen != LenOfPWDLines:
            Credential = PWDlines[CountPWDLen].split(";")
            Username = Credential[0]
            Password = Credential[1]
            print(IPline)
            try:
                Connect_Try(IPline,Username,Password,"id")
                CountPWDLen += 1
            except: 
                print(f'the password / username number {CountPWDLen} is not the good for this ip adress')
            

        CountPWDLen = 0
        CountIPLen += 1
    

   


        
        
