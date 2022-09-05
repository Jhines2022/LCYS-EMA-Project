# LCYS-EMA-Project
## Internal Python Port Scanner for checking which ports are open on the Queens Medical Center ASMIS network
#### This python script was put together to help check and mitigate a potential security issue that was highlighted in unit 9s ASMIS Essay.
#### list of Credits and Acknowledgments to information used while learning the "how and why of the parts" of this script are located at the end of this page  

<br/>

> IMPORTANT, Please read! The hostname being used in this example is for demonstration purposes only and must be changed to a permissioned target prior to use. This scanner has been developed for a project to scan internally only. 

<br/>

----

## Video Demo

https://user-images.githubusercontent.com/106968996/188339123-c58d5ec9-58e1-445c-b760-7e4d4e184cda.mp4

#### This video demo of a scan took 15.19 seconds to scan 100 ports but the screenshots will also show that it took just 2.25 seconds on a different day.
#### It appears that the time of day can make a significant difference on a scan of the permissioned target

----

## Pre-requisites
* Python v3.10.6 ([DOWNLOAD HERE](https://www.python.org/downloads/))
* An IDE such as PyCharm IDE (Free Community) ([DOWNLOAD HERE](https://www.jetbrains.com/pycharm/)) if you wish to run it outside of google. Otherwise, Google Colab will run it easily.
* Possible to run the code directly in Google colab if you have a google account ([Link to Google Colab](https://colab.research.google.com/notebook))

## What to change/Customize prior to usage (Bold areas inticate what needs to be changed)
* print("**Scanning scanme.nmap.org for testing reasons due to permissions.** ")
* target = socket.gethostbyname('**IP Address**', sys.argv[1]) 
* for port in range(**from port, to port**) *example (1,800), can also refer to the UML at the bottom of the page for Port ranges*
* socket.setdefaulttimeout(**0.2**) *example (1) represents one second, (0.5) represents half of a second.*
* result = s.connect_ex(('**IP Address**', port))

## Documentation

* ([Python 3.10.6 documentation](https://www.python.org/doc/))
* ([How to use Python on different platforms](https://docs.python.org/3/using/index.html))

## Port Scanner Code
* Port Scanner code without comments ([look at code](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/EMA_port_scanner.py))
* Port Scanner code with comments ([look at code](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/EMA_Port_Scanner(%2B-Comments).ipynb))

<br/>

----

## Screenshots of Code Input and Output


### Chosen Modules/Libraries

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/importSection.png)

#### This if else statement

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/ifLen.png)

#### Prints the output below.

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/invalidSyntaxOutput.png)

#### This print section creates the dashes, prints text and combines string to text.

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/printSection.png)

#### Prints the following output.

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/scanningTimeStartedOutput.png)

#### This for loop will scan the chosen port ranges via our targets IPv4 address.

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/tryForPort.png)

#### Outputs the following details:

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/portOpenReturnOutput.png)

#### This Except construction allows ways to exit the program logically.

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/except.png)

#### This datetime.now function combination

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/bettert1t2print.png)

#### Calculates how long the scan took and outputs the section grid and time.

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/TimeToCompleteOutput.png)

### The Program Output (Full) from running the script.

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/OUTPUTfull.png)

#### This particular scan took 2.25 seconds but it can take longer.
#### Scans during testing took between 2.25 seconds and upto 15.19 seconds, depending on the time and system resources 

## Access The Internal Port Scanner
*  ([Internal Port Scanner](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/EMA_port_scanner.py))

----

## UML Process to help illustrate the 3 groups of port ranges assigned to systems as well-known ports(0 to 1023), registered ports(1024 to 49151) and private ports (49152–65535) 

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/UMLforScanner.png)

----

## Credits and acknowledgments
*  Geeksforgeeks ([Defining a target](https://www.geeksforgeeks.org/port-scanner-using-python/?ref=gcse))
*  Heath Adams TCM Security ([Introduction to Python](https://academy.tcm-sec.com/))
*  Python ([Creating a Socket](https://docs.python.org/3/howto/sockets.html))
*  Python ([How to use Python on different platforms](https://docs.python.org/3/using/index.html))
*  Python ([Python 3.10.6 documentation](https://www.python.org/doc/))

----



