# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 10 min

### Prerequisites:

In order to complete this tutorial, you will need to have an Ubuntu 20.04 server with a non-root sudo-enabled user account and a basic firewall. This can be configured using our initial server setup guide for Ubuntu 20.04.

## How to Install Ubuntu

1. Log in as root using the IP address of your droplet
    ```
    $ ssh root@your_server_ip
    ```
2. Create a new user
    ```
    $ adduser sammy
    ```
3. Grant administrative priveleges
    ```
    $ usermod -aG sudo sammy
    ```
4. Set up a basic firewall
    ```
    ufw allow OpenSSH
    ufw enable
    ufw status
    ```
5. Enabling external access for your regular user
    Using Password
    ```
    ssh sammy@your_server_ip
    sudo command_to_run
    ```
    Using SSH
    ```
    rsync --archive --chown=sammy:sammy ~/.ssh /home/sammy
    ssh sammy@your_server_ip
    sudo command_to_run
    ```

### Installing Apache:

1. Update the package manager cache with
    ```
    $ sudo apt update
    ```
2. Install Apache
    ```
    $ sudo apt install apache2
    ```
3. Allow traffic on port 80 with
    ```
    $ sudo ufw allow in "Apache"
    ```


### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
---

Accurate as of (last update): 2022-01-13

#### Contributors:  
Ella Krechmer, pd1  
Ivan Lam, pd1  
