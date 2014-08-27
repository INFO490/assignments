## (Optional) Guest Additions

When you first use the VM, the VM window might be too large or too small for your monitor. Installing guest additions will let you resize the VM window. The VM will also automatically capture and uncapture your mouse pointer. Do the following to install the VirtualBox guest additions. (Note that a few details might be different depending on your host OS.)

1. Double-click the VM icon or click __Start__ to start the VM. Log in by entering your password (__uiucinfo__ by default in the pre-built VM).

2. In the VirtualBox menu bar on your host PC (not inside the Ubuntu VM), go to __Devices__ and select __Insert Guest Additions CD Image...__.

3. When asked if you want to download the guest addition image, click __Download__. After downloading, click __Mount__. A folder of the guest addition image will automatically appear.

 ![Guest 1](guest1.png)

4. Double-click __autorun.sh__. Enter your password.

5. The following window will appear, and it will take a few minutes to install. When the installation is complete, press __Enter__.

 ![Guest 2](guest2.png)

6. Click the blue/white in the top left corner. When a list appears, click the gray __Log Out__ icon in the bottom right corner. Click Restart.

 ![Guest 3](guest3.png)

7. After the VM reboots, type your password to log into Ubuntu. When you resize the VirtualBox window of your host OS, the Ubuntu desktop should resize automatically.