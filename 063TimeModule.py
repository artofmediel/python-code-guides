import time
# epoch - a date and time from which a computer measures system time

print(time.ctime(0)) # this will convert a time, expressed in seconds, and convert into readable string
                    # convert a time expressed in seconds since epoch to a  readable string
                    # epoch is when your computer thinks time began (reference point)

print(time.time())  # returns current seconds since epoch

print(time.ctime(time.time())) # returns current data and time

time_object = time.localtime()
#time_object = time.gmtime()
# UTC - coordinated universal time is the primary time standard by which the world regulates clocks and time.
#       it's within about 1 second of mean solar time at 0º longitude, and is not adjusted for daylight saving time

print(time_object) # time object is made up of time struct
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
                            # %B = month
                            # %d = day
                            # %Y = year
                            # %H = hour
                            # %M = minutes
                            # %S = seconds
# display time
print(local_time)

# ------------------------------------
print("-----------------------------")
time_string = "20 April, 2020"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)

# ------------------------------------
print("-----------------------------")
# (year, month, day, hours, minutes, seconds, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
time_string = time.mktime(time_tuple) # converts time to seconds pass since epoch
print(time_string)

# ------------------------------------
print("-----------------------------")