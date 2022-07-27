You are expected to produce working code that will generate a hashcat-like password mask based on each line of the password file
and print to console the top three most common password patterns.
A password pattern, or mask, is comprised of four character sets that are defined as follows:

?l - All lowercase characters.
?u - All uppercase characters.
?d - A number in the range [0, 9]
?s - A non-alphanumeric character, which we’ll define as anything not in ?l, ?u, or ?d
Given a line of input from the password file, such as Hunter01!, it would be translated to the mask:

?u?l?l?l?l?l?d?d?s

as:

H => ?u, as H is in upper ASCII.
u => ?l, as u is in lower ASCII.
n => ?l, as n is in lower ASCII.
t => ?l, as t is in lower ASCII.
e => ?l, as e is in lower ASCII.
r => ?l, as r is in lower ASCII.
0 => ?d, as 0 is between 0 and 9 inclusive.
1 => ?d, as 1 is between 0 and 9 inclusive.
! => ?s, as it is not alphanumeric.

Input
The password file is located at <Python-Scripts/Python Challenge/Python Hash/passwords.txt>

Expected Output
The output of the file should show the top three masks from /home/coderpad/data/passwords.txt and how often they occur. Example output to this challenge should look like:

Top 3 Password Masks
--------------------
1. ?u?l?l?l?d?d?s   : 100
2. ?l?l?l?l?d?d     : 50
3. ?d?d?u?l?l?l?l   : 25
Validation
Note: If you wish to verify your program’s accuracy, use the following data set to run your application against first.

123456
password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
123123
baseball1
abc123
football
monkey
letmein
696969
shadow2
master1
666666
In this sample set, the results should be:

    Top 3 Password Masks
-----------------------------
1. ?d?d?d?d?d?d     :    5     
2. ?l?l?l?l?l?l     :    3     
3. ?l?l?l?l?l?l?l?l :    2  
Again, remember your final submission should use passwords.txt as input and return the top three most common password masks!

References
https://hashcat.net/wiki/doku.php?id=mask_attack
