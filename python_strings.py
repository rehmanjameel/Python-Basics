import psutil
import time
from datetime import datetime
import ctypes
import struct

course = 'Python for Beginners'
print(course)
# These methods don't change the original string it will create the new string
print(course.upper())
print(course.lower())
print(course.capitalize())
print(course.find('o'))
print(course.replace('B', 'b'))
# Another way to find using 'in' keyword
print('Python' in course)


def get_time():
    timing = time.time() - psutil.boot_time()
    print(timing)
    print(time.strftime("%H hours %M min %S sec", time.gmtime(timing)))
    # date_time = time.strptime(str(timing), "%M")
    # print(date_time)


get_time()
#
# def uptime():
#     libc = ctypes.CDLL('libc.so.6')
#     buff = ctypes.create_string_buffer(4096)
#
#     if libc.sisinfo(buff) != 0:
#         print('failed')
#         return -1
#
#     uptime = struct.unpack_from('@', buff.raw)[0]
#     print(uptime)
#     return uptime

# uptime()
# @register('shutdown')
# def shutdown_sys(self):
#     shutdown = input("Do you want to shut down the computer? (y/n): ")
#     if shutdown == "n":
#         exit()
#     else:
#         os.system("shutdown /s /t 1")
