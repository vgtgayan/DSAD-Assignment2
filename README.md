# DSAD-Assignment2
1. Problem Statement
You have recently opened a fast-food joint in one of the most crowded markets of your city. Since
the area is an expensive one, the shops are not too large and you have a tight fund to stick to.
Through extensive research and surveys, you have identified certain preparations that might work in
your area. You need to allocate funds for food preparations. Since different food preparations use
different ingredients, their costs differ. Through your surveys and research, you also have an
estimate of the profit you might obtain on the given food preparation while remaining competitive in
your area. Excluding rent and other utilities, you have a total of 15 lakhs to be allocated to different
food preparations for a month. Here your task would be to select as many preparations as possible
with the fund constraints such that the total profit is maximized. If there are multiple solutions with
same profit, choose the one which results in maximum utilization of funds and selection of
preparations as well, as more variety in food is generally preferred.

Requirements:
1. Formulate an efficient recursive algorithm using Dynamic Programming to determine how to
select the preparations to be funded and maximize PROFIT.
2. Analyse the time complexity of your algorithm.
3. Implement the above problem statement using Python 3.7

Sample Input:
For example, if there are 10 different preparations in total and their fund requirements and values
are given as shown:

Preparations(i)/Cost(lakhs)/PROFIT(lakhs)
1 / 3 / 6
2 / 1.7 / 3.5
3 / 2 / 5.5
4 / 1 / 4
5 / 1.3 / 6.6
6 / 1 / 2
7 / 1.6 / 3.5
8 / 2.5 / 5
9 / 1.5 / 7
10 / 1.8 / 1

Sample Output:
The preparations that should be funded: 1,2,3,4,5,7,8,9
Total PROFIT: 41.1
Fund remaining: 0.4

Display the output in outputPS15.txt.
