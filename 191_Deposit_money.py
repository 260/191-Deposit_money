#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/502

first_line  = input()
second_line = input()

number_of_people            = int(first_line)
deposit_moneys_of_people    = list(map(int, second_line.split(' ')))
paid_deposit_moneys_of_people = list(filter(lambda n: n<=sum(deposit_moneys_of_people)/10, deposit_moneys_of_people))

print(30 * len(paid_deposit_moneys_of_people))
