# LCYS-EMA-Project
## Internal Python Port Scanner for checking which ports are open on the Queens Medical Center ASMIS network

<br/>

> IMPORTANT, Please read! The hostname being used in this example is for demonstration purposes only and must be changed to a permissioned target prior to use. This scanner has been developed for a project to scan internally only. 

<br/>


## Pre-requisites
* Python v3.10.6 ([DOWNLOAD HERE](https://www.python.org/downloads/))
* An IDE such as PyCharm IDE (Free Community) ([DOWNLOAD HERE](https://www.jetbrains.com/pycharm/)) if you wish to run it outside of google. Otherwise, Google Colab will run it easily.
* Possible to run the code directly in Google colab if you have a google account ([Link to Google Colab](https://colab.research.google.com/notebook))

## What to change/Customize prior to usage (Bold areas inticate what needs to be changed)
* print("**Scanning scanme.nmap.org for testing reasons due to permissions.** ")
* target = socket.gethostbyname('**IP Address**', sys.argv[1]) 
* for port in range(**from port, to port**) *example (1,800)*
* socket.setdefaulttimeout(**0.2**)
* result = s.connect_ex(('**IP Address**', port))

## Screenshots of code input and output


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

#### The Program Output (Full) from running the script.

![](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/Folder%20of%20Scanner%20images/OUTPUTfull.png)

#### This particular scan took 2.25 seconds but it can take longer.
#### Scans during testing took between 2.25 seconds and upto 7.3 seconds 

Get the Internal Port Scanner ([HERE]([https://www.python.org/downloads/](https://github.com/Jhines2022/LCYS-EMA-Project/blob/main/EMA_port_scanner.py)))
![]()

Copyright and licensing information

Credits and acknowledgements

