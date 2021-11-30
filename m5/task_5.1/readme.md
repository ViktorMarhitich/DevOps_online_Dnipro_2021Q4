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

Part 2

1) Examine the tree command. Master the technique of applying a template, for example, display all files that contain a character c, or files that contain a specific sequence of characters. List subdirectories of the root directory up to and including the second nesting level.

sudo apt update
sudo apt install tree
sudo tree -P '*c*'

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/tree_c.png)

2) What command can be used to determine the type of file (for example, text or binary)? Give an example.

file .bashrc

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/file_command.png)

3) Master the skills of navigating the file system using relative and absolute paths. How can you go back to your home directory from anywhere in the filesystem?

cd
cd ~

4) Become familiar with the various options for the ls command. Give examples of listing directories using different keys. Explain the information displayed on the terminal using the -l and -a switches.

ls -a 
show all files, include hide

ls -l
show on list all details although create date, owner, size and other useful information

5) Perform the following sequence of operations: 
-  create a subdirectory in the home directory;
mkdir subdir_5_1

-  in this subdirectory create a file containing information about directories located in the root directory (using I/O redirection operations);
tree -dL 1 > subdir_5_1/folder.txt

-  view the created file;
cat subdir_5_1/folder.txt

-  copy the created file to your home directory using relative and absolute addressing.
cp subdir_5_1/folder.txt ~/

-  delete the previously created subdirectory with the file requesting removal;
rm -rI subdir_5_1

-  delete the file copied to the home directory
rm ~/folder.txt

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/fifth_point.png)

6)Perform the following sequence of operations:
-  create a subdirectory testin the home directory;
mkdir test

-  copy the .bash_historyfile to this directory while changing its name to labwork2;
cp .bash_history test/labwork2

-  create a hard and soft link to the labwork2file in the test subdirectory;
 cd test
 ln -P labwork2 hardlink
 ln -s labwork2 softlink

-  how to define soft and hard link, what do theseconcepts;
-  change the data by opening a symbolic link. What changes will happen and why
 less softlink

-  rename the hard link file to hard_lnk_labwork2;
-  rename the soft link file to symb_lnk_labwork2 file;
mv hardlink hard_link_labwork2 && mv softlink symb_link_labwork2

-  then delete the labwork2. What changes have occurred and why?
rm labwork2
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/bash_history.png)
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/task51_point6.png)

7) Using the locate utility, find all files that contain the squid and traceroute sequence.
sudo -i
apt-get update
apt-get install locate
updatedb
locate -A squid
locate -A traceroute
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/locate_command.png)

8) Determine which partitions are mounted in the system, as well as the types of these partitions.
df

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/df.png)

9) Count the number of lines containing a given sequence of characters in a given file
less -N test/hard_link_labwork2
less test/hard_link_labwork2 | wc -l

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/less_N.png)
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/count.png)

10) Using the find command, find all files in the /etc directory containing the host character sequence.
cd /etc/ && sudo find -type f -name "*host*"

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/find_host.png)

11) List all objects in /etc that contain the ss character sequence. How can I duplicate a similar command using a bunch of grep?
ls -al | grep "ss"

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/grep_ss.png)

12) Organize a screen-by-screen print of the contents of the /etc directory. Hint: You must use stream redirection operations.
ls -alh | less

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/12.png)

13) What are the types of devices and how to determine the type of device? Give examples.
Device files are denoted as the following:

c - character
b - block
p - pipe
s - socket
Character Device

These devices transfer data, but one a character at a time. You'll see a lot of pseudo devices (/dev/null) as character devices, these devices aren't really physically connected to the machine, but they allow the operating system greater functionality.

Block Device

These devices transfer data, but in large fixed-sized blocks. You'll most commonly see devices that utilize data blocks as block devices, such as harddrives, filesystems, etc.

Pipe Device

Named pipes allow two or more processes to communicate with each other, these are similar to character devices, but instead of having output sent to a device, it's sent to another process.

Socket Device

Socket devices facilitate communication between processes, similar to pipe devices but they can communicate with many processes at once.

14) How to determine the type of file in the system, what types of files are there?

ls command will show the file type as an encoded symbol found as the first character of the file permission part. In this case it is “-“, which means “regular file”. It is important to point out that Linux file types are not to be mistaken with file extensions. Let us have a look at a short summary of all the seven different types of Linux file types and ls command identifiers:

– : regular file
d : directory
c : character device file
b : block device file
s : local socket file
p : named pipe
l : symbolic link

15)* List the first 5 directory files that were recently accessed in the /etc directory. 

ls -ltr | tail -n 5

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.1/images/last_5.png)