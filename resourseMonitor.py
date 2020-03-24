import psutil
import platform
from datetime import datetime

# function to convert large number of bytes into different scaled format
def get_size(bytes, suffix="B"):
	'''Scale bytes to it's proper format eg: 1234567 => 1.20MB, 1234567894 = 1.17GB'''
	factor = 1024
	for unit in ["", "k", "M", "G", "T", "P"]:
		if bytes < factor:
			return f"{bytes:.2f}{unit}{suffix}"
		bytes /= factor



# platform information
print("="*40, "System Information", "="*40)
# gathers system information
uname = platform.uname()
# Retrieve specified information from uname
# print(f"System: {uname.system}")
# print(f"Node Name: {uname.node}")
# print(f"Release: {uname.release}")
# print(f"Version: {uname.version}")
# print(f"Machine: {uname.machine}")
# print(f"Processor: {uname.processor}")

#Getting boot time information
print("="*40, "Boot Time", "="*40)
boot_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")