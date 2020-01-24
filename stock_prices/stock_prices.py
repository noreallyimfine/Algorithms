#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # set current max profit
    current_max_profit = float("-inf")
    # for every price:
    for i, price in enumerate(prices):
        for p in prices[i+1:]:
            trade_profit = p - price
            # check if max profit it could make is bigger
            if trade_profit > current_max_profit:
                # reset max profit
                current_max_profit = trade_profit
    return current_max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N',
                        type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
