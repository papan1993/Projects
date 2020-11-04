
################   README FILE - PROJECT : 1 - AOS  #############################################################

Note-* Important : 
(Assume : "/PATH_TO_PROJECT_DIR" : Path to Project Folder directory in a DC machine.)
(Assume : "/PATH_TO_LOCAL_DIR/AOS_Project_1/" : Path to Local folder to Execute Launcher.)
(Assume : "Config.dat" : Configuration file for the program.)

1) All the java files including launcher and cleanup files, are included in the "AOS_Project_1" folder.
2) Path to launcher and cleanup files : "/PATH_TO_PROJECT_DIR/AOS_PROJECT_1/".
3) Path to java files : "/PATH_TO_PROJECT_DIR/AOS_PROJECT_1/src/".
4) Follow the commands mentioned below to run the program.

###########  STEP BY STEP COMMANDS TO RUN THE PROGRAM  ################

1) Copy and paste the whole project zip file - "AOS_Project_1.zip" in your desired location in DC machine.
	
	-> "scp AOS_Project_1.zip sxc180056@dc02:~/PATH_TO_PROJECT_DIR/" 

2) Unzip the Project. (You can also use other tool to extract project code).

	-> "unzip AOS_Project_1.zip"

3) Go to the AOS project src directory containing the java files.

	-> "cd /PATH_TO_PROJECT_DIR/AOS_PROJECT_1/src/"

4) Compile and build the AOS_Project_1 to generate the java classes.

	-> "javac *.java"

5) Copy the Config.dat file in both local machine (from where the launcher will be executed) and DC machine.

6) a) Path to Config File in DC Machine (Try to keep the config file inside AOS_Project_1 folder because the 
	output files will also generated at the same location). 

	-> CONFIGDC = "/PATH_TO_PROJECT_DIR/AOS_Project_1/Config.dat"

6) b) Path to Config File in Local or Launcher-Execution Machine.
	
	-> CONFIGLOCAL = "/PATH_TO_LOCAL_DIR/AOS_Project_1/Config.dat"

7) Copy the launcher.sh and cleanup.sh files in the Local execution directory : "/PATH_TO_LOCAL_DIR/AOS_Project_1/".

	-> for Launcher = "/PATH_TO_LOCAL_DIR/AOS_Project_1/launcher.sh"
	-> for Cleanup = "/PATH_TO_LOCAL_DIR/AOS_Project_1/cleanup.sh" 

8) Edit the both launcher.sh and cleanup.sh with the Config.dat file path and project directories as follows.

	-> "Make the Following changes below (Snippet from the launcher and cleanup file) and save it"
    --------------------------------------------------------------------------------------------
	#### Change this to your netid
	netid=sxc180056

	#### Root directory of your project
	PROJDIR=/PATH_TO_PROJECT_DIR/AOS_project_1

	#### Directory where the config file is located on DC system
	CONFIGDC=$PROJDIR/Config.dat

	#### Config File local machine
	CONFIGLOCAL=/PATH_TO_LOCAL_DIR/AOS_Project_1/Config.dat
    ---------------------------------------------------------------------------------------------

9) Create an executable of both launcher.sh and cleanup.sh.

	-> "chmod +x launcher.sh cleanup.sh"

10) Run the launcher code from the local execution directory.

	-> "./launcher.sh"

11) All the terminals will show : "Output File Generated" : to indicate all the programs are finished.

12) Run the cleanup code from the local execution directory to clean all the dc server nodes.

	-> "./cleanup.sh"

13) All the output files of all the DC nodes are generated in the DC project path ('*' denotes node id of DC machine).

	-> Output files path = "/PATH_TO_PROJECT_DIR/AOS_Project_1/Config-*.dat"

14) Close all the terminals after the execution of the project.

################## DEVELOPER CONTACT FOR BUG OR ISSUES ##########################################

Name : Soumyadeep Choudhury
UTD Net ID : sxc180056
UTD ID : 2021439916
Email ID : sxc180056@utdallas.edu

###################################################  END ######################################################################

