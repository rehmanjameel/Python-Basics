import math

import psutil
import time

from datetime import datetime

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


def get_current_time():
    now = datetime.now()
    current_date = now.strftime("%b %d, %Y %H:%M")
    print(current_date)
    return current_date


def get_systime():
    system_start_time = time.time() - psutil.boot_time()
    formatted_time = time.strftime("%H hours %M min %S sec", time.gmtime(system_start_time))
    print(formatted_time)
    return formatted_time


def to_celsius(f):
    celsius = (f - 32) / 1.8
    print(celsius)
    return celsius


def to_fahrenheit(c):
    fahrenheit = c * 1.8 + 32
    print(fahrenheit)
    return fahrenheit


def find_square(square):
    sq_root = square * square
    print(sq_root)
    return sq_root


def find_pi(pi_value):
    value = pi_value * math.pi
    print(value)
    return value


def find_cpu_cores():
    total = psutil.cpu_count()
    cpu_cores = psutil.cpu_count() / 2
    threads_percore = psutil.cpu_count() / psutil.cpu_count(logical=False)
    info = {"cores": cpu_cores,
            "threads_per_core": threads_percore,
            "cpu_count": total}
    print(info)
    return info


def get_remaining_ram():
    ram_free_space = (psutil.virtual_memory()[4]) / (1024 * 1024 * 1024)
    print(ram_free_space)
    return ram_free_space


class SysTimeComponent(ApplicationSession):

    async def onJoin(self, _details):
        reg1 = await self.register(get_systime, "org.deskconn.sys.get_sys_uptime")
        self.log.info("Registered procedure {procedure}", procedure=reg1.procedure)

        reg2 = await self.register(get_current_time, "org.deskconn.sys.curr_time")
        self.log.info("Registered procedure {procedure}", procedure=reg2.procedure)

        reg3 = await self.register(to_celsius, "org.deskconn.sys.to_celsius")
        self.log.info("Registered procedure {procedure}", procedure=reg3.procedure)

        reg4 = await self.register(to_fahrenheit, "org.deskconn.sys.to_fahrenheit")
        self.log.info("Registered procedure {procedure}", procedure=reg4.procedure)

        reg5 = await self.register(find_square, "org.deskconn.sys.get_sqrt")
        self.log.info("Registered procedure {procedure}", procedure=reg5.procedure)

        reg6 = await self.register(find_cpu_cores, "org.deskconn.sys.get_cpu_cores")
        self.log.info("Registered procedure {procedure}", procedure=reg6.procedure)

        reg7 = await self.register(get_remaining_ram, "org.deskconn.sys.ram_space")
        self.log.info("Registered procedure {procedure1}", procedure1=reg7.procedure)

        reg8 = await self.register(find_pi, "org.deskconn.sys.get_pi_value")
        self.log.info("Registered procedure {procedure}", procedure=reg8.procedure)


if __name__ == '__main__':
    runner = ApplicationRunner("ws://0.0.0.0:8080/ws", realm="realm1")
    runner.run(SysTimeComponent)

# C to F, F to C, pi, square root, cpu cores, free ram
