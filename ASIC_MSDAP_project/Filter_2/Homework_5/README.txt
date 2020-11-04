######## README FILE : Filter.cpp ###########

* Important Note 1 -> "To execute the cpp code - filter.cpp, please
build the project by the below mentioned steps"

* Important Note 2 -> "Please donot change the name of the folder name or
code name - Homework_5, if you change, please update it in CMakeLists.txt"

* Important Note 3 -> "The code and the cmake files are designed to run the
project in college server or linux machine with cmake tools"

######## STEPS TO BUILD AND RUN : Filter.cpp #########

1) Copy the Project Folder to a directory<"DIR">

2) Move to the Project directory through terminal
:-> "cd <DIR>/Homework_5/"

3) Create an executable for launcher-setup shell script
:-> "chmod +x project_setup.sh"

4) Build and setup the project (Minimum CMake Version Required : 2.8)
:-> "./project_setup.sh"

5) Compile the cpp file with C++11 - version compiler
:-> "g++ -std=c++11 filter.cpp -o <executable_object_name>"
ex :-> "g++ -std=c++11 filter.cpp -o filter_object"

6) Before Executing the code : Files input and output paths can be given as
arguments in different ways. Also, you can keep the data and coefficient files
in a input_folder say named - "input_files" (used for example) :-

    <path_input_file> :-
    a) If the file is inside the project folder, then give only path to file
    from the project directory, because the code contains CURRENT_DIR to reach
    the Project Folder DIR.

    b) If the output file doesn't exist, just give the name of the file and the
    code will automatically create a file.out of that name in "output_files" folder
    and it will save the result in it.

    c) Note***(Very Important) : Easiest way is to give the "<FULL_PATH_TO_FILE>" but
    if you use just file names inside the project directory then "PLEASE DONOT ADD a
    "/" SLASH sign before or starting of the file name or folder name".

7) Executing the filter.cpp with both path examples

:-> "./<executable_object_name> <path_coeffiecient_file> <path_Rj_file> <path_data_file> <path_output_file>"

ex 1:-> "./filter_object input_files/Coeff1.in input_files/Rj1.in input_files/data1.in output1.out"
(Note** -> Remember for example 1 : Any ouput file name can be given and the result will be in output_files)

********** OR *************

ex 2:-> "./filter_object /home/DIR_FOLDER/input_files/Coeff1.in /home/DIR_FOLDER/input_files/Rj1.in /home/DIR_FOLDER/input_files/data1.in /home/DIR_FOLDER/output1.out"
(Note** -> Remember for example 2 : The ouput file should be created before running the code)

########################  CONTACT FOR BUGS  OR INFORMATION  ####################

Name : Soumyadeep Choudhury and Anmol Gautam
Email : sxc180056@utdallas.edu and axg190014

################  END  ###############