## Virtual Machine for INFO 490

A Virtual Machine (VM) is a software that lets you virtually emulate an operating system (_e.g._ Linux) on your physical computer (_e.g._ Windows or Mac). This tutorial walks you through the steps necessary to set up a VM that runs a Linux distribution called Ubuntu. There are two ways to set up a Linux VM on your PC:

1. Download and install [VirtualBox](https://www.virtualbox.org/) and then download a pre-built Virtual Machine (VM), and

2. Download and install VirtualBox and then [build your own VM](build_your_own.html). This takes more time than the first option.

This section walks you through the first option: using a pre-built VM. For building your own VM, see [Building your own VM](build_your_own.html).

## Setting up the pre-built VM

### Downloading VirtualBox

1. Go to [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) page. Download and install the version that corresponds to your operating system.

 ![Download 1](download1.png)

### Downloading pre-built VM

1. You can download the VM from [the LCDM webpage](http://lcdm.astro.illinois.edu/teaching/info490su14.html). Note that the file is quite large (approximately 1.6 GB) and might take a while to download. Also make sure you have enough space available as the VM could become as large as 8 GB. Unzip it and remember where you save the VM.

### Setting up the pre-built VM

1. Start VirtualBox. In the menu bar, go to __File__ and select __Import Appliances__ (Ctrl + I).
 
 ![VirtualBox 0](vbox0.png)

2. Click the folder icon on the right side, and find where you saved your pre-built VM. Once you selected "info490.ova" click __Next__ at the bottom.

 ![VirtualBox 1](vbox1.png)

3. If your host PC has more than 2 GB of RAM, click __Import__. If your host PC has less than 2 GB of RAM, change __RAM__ to 512 MB before clicking __Import__.
 
 ![VirtualBox 2](vbox2.png)

4. It will take a few minutes to import the virtual disk image. When importing is complete, double click on your new VM icon (or click __Start__).

5. As the VM starts up, VirtualBox will display a few messages about mouse pointer and keyboard capturing, which you should read as they are useful features. After the VM has finished booting, you will see a login screen; both the username and password are __uiucinfo__.

6. The first thing you should do is change the password. press Ctrl + Alt + T to open a terminal. Type `passwd`. Type "uiucinfo" when asked for current UNIX password. Enter new UNIX password. __Remember your password__.

 ![VirtualBox 3](vbox3.png)
 



