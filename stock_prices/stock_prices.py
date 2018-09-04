#!/usr/bin/python

import argparse

def find_max_profit(prices):
  for i in range(len(prices)):
    if prices[i] > prices[i-1]:
      max = prices[i]
    if prices[i] < prices[i-1]:
      min = prices[i]
  maxProfit = max - min
  print(maxProfit)


if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))



  #Runtime complexity = O(n)