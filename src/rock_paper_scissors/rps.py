#!/usr/bin/python

import sys

import itertools

rock = "rock"
paper = "paper"
scissors = "scissors"
initSet=[rock,paper,scissors]

##
##this ain't working out,
##when we come back to this:
## what about not bothering with recursions?
## can't we find the size of the lists needs, then populate them?
## maybe with list comprehensions?

def rock_paper_scissors(n):
    rockArr = [rock]
    scissorsArr = [scissors]
    paperArr = [paper]
    final =[]
    final.extend(rps_recur(rockArr,n))
    final.extend(rps_recur(scissorsArr,n))
    final.extend(rps_recur(paperArr,n))
    return final

def rps_recur(currentArray:list,depth):
    depth-=1
    if depth<=0:
        return currentArray
    rockResult = currentArray.copy()
    scissorsResult =currentArray.copy()
    paperResult = currentArray.copy()
    rockResult.append(rock)
    scissorsResult.append(scissors)
    paperResult.append(paperResult)
    final =[]
    final.append(rps_recur(rockResult,depth))
    final.append(rps_recur(scissorsResult,depth))
    final.append(rps_recur(paperResult,depth))
    return final



print(rock_paper_scissors(2))

def old_rock_paper_scissors(n):
  rockArr = [rock]
  scissorsArr = [scissors]
  paperArr = [paper]
  final =[]
  final.extend(old_recursive_rps(rockArr,n))
  final.extend(old_recursive_rps(paperArr,n))
  final.extend(old_recursive_rps(scissorsArr,n))
  return final

def old_recursive_rps(arr,depth):
    depth-=1
    if depth <= 0:
      return arr

    rockR=arr.copy()
    scissorsR=arr.copy()
    paperR=arr.copy()
  #  print(f"sanity: rockr{rockR}\n sci{scissorsR}\n paperr{paperR}")
    rockR.append(rock)
    paperR.append(paper)
    scissorsR.append(scissors)
    #print(f"sanity: rockr{rockR}\n sci{scissorsR}\n paperr{paperR}")

    final =[]
    final.append(old_recursive_rps(rockR,depth))
    final.append(old_recursive_rps(paperR,depth))
    final.append(old_recursive_rps(scissorsR,depth))
    return final


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
