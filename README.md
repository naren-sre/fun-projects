# fun-projects

1. Testing Parse
Takes two arguments filename and string as word
Usage:

`python3 testing_parse.py /Users/narendram.admin/ownloads/iad51_HwEmul.log(full file path)  -w stream (word of your interest)`

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
