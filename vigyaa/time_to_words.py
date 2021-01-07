"""
Given the time in numerals we may convert it into words.

"""
"""
solution to this problem is,

step 1) create a list with 0-29 in words like "zero" to "twenty nine".

step 2) check if the input minutes is 0 if zero return "list[hour] o'clock "

step 3) check if the minutes is less than or equal to 30 if so enter the if condition for  "past"

step 4) regarding above step add more if else condition for 1 min, 15 min and 30 min. 

step 5) check if the minutes is greater than 30 if so enter the if condition for the "to".

step 6) regarding above step add more if else condition for 45 mins, 59 min, and other mins greater than 30mins.

"""



"""

time_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
 "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
 "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
  "twenty eight", "twenty nine" ]
    
 time = ""
 if m<=30:
    if m==0:
        time=time_words[h]+" o' clock"
    elif m==15 :
        time="quarter past "+time_words[h]
    elif m==30:
        time="half past "+time_words[h]
    elif m==1:
        time=time_words[m]+" minute past "+time_words[h]
    else
        time=time_words[m]+" minutes past "+time_words[h]
  
else:
    if m==45:
        time="quarter to "+time_words[h+1];
    elif m==59:
        time=time_words[60-m]+" minute to "+time_words[h+1]
    else:
        time=time_words[60-m]+" minutes to "+time_words[h+1]
 
return time

"""