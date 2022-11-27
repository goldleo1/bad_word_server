
import platform
import psutil
import torch
import cpuinfo


def OS_Info():

    return'OS                   :\t'+platform.system()


def OS_Version():
    return 'OS Version           :\t' + platform.version().split('.')[0]


def RamInfo():

    return'RAM Size             :\t' + str(
        round(psutil.virtual_memory().total / (1024.0 ** 3)))+"(GB)"


def CpuInfo():
    V = cpuinfo.get_cpu_info()
    return V['brand_raw']


def GpuInfo():
    if torch.cuda.is_available():
        return 'GPU : '+torch.cuda.get_device_name(0)
    else:
        return 'GPU : None'


if __name__ == '__main__':

    print(OS_Info())
    print(RamInfo())
