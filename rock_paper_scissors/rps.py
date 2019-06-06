#!/usr/bin/python

import sys

possible_plays = [['rock'], ['paper'], ['scissors']]

# 2= [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
    # ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'],
    # ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

def rock_paper_scissors(n):
    if n <= 0:
        return [[]]
    if n == 1:
        return([['rock'], ['paper'], ['scissors']])
    i = 0
    j = 0
    x = []
    while i < 3:
        rock = (possible_plays[0] + possible_plays[i] * (n - 1))
        x.append(rock)
        paper = (possible_plays[1] + possible_plays[i] * (n - 1))
        x.append(paper)
        scissors = (possible_plays[2] + possible_plays[i] * (n - 1))
        x.append(scissors)
        i += 1



        #     plays = ([possible_plays[0] + possible_plays[j] ] * n + [possible_plays[1] + possible_plays[j]] + [possible_plays[2] + possible_plays[j]])
        #     j+=1
        #     # print(plays)
    print(x)
    # return(x)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')