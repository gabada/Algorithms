#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # max_profit = -1000
    # min_value = prices[0]
    # max_value = -1000
    # if len(prices) < 2:
    #     return 0
    # for price in prices:
    #     if price < min_value:
    #         min_value = price
    #         # print(min_value)
    #         min_index = prices.index(min_value)
    #         # print(min_index)
    # for price in prices[min_index:]:
    #     print(min_value)
    #     print(prices[min_index:])
    #     if price >= max_value:
    #         max_value = price
    #         print(max_value)
    #     if max_value == prices[-1]:
    #         return prices[-1] * -1
    # return(max_value - min_value)

    #Find max profit from the highest 
    # highest then look for highest in right

    # find max profit from lowest
    # lowest then look right for highest number

    # return higher of each



    # if len(prices) < 2:
    #     return 0
    # for price in prices:
    #     current_price = price
    #     # if current_price + 1 < len(prices):
    #     max_index = prices.index(current_price)
    #     max_price = prices[max_index]
    #     print("CUR", current_price)
    #     if max_price - current_price > max_profit:
    #         max_profit = max_price - current_price
    # return max_profit
    max_profit = 0
    for i in range(0, len(prices)):
        current_price = prices[i]
        # print('current PRICE', current_price)
        for j in range(i, len(prices)):
            next_price = prices[j]
            # print('next PRICE', next_price)
            current_profit = next_price - current_price
            # print('CURRENT PROFIT', current_profit)

            if current_profit > max_profit:
                max_profit = current_profit
                # print('MAX PROFIT', max_profit)
    if max_profit == 0:
        return prices[-1] * -1
    return max_profit

    #     if highest_price - current_price > max_profit:
    #         max_profit = highest_price - current_price
    # return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))



"""
Problem
-------

iterate through the list find the lowest number before the highest
subtract lowest from highest

Find lowest number and record number and index.

Plan
-----

place to store low index
please to store low value
place to store high index
place to store high value


step 1: find max profit from the highest number
step 2: find max profit from the lowest number
step 3 return whichever is greater

"""