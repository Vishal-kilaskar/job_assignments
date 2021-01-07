"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record for most points and least points in a game.
Points scored in the first game establish her record for the season, and she begins counting from there.

"""


"""
solution for this is,

we need 4 variables to keep the track of her high scores and low score and counters for high and low score respectively.
step 1) we loop through the length of the scores by her.

step 2) if the first index i.e 0 we assume that her highest and lowest score are same as of index 0 or in starting.

step 3) if the score of ith game is greater then the highest score we then set the highest score to the ith game score
        and we also increment the highest counter to +1 

step 4) if the score of the ith game is less than the lowest score then we set the lowest score value to the ith game 
        score and we increment the lowest counter to +1
        
step 5) finally we return the count of highest counter and lowest counter.

Note:  we are not doing anything if the score is equal to either highest score or lowest score  

"""

"""
for i in range(len(score_list)):
    if i == 0:
        highest_score = score_list[i]
        lowest_score = highest_score
    elif score_list[i] > highest_score:
        highest_score = score_list[i]
        highest_count += 1
    elif score_list[i] < lowest_score:
        lowest_score = score_list[i]
        lowest_count += 1

return highest_count, lowest_count


"""