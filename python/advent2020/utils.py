from os import path
from decimal import Decimal
import numpy as np
import itertools

dir_path = path.dirname(path.realpath(__file__))


def read_string(file_name):
    file_path = path.join(dir_path, "data", file_name)
    with open(file_path, "r") as f:
        return f.read()


def read_strings(file_name):
    file_path = path.join(dir_path, "data", file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def read_strings_2d(file_name, split_by=","):
    return [s.split(split_by) for s in read_strings(file_name)]


def read_ints(name, split_by=","):
    list2d = read_ints_2d(name, split_by)
    return list(itertools.chain.from_iterable(list2d))


def read_ints_2d(name, split_by=","):
    return [[int(c) for c in s.split(split_by)] for s in read_strings(name)]


def read_floats(name, split_by=","):
    list2d = read_floats_2d(name, split_by)
    return list(itertools.chain.from_iterable(list2d))


def read_floats_2d(name, split_by=","):
    return [[float(c) for c in s.split(split_by)] for s in read_strings(name)]


def read_decimals(name):
    return [Decimal(s) for s in read_strings(name)]


def read_np_ints(name):
    return np.array(read_ints(name), dtype=np.int)


def read_np_int_2d(name, split_by=","):
    a = [s.split(split_by) for s in read_strings(name)]
    return np.array(a, dtype=np.int)


def read_np_floats(name):
    return np.array(read_floats(name), dtype=np.float32)


def read_np_float_2d(name, split_by=","):
    a = [s.split(split_by) for s in read_strings(name)]
    return np.array(a, dtype=np.float32)


