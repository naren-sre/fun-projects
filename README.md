# fun-projects

To download the code:

`git clone https://github.com/naren-sre/fun-projects.git`

1. Testing Parse:

Takes two arguments filename and string as word
Usage:

`python3 testing_parse.py /Users/narendram.admin/Downloads/iad51_HwEmul.log(full file path)  -w stream (word of your interest)`

Sample output:
I was searching for word stream

`(venv) naren-pc%  python3 testing_parse.py /Users/narendram.admin/Downloads/iad51_HwEmul.log  -w stream -i .The word  stream is case insensitve: True ,occured  6570  times in file `

In the following log I have two words with stream and STREAM
so I provided an option for users with '-i' which checks for case insensitve word

`Jun 10 13:29:24.072413 ERR [89310] HwTagTable::remove_rtp_stream() STREAM 163 NOT ACTIVE`

so the output shall be as following when user uses -i and when -i is not included

`(venv) naren-pc%  python3 testing_parse.py /Users/narendram.admin/Downloads/iad51_HwEmul.log  -w stream -i
The word  stream is case sensitve: True ,occured  6570  times in file`

`(venv) naren-pc %  python3 testing_parse.py /Users/narendram.admin/Downloads/iad51_HwEmul.log  -w stream   
The word  stream is case sensitve: False ,occured  3285  times in file`



2. Health check(work in progress, I intend to add more features to this script)

Usage:
`(venv) naren-pc %  python3 healthchecker.py   
output:
I wrote the output to a log file. So customer has idea when connection was lost or when the connection was working. I used the logging module and writing the results and status codes into log file.

This script checks default gateway first and ping to see if interface is up and running and then checks the DNS runs a connectivity test to standard url google and then tries to request get url for google just to verify if DNS is working correctly and connectivty is working properly to the url of interest. If script fails at this step 1 then customer is having issues with interface and/or default gateway

if  second part of script fails that indicates you have no internet connection or your internal DNS is having issues resolving the standard website
if script fails at 3rd part then you might want to double check url or please check with your router/isp


