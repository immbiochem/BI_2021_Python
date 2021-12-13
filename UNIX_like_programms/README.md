# The UNIX command line tools

## Description

In this directory you can find several UNIX-like utilities:
1) wc.py
2) ls.py
3) rm.py
4) sort.py
5) cat.py
6) tail.py

### wc.py
The program is designed to calculate a number of parameters in text documents or in text entered in interactive (streaming) mode.

This program works in several modes: 
1) in streaming mode, to do this, type the necessary arguments (or do not do this), press Enter; then enter the text, press Ctrl+D to complete the input.
2) in file mode. After entering the options (or without them), enter the file or list of files for which you want to make calculations.
This program has several options:
* *"-l"*, allows you to count rows;
* *"-w'*, allows you to count words;
* *"-c"*, allows you to count bytes in an object (string or file)

When running without options, all three parameters will be counted.
Options can be combined with each other, however, unlike the UNIX wc utility, this program does not distinguish between combinations of options, for example, "-wc" is not a valid combination, and "-w -c" is. The same goes for other options.

### ls.py

The program is designed to display the contents of the directory specified in the argument. If the directory name was not passed to the argument, the program will display the contents of the current directory. A list of directories and files can be passed as an argument. The contents of the directory will be displayed for all directories. If the file name was passed to the argument, the program ls.py displays it only if the file exists in the current directory.

The program has the option *"-a"*: when specifying this key in the argument, the program will output everything the same as in normal mode + hidden files and folders whose names begin with a dot (".txt").

### rm.py

The program is designed to delete files or folders whose names were entered as an argument.

The program has the *"-r"* option for recursively deleting folders (the folder will be deleted along with all the contents).

### sort.py

The program is designed to sort objects (lines from text files or lines from entered text).

The program has several modes of operation: 
1) streaming mode, starts when the program starts without arguments. Allows you to enter text line by line for subsequent sorting. To interrupt the input, use the Ctrl+D combination. 
2) file mode. To use it, pass a file name or several file names as an argument.

### cat.py

The program is designed to read a file or input text.

The program has several modes of operation: 
1) streaming mode, starts when the program starts without arguments. Allows you to enter text line by line for subsequent sorting. To interrupt the input, use the Ctrl+D combination. 
2) file mode. To use it, pass a file name or several file names as an argument.

## tail.py

The program is designed to output a limited number of lines of text from a file or input text. The program outputs the last few lines of text.

The program has several modes of operation: 
1) streaming mode, starts when the program starts without arguments. Allows you to enter text line by line for subsequent sorting. To interrupt the input, use the Ctrl+D combination. 
2) file mode. To use it, pass a file name or several file names as an argument.

The program has the option *"-n"*. By default, the last 10 lines from the file/input text are output, or all lines if their number is less than or equal to 10. If the *"-n"* option is used, then after it it is necessary to specify the number of the last lines to be output in the file or the text being entered.

## How to run the programs


All programs are run from the terminal command line by typing the command name/argument(s)/option (optional for some commands). To run the program from the folder in which it is installed, it is enough to make the command executable in the terminal:

*$ chmod +x <programm_name>*

For example:
*$ chmod +x cat.py*

It is enough to do this operation once before the first launch for each program, for all other launches the program will be ready for use.

There are two ways to run the program not from the directory where the program file is located: 
1) specifying the path to the file before the program name (*home/progs/cat.py* ) 
2) add the path to the file to the PATH environment variable (more details here: https://losst.ru/peremennaya-path-v-linux)

Some programs (cat.py , ls.py , wc.py , tail.py , sort.py ) support the use of pipelines. 
You can combine these programs with each other or with standard UNIX utilities using the pipeline operator *"|"*. 
Example: *cat file.txt | ./sort.py | ./wc.py*
