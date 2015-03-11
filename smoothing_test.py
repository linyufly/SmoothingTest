# Author: Mingcheng Chen (linyufly@gmail.com)

import sys
import numpy as np

def smooth_1(state, num_repetitions):
  print state

  if num_repetitions > 0:
    new_state = [None] * len(state)
    
    new_state[0] = state[1]
    new_state[-1] = state[-2]

    for index in range(1, len(state) - 1):
      new_state[index] = (state[index - 1] + state[index + 1]) / 2.0

    smooth_1(new_state, num_repetitions - 1)

def smooth_2(state, num_repetitions):
  print state

  if num_repetitions > 0:
    new_state = [0.0] * len(state)

    new_state[1] += state[0] - state[1];
    new_state[-2] += state[-1] - state[-2];

    for index in range(1, len(state) - 1):
      average = (state[index - 1] + state[index + 1]) / 2.0

      delta = (state[index] - average) / 2.0
      new_state[index - 1] += delta;
      new_state[index + 1] += delta;

    for index in range(0, len(state)):
      new_state[index] += state[index]

    smooth_2(new_state, num_repetitions - 1)

def main():
  init_state = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  print 'smooth_1'
  smooth_1(init_state, int(sys.argv[1]))
  print 'smooth_2'
  smooth_2(init_state, int(sys.argv[1]))

if __name__ == '__main__':
  main()
