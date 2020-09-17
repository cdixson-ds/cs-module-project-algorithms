#!/usr/bin/python

import sys



options = ['rock', 'paper', 'scissors']

#n is the number of rounds
def rock_paper_scissors(n):

  results = []

  def rps(play, remain):  #recursive function
    if remain == 0:       #remaining turns
      results.append(play)
      return

    for o in options:
      rps([*play, o], remain-1)

  rps([], n)
  return results

  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')