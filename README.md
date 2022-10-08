# fun-projects

1. Testing Parse
Takes two arguments filename and string as word
Usage:

`python3 testing_parse.py /Users/narendram.admin/Downloads/iad51_HwEmul.log(full file path)  -w stream (word of your interest)`

Sample output:
I was searching for word stream

`(venv) naren-pc%  python3 testing_parse.py /Users/narendram.admin/Downloads/iad51_HwEmul.log  -w stream -i

The word  stream is case sensitve: True ,occured  6570  times in file`

In the following log I have two words with stream and STREAM
so I provided an option for users with '-i' which checks for case insensitve word

`Jun 10 13:29:24.072413 ERR [89310] HwTagTable::remove_rtp_stream() STREAM 163 NOT ACTIVE`

so the out shall be as following when user uses i and when -i is not included

`(venv) naren-pc%  python3 testing_parse.py /Users/narendram.admin/Downloads/iad51_HwEmul.log  -w stream -i
The word  stream is case sensitve: True ,occured  6570  times in file
(venv) naren-pc %  python3 testing_parse.py /Users/narendram.admin/Downloads/iad51_HwEmul.log  -w stream   
The word  stream is case sensitve: False ,occured  3285  times in file`



2. Health check(work in progress)

Usage:
(venv) naren-pc %  python3 healthchecker.py                                                              
Self intenet is working
Website is recheable

This script checks self connectivity first and then tries to request get url for google just to verify if DNS is workign correctly and connectivty is working properly. If script fails at this step then customer is having connectivity issues

The second part of script checks conenctivity to Instrumental healthcheck website to check connectivity to the site.


