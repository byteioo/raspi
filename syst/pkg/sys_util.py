import os
import time

# 返回CPU温度 字符串
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=", "").replace("'C\n", ""))

# 返回cpu使用百分比
def getCPUusage():
    # calculate CPU with two short time, time2 - time1
    time1 = os.popen('cat /proc/stat').readline().split()[1:5]
    time.sleep(0.2)
    time2 = os.popen('cat /proc/stat').readline().split()[1:5]
    deltaUsed = int(time2[0]) - int(time1[0]) + int(time2[2]) - int(time1[2])
    deltaTotal = deltaUsed + int(time2[3]) - int(time1[3])
    cpuUsage = float(deltaUsed) / float(deltaTotal) * 100
    return round(cpuUsage,2)

# 返回一个 list 包含RAM信息
# Index 0: 总内存
# Index 1: 已使用内存
# Index 2: 剩余内存
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:4])



# 返回一个 list 包含硬盘信息
# Index 0: 总硬盘大小
# Index 1: 已使用硬盘大小
# Index 2: remaining disk space
# Index 3: 已使用 % 多少硬盘
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:5])




def sysInfo():
    RAM_stats = getRAMinfo()
    DISK_stats = getDiskSpace()
    return {
        "cpu_temperature":getCPUtemperature(),
        "cpu_used":getCPUusage(),
        "ram_total": round(int(RAM_stats[0]) / 1000, 1),
        "ram_used":round(int(RAM_stats[1]) / 1000, 1),
        "ram_free":round(int(RAM_stats[2]) / 1000, 1),
        "disk_total":str(DISK_stats[0]).replace("G",""),
        "disk_used":str(DISK_stats[1]).replace("G",""),
        "disk_used_percentage":str(DISK_stats[3]).replace("%","")

    }

if __name__ == '__main__':
    print(sysInfo())
    # CPU informatiom
    CPU_temp = getCPUtemperature()
    CPU_usage = getCPUusage()

    # RAM information
    # Output is in kb, here I convert it in Mb for readability
    RAM_stats = getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1000, 1)
    RAM_used = round(int(RAM_stats[1]) / 1000, 1)
    RAM_free = round(int(RAM_stats[2]) / 1000, 1)

    # Disk information
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_perc = DISK_stats[3]
    print('')
    print('CPU Temperature = ' + CPU_temp)
    print('CPU Use = ' + CPU_usage)
    print('')
    print('RAM Total = ' + str(RAM_total) + ' MB')
    print('RAM Used = ' + str(RAM_used) + ' MB')
    print('RAM Free = ' + str(RAM_free) + ' MB')
    print('')
    print('DISK Total Space = ' + str(DISK_total) + 'B')
    print('DISK Used Space = ' + str(DISK_used) + 'B')
    print('DISK Used Percentage = ' + str(DISK_perc))