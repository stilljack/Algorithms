#!/usr/bin/python


import itertools


#completeList = rock+paper+scissors
##
##this ain't working out,
##when we come back to this:
## what about not bothering with recursions?
## can't we find the size of the lists needs, then populate them?
## maybe with list comprehensions?

cache = {}

#curtosy austin michaud
# rock = ["rock"]
# paper = ["paper"]
# scissors = ["scissors"]
# available_options = ["rock", "paper", "scissors"]
# def rock_paper_scissors(n):
#     if n == 0:
#         return [[]]
#     if n == 1:
#         return [rock, paper, scissors]
#     return rps_helper(n, rock) + rps_helper(n, paper) + rps_helper(n, scissors)
# def rps_helper(n, list):
#     if n == 1:
#         return [list]
#     rockList, paperList, scissorList = list[:], list[:], list[:]
#     rockList += rock
#     paperList += paper
#     scissorList += scissors
#     n -= 1
#     return (
#         rps_helper(n, rockList) + rps_helper(n, paperList) + rps_helper(n, scissorList)
#     )

rock = ["rock"]
paper = ["paper"]
scissors = ["scissors"]
rps = [rock,paper,scissors]
available_options = ['rock', 'paper', 'scissors']

def rock_paper_scissors(n):
    if n==0:
        return [[]]
    if n==1:
        return rps
    return rps_helper(n,rock)+rps_helper(n,paper)+rps_helper(n,scissors)


def rps_helper(n,list):
    if n ==1:
        return list
    if n ==2:
        rockList=list.copy()
        paperList=list.copy()
        scissorList=list.copy()
        rockList.extend(rock)
        paperList.extend(paper)
        scissorList.extend(scissors)
        n-=1
        return [rps_helper(n,rockList), rps_helper(n,paperList), rps_helper(n,scissorList)]
    else:
        rockList=list.copy()
        paperList=list.copy()
        scissorList=list.copy()
        rockList.extend(rock)
        paperList.extend(paper)
        scissorList.extend(scissors)
        n-=1
        return rps_helper(n,rockList) + rps_helper(n,paperList) + rps_helper(n,scissorList)

print(rock_paper_scissors(6))







#
#
#
#
# def D_rock_paper_scissors(n):
#     rockArr = [rock]
#     scissorsArr = [scissors]
#     paperArr = [paper]
#     final =[]
#     final.extend(rps_recur(rockArr,n))
#     final.extend(rps_recur(scissorsArr,n))
#     final.extend(rps_recur(paperArr,n))
#     return final
#
# def rps_recur(currentArray:list,depth):
#     depth-=1
#     if depth<=0:
#         return currentArray
#     rockResult = currentArray.copy()
#     scissorsResult =currentArray.copy()
#     paperResult = currentArray.copy()
#     rockResult.append(rock)
#     scissorsResult.append(scissors)
#     paperResult.append(paperResult)
#     final =[]
#     final.append(rps_recur(rockResult,depth))
#     final.append(rps_recur(scissorsResult,depth))
#     final.append(rps_recur(paperResult,depth))
#     return final
#
#
#
#
#
# def old_rock_paper_scissors(n):
#   rockArr = [rock]
#   scissorsArr = [scissors]
#   paperArr = [paper]
#   final =[]
#   final.extend(old_recursive_rps(rockArr,n))
#   final.extend(old_recursive_rps(paperArr,n))
#   final.extend(old_recursive_rps(scissorsArr,n))
#   return final
#
# def old_recursive_rps(arr,depth):
#     depth-=1
#     if depth <= 0:
#       return arr
#
#     rockR=arr.copy()
#     scissorsR=arr.copy()
#     paperR=arr.copy()
#   #  print(f"sanity: rockr{rockR}\n sci{scissorsR}\n paperr{paperR}")
#     rockR.append(rock)
#     paperR.append(paper)
#     scissorsR.append(scissors)
#     #print(f"sanity: rockr{rockR}\n sci{scissorsR}\n paperr{paperR}")
#
#     final =[]
#     final.append(old_recursive_rps(rockR,depth))
#     final.append(old_recursive_rps(paperR,depth))
#     final.append(old_recursive_rps(scissorsR,depth))
#     return final

# def newrps(numberOfPerMutations):
#     result =[]
#     if 0 <= numberOfPerMutations:
#         return None
#     if numberOfPerMutations==1:
#         return rps
#     for count in numberOfPerMutations:
#         for permutations in numberOfPerMutations:
#             result.append(rock)
#             pass

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
