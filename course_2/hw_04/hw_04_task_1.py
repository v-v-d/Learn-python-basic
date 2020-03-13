#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 1.
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description='Employee payroll calculation.')
    parser.add_argument(
        '-p', '--production', type=int, required=True,
        help='Employee production, hours'
    )
    parser.add_argument(
        '-r', '--rate', type=int, required=True,
        help='Employee rate, currency'
    )
    parser.add_argument(
        '-b', '--bonus', type=int, required=True,
        help='Employee bonus, currency'
    )
    return parser.parse_args()


def payroll_calculation(production, rate, bonus):
    return production * rate + bonus


if __name__ == '__main__':
    PARSER = parse_args()

    print(payroll_calculation(PARSER.production, PARSER.rate, PARSER.bonus))
