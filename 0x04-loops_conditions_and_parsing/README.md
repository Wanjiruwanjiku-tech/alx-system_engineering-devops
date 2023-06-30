	BASH

	Loops, conditions and parsing
	DevOps
	Shell
	Bash
	Scripting By: Sylvain Kalache
	Weight: 1


AUTHOR: NATALIE WANJIRU WANJIKU

Learning Objectives

- How to create SSH key

	LINUX

	Open a terminal and Run the following command to generate an RSA key pair
		ssh-keygen -t rsa -b 4096
	This command will create a 4096-bit RSA key pair.

	You will be prompted to choose the file where you want to save the key. Press Enter to accept the default location or specify a different path.

	Next, you will be prompted to enter a passphrase. It is recommended to use a strong passphrase for added security. Press Enter if you want to create the key without a passphrase.

	After the key pair is generated, your public key will be saved in a file with the extension .pub. You can view the contents of the public key by running the following command

		cat ~/.ssh/id_rsa.pub
	
	Copy the contents of the public key file (id_rsa.pub), and save it in a file named 0-RSA_public_key.pub as required.

- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash

	The #!/usr/bin/env bash shebang privides greater flexibility and portability as the script will work even if the bash interpreter is un a different location.


- How to use while, until and for loops

	While:
		while condition
		do
			#code to execute
		done


- How to use if, else, elif and case condition statements

	if condition1
	then
		#code to execute
	elif condition2
	then
		#code to execute
	else
		#code to execute
	fi

	CASE:
	
	case variable in
		pattern1)
			#code to execute if match
		;;
		
		pattern2)
			#code to execute if match
		;;

		*)
			#code to execute if no match
		;;
	esac


- How to use the cut command

	The cut command is used to extract sections from lines of files or input streams

	Basic Usage:
		cut OPTIONS FILE


- What are files and other comparison operators, and how to use them

	File Operators
		-e - exist
		-f - regula
		-d - directory
		-r - readable
		-w - writeable
		-x - executable

	String Operators:
		= equal
		!= - not equal
		-z - zero length of str
		-n - non-zero length of str

	Numeric Operators:
		-eq - equal
		-ne - not equal
		-lt - less than
		-gt - greater than
		-le - less than or equal to
		-ge - greater than or equal to.
