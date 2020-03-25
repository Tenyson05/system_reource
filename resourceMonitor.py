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



#################### platform information ####################
print("="*40, "System Information", "="*40)
# gathers system information
uname = platform.uname()
# Retrieve specified information from uname
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

#################### Boot time information ####################
print("="*40, "Boot Time", "="*40)
boot_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

#################### CPU information ####################
print("="*40, "CPU Info", "="*40)
#Number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Physical & Logical cores:", psutil.cpu_count(logical=True))
#CPU frequency
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
print("CPU Usage per core")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
	print(f"Core {i}: {percentage}%")
	
print(f"Total CPU usage: {psutil.cpu_percent()}%")

#################### Memory Information ####################
print("="*40, "Memory Info", "="*40)
# Get memory details
svmem =  psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")


print("="*40, "SWAP", "="*40)
#Get swap memory details if it exist
# Memory the OS provide to a running app or process if there isnt enough ram to share 
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")


#################### Disk Usage ####################
# Disk info
print("="*40, "Disk Information", "="*40)
#Get all disk partition
partitions = psutil.disk_partitions()
for partition in partitions:
	print(f"=== Device: {partition.device} ===")
	print(f" Mountpoint: {partition.mountpoint}")
	print(f" File system type: {partition.fstype}")
	try:
		partition_usage = psutil.disk_usage(partition.mountpoint)
	except PermissionError:
		continue
	
	print(f" Total Size: {get_size(partition_usage.total)}")
	print(f" Used: {get_size(partition_usage.used)}")
	print(f" Free: {get_size(partition_usage.free)}")
	print(f" Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")


#################### Network usage ####################
print("="*40, "Network Information", "="*40)
# Get all network information
if_addrs = psutil.net_if_addrs()
# ds = psutil.net_connections()
# da = psutil.net_if_stats()
# dw = psutil.net_io_counters()
for interface_name, interface_addresses in if_addrs.items():
	for address in interface_addresses:
		print(f"=== Interface: {interface_name} ===")
		# getting the type of address your socket can communicate with
		if str(address.family) == "AddressFamily.AF_INET":
			print(f"IP Address: {address.address}")
			print(f" Netmask: {address.netmask}")
			print(f" Broadcast IP: {address.broadcast}")
		elif str(address.family) == "AddressFamily.AF_PACKET":
			print(f" MAC Address: {address.address}")
			print(f" Netmask: {address.netmask}")
			print(f" Broadcast MAC: {address.broadcast}")
#get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
