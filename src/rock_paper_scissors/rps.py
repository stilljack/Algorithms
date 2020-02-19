#!/usr/bin/python

import sys

rock = "rock"
paper = "paper"
scissors = "scissors"
def rock_paper_scissors(n):
  rockArr = [rock]
  scissorsArr = [scissors]
  paperArr = [paper]
  final =[]
  final.extend(recursive_rps(rockArr,n))
  final.extend(recursive_rps(paperArr,n))
  final.extend(recursive_rps(scissorsArr,n))
  return final

def recursive_rps(arr,depth):
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
    final.append(recursive_rps(rockR,depth))
    final.append(recursive_rps(scissorsR,depth))
    final.append(recursive_rps(paperR,depth))
   # print(f"final after extend {final}")
    return final

print(rock_paper_scissors(2))
# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
