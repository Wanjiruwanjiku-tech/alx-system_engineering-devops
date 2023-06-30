	BASH
	
	0x05. Processes and signals

- A PID (Process IDentifier) is a unique numerical identifier assigned to each running process in an operating system. It helps identify and manage individual processes.

- In computing, a process refers to a program or a task that is being executed by the operating system. It represents an instance of a running program and contains the program's code, data, and resources. Processes are managed by the operating system's process scheduler, which allocates system resources and determines the execution order.

- To find a process's PID, you can use various system utilities depending on the operating system you're using:

	- On Linux and Unix-like systems, you can use the `ps` command to list running processes along with their PIDs. For example, the command `ps aux | grep "process_name"` will display the PID of the process with the specified name.
	- On Windows, you can use the `Task Manager` or the `Get-Process` command in PowerShell to view a list of running processes along with their PIDs.

To kill or terminate a process, you can use the appropriate system utility based on your operating system:

- On Linux and Unix-like systems, the `kill` command is used to send a signal to a process. The default signal sent by `kill` is SIGTERM (signal number 15), which requests the process to terminate gracefully. For example, to kill a process with a specific PID, you can use the command `kill PID`.
- On Windows, you can use the `Task Manager` or the `Stop-Process` command in PowerShell to terminate a process. In the Task Manager, you can right-click on a process and select "End Task" to kill it.

A signal is a software interrupt delivered to a process to notify it of an event or to request a specific action. Signals can be sent by the operating system or other processes. They are used for various purposes, such as terminating a process, requesting a process to reload its configuration, or pausing/resuming a process.

The two signals that cannot be ignored are:

1. SIGKILL (signal number 9): This signal is used to forcefully terminate a process. It cannot be caught or ignored by the process. When a process receives SIGKILL, it is immediately terminated without any chance to clean up or save its state.

2. SIGSTOP (signal number 19 on most systems): This signal is used to pause/suspend a process. When a process receives SIGSTOP, it is halted and put into a suspended state. The process remains suspended until it receives a SIGCONT (signal number 18), which allows it to resume execution.

These two signals have a special status and cannot be overridden or blocked by the process they are sent to.
