SECURE SHELL (SSH)
------------------------------

- A secure protocal used as the primary means of connecting to Linux servers remotely.

- It provides a text based interface by spawning a remote shell.

- After connecting, all commands you type in your local terminal are sent to the remote server.

- It is a communication protocol and its traffic is always encrypted


HOW SSH WORKS
---------------------

- Authentication.
    - Passwords
    - Public/private key pair

Using key pairs is most highly recommended.

- Generate keys

        you can use the command:

        ssh-keygen


the command generates the keys and saves them in their specific default files.

- .ssh/id_rsa for the private key.
- .ssh/id_rsa.pub for the public key.

The .ssh folder will be located in the home directory i.e cd ~


- Copy the public key to the server

        ssh-copy-id username@remote_host (the server's IP address)

once copied the public key will be located in the folder .ssh as well under the file name authorized_keys


This project will dive deeper into how one can interact with the server by writing bash scripts