# File_Sharing

# For Linux
There are three version of this app uploaded so far.
In V-1.0 You can share all files inside your share folder. For this you just have to activate virtualenv and run main.py.
In V-1.1 You can share all of your Files inside Home folder {Only selective kind of file extension}. Just run main.py.

In V-1.2 I have added feature of authentication of user as well as authorization of user, In this you can authorise someone to be
admin or a general user. For admin you have to change the value of isadmin field in table to 1 manually. An admin can access all the
files inside home folder but an nonadmin only can access files inside sharing folder. In all the cases anyone can upload a file with 
(Certain extentions like .pdf/.mp4....) to your PC.

NOTE -- You have to set MySQL database to run  V-1.2, you can see a file at location Flask_v1.2/MySQL_setup which can assist you with
MySQL.

Thanks

# For Windows

Go to V-1.0 or V-1.1 folder through Command prompt 
then type ..\venv_win\Scripts\python.exe main.py 
Now open the url in browser.
You're Done now
