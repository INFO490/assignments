## Virtual Machine for INFO 490

A Virtual Machine (VM) is a software that lets you virtually emulate an operating system (_e.g._ Linux) on your physical computer (_e.g._ Windows or Mac). This tutorial walks you through the steps necessary to set up a VM that runs a Linux distribution called Ubuntu. There are two ways to set up a Linux VM on your PC:

1. Download and install [VirtualBox](https://www.virtualbox.org/) and then download a pre-built Virtual Machine (VM), and

2. Download and install VirtualBox and then [build your own VM](build_your_own.html). This takes more time than the first option.

This section walks you through the second option: building your VM using a Xubuntu ISO image. For using a pre-built VM to set up VirtualBox, see [Setting up the pre-built VM](prebuilt.html).

## Building your own VM

### Downloading VirtualBox

1. Go to [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) page. Download and install the version that corresponds to your operating system.

 ![Download 1](download1.png)

### Downloading Xubuntu

1. Download Xubuntu 14.04 LTS PC (Intel x86) desktop ISO image from [here](http://mirror.anl.gov/pub/ubuntu-iso/CDs-Xubuntu/14.04/release/xubuntu-14.04-desktop-i386.iso). Remeber where you save this file, since you will need to access it later.

### Creating a VM

1. Start VirtualBox. Create a new VM by clicking the _New_ button at the top left corner.

2. Enter a name for the VM (_e.g._ Ubuntu 14.04). Select "Linux" for _Type_. Select "Ubuntu (32bit)" for _Version_. Click _Next_.

3. Enter the amount of memeory to be allocated to the VM. The optimal amount depends on how much RAM you have on your host PC (the one that runs the VirtualBox). The best way to find out the optimal amount of RAM is to do some experimenting yourself, but if you are unsure, you can assign the minimum (512 MB) and adjust it later. The general rules are:
 
 * You should assign enough RAM for the VM to run smoothly (> 512 MB for 32-bit Ubuntu).
  
 * You should leave enough RAM for the host PC (> 2 GB for 64-bit Windows 7).

 Click _Next_.

4. Select _Create a virtual hard drive now_. Select _Create_.

5. Select _VDI_. Click _Next_.

6. Select _Fixed size_. Click _Next_.

7. Set the size of the virtual hard drive to 8.0 GB. Click _Create_.

8. It will take a few minutes to create a virtual hard drive. Now the VM is ready to use.

### Installing Ubuntu

1. Press start or double click on your new VM icon. A dropdown box should appear. Click the folder icon at the bottom right corner and find where you saved your Xubuntu ISO image. Once you selected "xubuntu-14.04-desktop-i386.iso," click _Start_.

2. It will take a few minutes for the install tool to load. On the Welcome screen, click _Install Ubuntu_.

3. Click _Continue_. Do not check the boxes.

4. Select _Erase disk and install Xubuntu_ and click _Install Now_.

5. Select your locale, etc. Enter your name, username, and password. Remember your password. Click _Continue_. 

6. It will take a few minutes to install. When the installation is complete, click _Restart Now_.

### Installing necessary packages

1. Log into your Ubuntu VM by entering your password. It should look like this: 

 ![Ubuntu Desktop](ubuntu1.png)

2. Click on _Software Update_ and click _Install Now_. It will take a few minutes to install updates. If it asks if you want to restart, click _Restart Now_.

3. When you log back into Ubuntu, press Ctrl + Alt + T to open a terminal. Type the following into the terminal:

         $ sudo apt-get install python

 ![Terminal 1](ubuntu2.png)

 Note 1: When you first open the terminal, the command prompt shows the following:

         username@servername:~$

 It is common for the prompt on Unix systems to end in a $ character. Thus, it is common to indicate that the given example is a Unix command by writing the $ symbol at the beginning. So when I told you to type "$ sudo apt-get install python" I was actually telling you that this is a Unix command and you have to type "sudo apt-get install python" at the prompt.

 Note 2: _apt-get_ is a command-line tool, commonly used in Linux systems that are derived from Debian (such as Ubuntu). It lets you install new software packages, and remove or upgrade existing ones.

4. When it asks for sudo password, enter your password.

 Note 1: It will likely say "python is already the newest version," but if it asks "Do you want to continue? [Y/n]" just press enter.

 Note 2: Different users on Unix systems can have various security privileges. _sudo_ is a program that allows users to run programs with the security priveleges of a superuser. Try running _apt-get_ without _sudo_ command and see what happens.

5. Install the [necessary packages](software_list.html) by using the following command:

         $ sudo apt-get install vim git ipython python-numpy python-scipy python-matplotlib python-pandas python-requests python-bs4 python-pymc python-sklearn

 If it asks "Do you want to continue? [Y/n]" press enter.