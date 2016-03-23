# Bridge Variables for Scratch
###Overview
A simple, open-source bridge varible server for Scratch written in Python.
###Prerequisites
Before you do anything you should install:
* Python
* pip package
Then use the pip package to install from the command line:
* PyYAML
* Dylan5797's scratch api package from github.com/Dylan5797/scratchapi/

###Server Setup
Download and extract the repository. Navigate to bridge-varibles/src/mooshoe/ and then run main.py through the command line.
###Configeration
Open the configeration folder found in bridge-varibles/src/ and open config.yml.
<b>username:</b> A scratch account's username. This should not be your main account and must be a Scratcher. <br>
<b>password:</b> The account's password. This is needed so you can log in and use cloud varibles. <br>
<b>projects:</b> A list of the project id's that are connected. <br>
<b>update-interval</b> How fast your varibles are synced. I recomend 0.1, or 10 times per second. <br>
<p>cloud-variable</b> The name of your cloud variable. I recomend "Cloud" or "Bridge."
###Scratch Project Setup
Create a cloud variable in the project that matches the setting in the configeration "cloud-varible." The default is cloud.
###Stopping the Server
Just type -1 into the console.
###Lisence
Under a CC and MIT licence.
