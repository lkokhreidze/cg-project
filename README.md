# CG-Project

[Try it out](https://lkokhreidze.github.io/cg-project/)

## How to run on local machine

To run the application in a local machine, you need a local server. For example [Uniform Server](http://www.uniformserver.com/) is a good option.

Here are the steps for running it with installation of Uniform Server:

* Download Uniform Server that is compatible with your platform
* Follow the installation instructions
* Download [the project](https://github.com/lkokhreidze/cg-project/archive/master.zip)
* Delete everything in UNIFORM_SERVER_PATH/www directory
* Unpack the contents of project ZIP file to UNIFORM_SERVER_PATH/www **IMPORTANT! index.html has to be in the UNIFORM_SERVER_PATH/www directory!**
* Open the UniController.exe, make sure that no other programs in your computer are listening to the ports that Uniform wants to listen (usually Skype can be a problem)
* When asked for MySql password, click cancel
* In UniServer GUI, click Start Apache
* Open web browser and go to http://localhost
* Enjoy!