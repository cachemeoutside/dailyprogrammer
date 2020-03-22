#!/usr/bin/python3
import csv

class BracketRange:
    def __init__(self, lower_income, upper_income, rate):
        self.lowerRange = lower_income
        self.upperRange = upper_income
        self.rate = rate

def main():
    MAX_INCOME = 100000000
    income_list = []
    with open('tax_table.csv', newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        header = next(r)
        for e in r:
            income_list.append((int(e[0]), int(e[1]), float(e[2])))
    bracket_table = []
    bracket_table = create_tax_bracket(income_list)

    income_list = [0, 10000, 10009, 10010, 12000, 56789, 1234567]
    for income in income_list:
        if not exceed_max_income(income, MAX_INCOME):
            print("tax(%d) => %d" % (income, calc_taxes(income, bracket_table)))
        else:
            print("%d is not a valid income" % income)

def create_tax_bracket(bracket_table):
    bTable = []
    for bracket in bracket_table:
        bTable.append(BracketRange(bracket[0], bracket[1], bracket[2]))
    return bTable

def calc_taxes(income, bracket_table):
    calc_income_tax = 0
    for bracket in bracket_table:
        if income >= bracket.lowerRange and income <= bracket.upperRange:
            return round(calc_income_tax + ((income - bracket.lowerRange) * bracket.rate))
        else:
            calc_income_tax = calc_income_tax + ((bracket.upperRange - bracket.lowerRange) * bracket.rate)

def exceed_max_income(income, max_income):
    if income > max_income:
        return True
    else:
        return False

main()
