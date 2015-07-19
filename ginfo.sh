# Script to print user information who currently login, current date & time

echo "Hello $USER"
echo "Today is \c";date
echo "Number of user login : \c" ; who | wc -l
echo "Calendar"
cal 
myname=viki
myos=windows
echo "My name is $myname"
echo "My os is $myos"
mypath=pwd
echo "My path is `pwd`"
exit 0
