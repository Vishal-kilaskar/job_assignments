"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking.
The game uses Dense Ranking, so its leaderboard works like this:
    The player with the highest score is ranked number on the leaderboard.
    Players who have equal scores receive the same ranking number,
    and the next player(s) receive the immediately following ranking number.

ex: r = [100, 90, 90, 80]
    p = [70, 80, 105]


The ranked players will have ranks 1, 2, 2, and 3, respectively.
If the player's scores are 70, 80 and 105, their rankings after each game are 4th,3rd and 1st. return [4, 3, 1]

"""

"""
solution to this is,

step 1) sort the ranked score in descending if the array is not sorted in descending . 
step 2) make all the elements in the array as unique. this is the scores already there in reverse sorted manner.
step 3) loop through the new players score (for loop) 
step 4) while we are in the loop do a while loop to check if the current looped element is greater than the last element
        of the sorted scores. (while loop)
step 5) if the above condition is true then remove the last element from the sorted array check till the condition fails    
step 6) if the condition fails grab the index of the current element/score of the player from the sorted arr.
step 7) finally return the rank of the new player ranks.

"""

"""
def game_rank(rank, player_score):
    sorted_array as  --> step1) and step 2) sorting rank.
    player_ranks --> to grab the rank of the player according to the score.
    for loop the player_score --> step 3) score/element
    while loop --> step 4) check the condition if the above score/elemnt is GE last element of the sorted_array
    if the above condition is true remove/pop the last element
    after end of the while loop append the index/rank of the the score to player_ranks --> step 6)
    finally return the player ranks ---> step 7)
"""

