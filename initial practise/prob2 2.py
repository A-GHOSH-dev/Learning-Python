time = str(input())
hrs = time[0:2]
minutes = time[3:5]
seconds = time[6:8]
AM_PM = time[8:10]
flag = True
if int(hrs) > 12:
    flag == False
if AM_PM == 'AM' and flag == True:
    if int(hrs) == 12:
        hrs = '0'
elif AM_PM == 'PM' and flag == True:
    if int(hrs) != 12:
        hrs = int(hrs) + 12
if int(minutes) > 60 or int(seconds) > 60:
    flag = False
if len(str(hrs)) != 2:
    hrs = '0' + str(hrs)
if len(str(minutes)) != 2:
    minutes = '0' + minutes
if len(str(seconds)) != 2:
    seconds = '0' + seconds
if flag==True:
    print("%s:%s:%s"%(hrs,minutes,seconds))
else:

    print('Invalid')





'''Time Conversion
Given a time in the 12-hour format with the suffix , either AM/PM, convert that  into a 24-hour format. 12-hour format is hours:minutes:seconds followed by AM or PM, where the hours range from 0 to 12, minutes range from 0 to 59, seconds range from 0 to 59.  24-hours format is hours:minutes and seconds , where hours range from 0 to 23, minutes range from 0 to 59, seconds range from 0 to 59. All the three components: hours, minutes, seconds are represented in the two digit format.

Note Midnight 12 o’clock is 12:00:00AM in the 12-hour format and it is 00:00:00 in 24- hour format. 12 Noon is 12:00:00PM in the 12-hour format and it is 12:00:00 in the 24- hour format.

For example, if input is 07:05:45PM then the output is 19:05:45 and if the input is 07:05:45AM then the output is 07:05:45.

Input format:

Time in 12-hour format with suffix, either  AM or PM

Output format:

Print time in 24-hour format

Boundary Conditions:

0 < hour, minute and seconds < 60

Meridium should be either “AM” or “PM”   '''


#Your code has Passed Execution!
t=str(input())
l=len(t)
if t[l-2:l]=='AM':
    if t[0:2]=='12':
        print('00:00:00')
    else:
        print(t[0:l-2])
elif t[l-2:l]=='PM':
    t=str(int(t[0:2])+12)+' :00:00'
    print(t)



















