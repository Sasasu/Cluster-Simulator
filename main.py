#!/bin/python3
from __future__ import print_function

from machine import Machine
from cluster import Cluster
from simulator import Simulator

# user_number = 1
# machine_number = 800
# core_number = 1
# json_dir = "./"
#
# machines = [Machine(i, core_number) for i in range(0, machine_number)]
# cluster = Cluster(machines)
#
# simulator = Simulator(cluster, json_dir, user_number)
# cluster.alpha = 0.7
# cluster.totalJobNumber = 2
# simulator.scheduler.scheduler_type = "paf"
#
# simulator.run()
# print("finish")

import functools


def log(name_or_function):
    if callable(name_or_function):
        @functools.wraps(name_or_function)
        def wrapper(*args, **kwargs):
            print("starting")
            name_or_function(*args, **kwargs)
            print("ending")

        return wrapper

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("starting", name_or_function)
            func(*args, **kwargs)
            print("ending", name_or_function)

        return wrapper

    return decorator


@log
def test():
    print(111)


@log("test 2")
def test2():
    print(222)


test()
test2()
