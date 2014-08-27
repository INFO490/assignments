## (Optional) Shared Folders

By using Shared Folders functionality of VirtualBox, you can move files between the file system of the host PC and the VM. When you want to move a file from the VM to the host, or vice versa, you simply put the file in this shared folder, which is seen by both the VM and the host machine.

1. To use the Shared Folders, first [install the guest additions](guest_addition.html).

2. On the host PC, create a folder/directory. Remember the location of this folder (e.g. C:\myshared).

3. In the VirtualBox menu, go to __Devices__ and select __Shared Folders Settings__.

4. Click the folder icon with + symbol on the right side.

 ![Folder 1](folder1.png)

5. In the _Folder Path_, type in the full path of the folder you created on the host PC (e.g. C:\myshared), or select __Other__ from the drop-down list and select the folder. Check the __Auto-mount__ option. Click __OK__.

6. Click __OK__.

7. Press `Alt + Ctrl + T` to open a terminal and type

         $ sudo adduser uiucinfo vboxsf

8. Restart Ubuntu. After it reboots, the shared folder will be automatically mounted into the `/media` folder, along with the prefix `sf_`. For example, if the name of your shared folder is `myshared` it will be mounted to `/media/sf_myshared`. To access it, use the __File System__ icon on Desktop, or type in the terminal:

         $ cd /media/sf_<foldername>

