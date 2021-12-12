# Part1
========

## 1. How many states could has a process in Linux?

Five possible states:

 - Running or Runnable (R)
 - Uninterruptible Sleep (D)
 - Interruptable Sleep (S)
 - Stopped (T)
 - Zombie (Z)

## 2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process.

Pstree command in Linux that shows the running processes as a tree which is a more convenient way to display the processes hierarchy and makes the output more visually appealing
   
   `pstree -h viktor`

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/pstree.png)

## 3. What is a proc file system?

    Proc file system (procfs) is virtual file system created on fly when system boots and is dissolved at time of system shut down.
   
   `ls -l /proc`

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/proc.png)

## 4. Print information about the processor (its type, supported technologies, etc.).

   `lscpu`

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/lscpu.png)

## 5. Use the ps command to get information about the process. The information should be as follows: the owner of the process, the arguments with which the process was launched for execution, the group owner of this process, etc.

   `ps -au`

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/psau.png)

## 6. How to define kernel processes and user processes?

A kernel process (kproc) exists only in the kernel protection domain and differs from a user process in the ways listed down.

   - It is created using the ***creatp*** and ***initp*** kernel services.
   - It executes only within the kernel protection domain and has all security privileges.
   - It can call a restricted set of system calls and all applicable kernel services. For more information, see ***System Calls Available*** to ***Kernel Extensions***.
   - It has access to the global kernel address space (including the kernel pinned and pageable heaps), kernel code, and static data areas.
   - It must poll for signals and can choose to ignore any signal delivered, including a kill signal.
   - Its text and data areas come from the global kernel heap.
   - It cannot use application libraries.
   - It has a process-private region containing only the u-block (user block) structure and possibly the kernel stack.
   - Its parent process is the process that issued the creatp kernel service to create the process.
   - It can change its parent process to the init process and can use interrupt disable functions for serialization.
   - It can use locking to serialize process-time access to critical data structures.
   - It can only be a 64–bit process in the 64–bit kernel.

A kernel process controls directly the kernel threads. Because kernel processes are always in the kernel protection domain, threads within a kernel process are kernel-only threads. For more information on kernel threads, see Understanding Kernel Threads.

A kernel process inherits the environment of its parent process (the one calling the creatp kernel service to create it), but with some exceptions. The kernel process does not have a root directory or a current directory when initialized. All uses of the file system functions must specify absolute path names.

Kernel processes created during phase 1 of system boot must not keep any long-term opens on files until phase 2 of system boot or run time has been reached. This is because Base Operating System changes root file systems between phase 1 and phase 2 of system boot. As a result, the system crashes if any files are open at root file system transition time.

## 7. Print the list of processes to the terminal. Briefly describe the statuses of the processes. What condition are they in, or can they be arriving in?

   `ps -aux`

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/psaux.png)

## 8. Display only the processes of a specific user. 

   `ps -au viktor`

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/psauviktor.png)

## 9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?

   - pgrep
   - pstree
   - top
   - proc 

## 10. What information does top command display?

`top` command is used to show the ***Linux processes***. It provides a dynamic real-time view of the running system. Usually, this command shows the summary information of the system and the list of processes or threads which are currently managed by the ***Linux Kernel***.

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/top.png)

## 11. Display the processes of the specific user using the top command.

   `top -u viktor`

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/topuviktor.png)

## 12. What interactive commands can be used to control the top command? Give a couple of examples.

- d | s  :Change-Delay-Time-interval
- E  :Enforce-Summary-Memory-Scale in Summary Area
- g  :Choose-Another-Window/Field-Group
- H  :Threads-mode toggle

## 13. Sort the contents of the processes window using various parameters (for example, the amount of processor time taken up, etc.)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/topname.png)
![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m5/task_5.3/images/topmem.png)

## 14. Concept of priority, what commands are used to set priority?

`nice`

Sometimes you might want to change the priority of a process in Linux. For example, you might run a process that is very important and you want it to finish quickly. You can change the process priority using the `nice` command and give that process more CPU time.

`renice`

The `renice` program can be used to change the priority of a process that is already running.

## 15. Can I change the priority of a process using the top command? If so, how?

To change the priority of process in `top` command, we need ad an `-r`key.

## 16. Examine the kill command. How to send with the kill commandprocess control signal? Give an example of commonly used signals.

To kill some process we can for example enter his PID.

`kill `***PID_number***

## 17. Commands jobs, fg, bg, nohup. What are they for? Use the sleep, yes command to demonstrate the process control mechanism with fg, bg.



# Part2
========

## 1. Check the implementability of the most frequently used OPENSSH commands in the MS Windows operating system. (Description of the expected result of the commands + screenshots: command – result should be presented)

## 2. Implement basic SSH settings to increase the security of the client-server connection (at least 

## 3. List the options for choosing keys for encryption in SSH. Implement 3 of them.

## 4. Implement port forwarding for the SSH client from the host machine to the guest Linux virtual machine behind NAT.

## 5*. Intercept (capture) traffic (tcpdump, wireshark) while authorizing the remote client on the server using ssh, telnet, rlogin. Analyze the result. 