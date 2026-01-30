import psutil

print(psutil.cpu_times(), end="\n")
print(psutil.cpu_percent(1), end="\n")
print(f"number of cores in  system {psutil.cpu_count()}", end="\n")

print("CPU statistics", psutil.cpu_stats(), end="\n")
print(psutil.cpu_freq(), end="\n\n")
print(psutil.getloadavg(), end="\n\n")
print(psutil.virtual_memory(), end="\n\n")
print(psutil.disk_partitions(), end="\n\n")
print(psutil.disk_usage('/run/media/Xashe/USB_DATA'), end="\n\n")

print(psutil.net_io_counters())

print(psutil.net_connections())

print(psutil.net_if_addrs())

print(psutil.sensors_temperatures())

print(psutil.sensors_fans())

print(psutil.sensors_battery())

print(psutil.boot_time())

print(psutil.users())
