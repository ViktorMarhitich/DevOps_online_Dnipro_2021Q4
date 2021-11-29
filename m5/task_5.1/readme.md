Part 1
1)  Log in to the system as root.  
sudo su
OR
sudo -i
2) Use the passwd command to change the password. Examine the basic parameters of the command. What system file does it change *?
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/pswd_upd.png)
Ubuntu Linux account information stored in a file named /etc/passwd and encrypted password in /etc/shadow.
3)  Determine the users registered in the system, as well as what commands they execute. What additional information can be gleaned from the command execution?
w
who
lastlog
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/lastlog.png)
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/w.png)
4) Change personal information about yourself.
chfn
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/change_info.png)
5) Become familiar with the Linux help system and the man and info commands. Get help on the previously discussed commands, define and describe any two keys for these commands. Give examples.
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/w_help.png)
6) Explore the more and less commands using the help system. View the contents of files .bash* using commands.
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/less_help.png)
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/more_help.png)
Read .bashrc file:
less .bashrc
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/bashrc_file.png)
7) * Describe in plans that you are working on laboratory work 1. Tip: You should read the documentation for the finger command.
man finger
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/man_finger.png)
8) * List the contents of the home directory using the ls command, define its files and directories. Hint: Use the help system to familiarize yourself with the ls command.
ls -lha --group-directories-first
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/home_directory.png)
