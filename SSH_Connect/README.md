# H_TOOLS

## SSH_Automations

the purpose of this script is to automate ssh connexions and command shell on the remote hosts. 
this script can be use for the following purpose
- Tcheck the versions of a service 
- C'mon you can do wathever you whant it is literaly a ssh connexions. 

The script take one argument: the name of the DB file. 

the DB file need to conatain the folowing informations in the following order in the following format. 

NAME||IP||USER;PASSWORD||PORT||command1||command2||
NAME||IP||USER;PASSWORD||PORT||command1||command2||
NAME||IP||USER;PASSWORD||PORT||command1||command2||

exemple of use 
- python.exe .\SSH_Connect.py -DBfile DBfile.txt -o out.txt