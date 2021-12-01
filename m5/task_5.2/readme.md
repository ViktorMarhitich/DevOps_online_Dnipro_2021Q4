1) Analyze the structure of the /etc/passwd and /etc/group file, what fields are present in it, what users exist on the system? Specify several pseudo-users, how to define them?

etc/passwd

`viktor:x:1000:1000:viktor,35,,0663423619:/home/viktor:/bin/bash`

 ------ | ------
 viktor | username 
 x | password 
 1000 | userID 
 1000 | groupID 
 viktor,35,,0663423619 | userID info (GEKOS) 
 /home/viktor | user home directory 
 /bin/bash | command/shell 

etc/group

adm:x:4:syslog,viktor

adm           - group name
x             - password
4             - groupID (GID)
syslog,viktor - group list: It is a list of user names of users who are members of the group. The user names, must be separated by commas

Pseudo user (UID 1-499)
Pseudo users are related to system and program services

    Any Linux system has these pseudo users by default
    Mail news games, Apache FTP, MySQL and sshd are related to the process of Linux system

    Pseudo users usually do not need or cannot log in to the system
    There can be no host directory

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/etc_passwd.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/etc_group.png)

2) What are the uid ranges? What is UID? How to define it?

UID stands for user identifier. A UID is a number assigned to each Linux user. It is the user’s representation in the Linux kernel. The UID is used for identifying the user within the system and for determining which system resources the user can access.

Superuser (root uid = 0)
General user (UID 500-60000)
Pseudo user (UID 1-499)

The id command in Linux will display the UID, GID and groups your current user belongs to

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/id.png)

3) What is GID? How to define it?

Groups in Linux are defined by GIDs (group IDs):
GID 0 (zero) is reserved for the root group.
GID 1–99 are reserved for the system and application use.
GID 100+ allocated for the user’s group.

| cat /etc/group | grep adm

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/group_find.png)

4) How to determine belonging of user to the specific group? 

| groups viktor

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/groups_viktor.png)

5) What are the commands for adding a user to the system? What are the basic parameters required to create a user?

if we need add new user:

| sudo useradd testuser

to enter system by new user we need create him a password:

| sudo passwd testuser

if we need add new user and create home directory:

| sudo useradd -m testuser

creating a user with specific home directory:

| sudo useradd -m -d /path_name testuser

creating a user with specific User ID:

| sudo useradd -u 1500 testuser

creating a user with an expiry date:

| sudo useradd -e 2021-12-01 testuser

creating a user and assign multiple groups:

| sudo useradd -g users -G wheel,developers testuser

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/useradd.png)

6) How do I change the name (account name) of an existing user?

| sudo usermod -l ttuser testuser

7) What is skell_dir? What is its structure?

Directory /etc/skel/ (skel is derived from the “skeleton”) is used to initiate home directory when a user is first created. “skeleton” directory is defined in /etc/default/useradd file.

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/skel.png)

8) How to remove a user from the system (including his mailbox)?

| sudo userdel -r ttuser

9) What commands and keys should be used to lock and unlock a user account?

first way using passwd command: 
   
   to lock:

| sudo passwd -l ttuser

   to unlock:

| sudo passwd -u ttuser

second way using usermod command:

   to lock:

| sudo usermod -L ttuser

   to unlock:

| sudo usermod -U ttuser

10) How to remove a user's password and provide him with a password-free login for subsequent password change?

To do so, we need open the sudoers configuration file with sudo visudo, and add the following line to the file:

| ttuser ALL=(ALL) NOPASSWD:ALL

Then delete the password for your user by running this command:

| sudo passwd -d `ttuser`

11) Display the extended format of information about the directory, tell about the information columns displayed on the terminal.

If I correctly understand this task we need Long Output Format of ls command

| ls -l

displays permissions, links, owner, group, size, time, name

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/extend.png)

12) What access rights exist and for whom (i. e., describe the main roles)? Briefly describe the acronym for access rights.

Permission settings grouped in a string of characters (-, r, w, x) classified into four sections:

- File type. There are three possibilities for the type. It can either be a regular file (–), a directory (d) or a link (i).
- File permission of the user (owner)
- File permission of the owner’s group
- File permission of other users

The characters r, w, and x stand for read, write, and execute.

Instead of letters, the octal format represents privileges with numbers:

- r(ead) has the value of 4
- w(rite) has the value of 2
- (e)x(ecute) has the value of 1
- no permission has the value of 0

The privileges are summed up and depicted by one number. Therefore, the possibilities are:

- 7 – for read, write, and execute permission
- 6 – for read and write privileges
- 5 – for read and execute privileges
- 4 – for read privileges

13) What is the sequence of defining the relationship between the file and the user?

By default, the owner of a file is the user who created it and the group assigned to a file is the primary group of the user. 

14) What commands are used to change the owner of a file (directory), as well as the mode of access to the file? Give examples, demonstrate on the terminal.

| sudo chown root hard_link_labwork2

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/chown.png)

15) What is an example of octal representation of access rights? Describe the umask command.

When a file is created, the permission flags are set according to the file mode creation mask, which can be set using the umask command. The file mode creation mask (sometimes referred to as "the umask") is a three-digit octal value whose nine bits correspond to fields 2-10 of the permission flags. 

Octal value	Binary representation	Meaning
0	                 0 	            No read, write, and execute permissions (—)
1	                 1	            Only execute permission (–x)
2	                 10	            Only write permission (-w-)
3	                 11	            Write and execute permissions (-wx)
4	                100	            Only read permission (r–)
5	                101	            Read and execute permissions (r-x)
6	                110	            Read and write permissions (rw-)
7	                111 	        Read, write, and execute permissions (rwx)

16) Give definitions of sticky bits and mechanism of identifier substitution. Give an example of files and directories with these attributes.

The sticky bit was initially introduced to ‘stick’ an executable program’s text segment in the swap space even after the program has completed execution, to speed up the subsequent runs of the same program. However, these days the sticky bit means something entirely different.

When a directory has the sticky bit set, its files can be deleted or renamed only by the file owner, directory owner and the root user.

| mkdir allAccess
| chmod 777 allAccess/
| cd allAccess
| touch file1.txt
| cd -
| sudo adduser guest
| sudo adduser guest1
| su guest
| cd allAccess
| touch file2.txt
| exit
| su guest1
| cd allAccess
| touch file3.txt
| exit
| cd allAccess
| chmod 777 file1.txt
| sudo chmod 777 file2.txt
| sudo chmod 777 file3.txt
| cd -
| chmod +t allAccess/
| su guest
| mv /home/viktor/allAccess/file2.txt /home/viktor/allAccess/file3.txt

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/bity_stick.png)

17) What file attributes should be present in the command script?

The files and directories can have following attributes:

a - append only
c - compressed
d - no dump
e - extent format
i - immutable
j - data journaling
s - secure deletion
t - no tail-merging
u - undeletable
A - no atime updates
D - synchronous directory updates
S - synchronous updates
T - top of directory hierarchy

| lsattr

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/attributes.png)