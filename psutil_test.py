import psutil

print(psutil.cpu_times(), end="\n")
print(psutil.cpu_percent(1), end="\n")
print(f"number of cores in  system {psutil.cpu_count()}", end="\n")

print("CPU statistics", psutil.cpu_stats(), end="\n")
print(psutil.cpu_freq(), end="\n\n")
print(psutil.getloadavg(), end="\n\n")
print("virtual memory:", psutil.virtual_memory(), end="\n\n")
print("disk partitions:", psutil.disk_partitions(), end="\n\n")
print("disk usage:", psutil.disk_usage('/run/media/Xashe/USB_DATA'), end="\n\n")

print(psutil.net_io_counters(), end="\n\n")

print("net connections:", psutil.net_connections(), end="\n\n")

print("if addrs:", psutil.net_if_addrs(), end="\n\n")

print("sensor temperatures:", psutil.sensors_temperatures(), end="\n\n")

print("sensors fans:", psutil.sensors_fans(), end="\n\n")

print("sensor battery:", psutil.sensors_battery(), end="\n\n")

print("boot time:", psutil.boot_time(), end="\n\n")

print("users -> ", psutil.users(), end="\t")
