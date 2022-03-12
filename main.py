# ----------------------------------------------------------------
# Assignment 2 – PS15 - [Fastfood Joint]
# ----------------------------------------------------------------
# 1. Problem Statement
# You have recently opened a fast-food joint in one of the most crowded markets of your city. Since
# the area is an expensive one, the shops are not too large and you have a tight fund to stick to.
# Through extensive research and surveys, you have identified certain preparations that might work in
# your area. You need to allocate funds for food preparations. Since different food preparations use
# different ingredients, their costs differ. Through your surveys and research, you also have an
# estimate of the profit you might obtain on the given food preparation while remaining competitive in
# your area. Excluding rent and other utilities, you have a total of 15 lakhs to be allocated to different
# food preparations for a month. Here your task would be to select as many preparations as possible
# with the fund constraints such that the total profit is maximized. If there are multiple solutions with
# same profit, choose the one which results in maximum utilization of funds and selection of
# preparations as well, as more variety in food is generally preferred.

# Requirements:
# 1. Formulate an efficient recursive algorithm using Dynamic Programming to determine how to
# select the preparations to be funded and maximize PROFIT.
# 2. Analyse the time complexity of your algorithm.
# 3. Implement the above problem statement using Python 3.7

# Sample Input:
# For example, if there are 10 different preparations in total and their fund requirements and values
# are given as shown:
# Input should be taken in through a file called “inputPS15.txt” which has the fixed format
# mentioned below using the “/” as a field separator:

# <Preparation Name i> / < Cost Ci(crores)> / < PROFIT Ri>
# Ex:
# 1 / 3 / 6
# 2 / 1.7 / 3.5
# 3 / 2 / 5.5
# 4 / 1 / 4
# 5 / 1.3 / 6.6
# 6 / 1 / 2
# 7 / 1.6 / 3.5
# 8 / 2.5 / 5
# 9 / 1.5 / 7
# 10 / 1.8 / 1

# Sample Output:
# The preparations that should be funded: 1,2,3,4,5,7,8,9
# Total PROFIT: 41.1
# Fund remaining: 0.4
# Display the output in outputPS15.txt


class fastFoodJoint(object):
    def __init__(self, input_file, output_file):
        '''
			1. Read the input file
            2. Call get_optimum_preparations
            3. Write to output file
		'''
        
        # Read input file
        self.preperation_list, self.cost_list, self.profit_list= self.read_input_file(input_file)
        # print("Preperations: ", self.preperation_list)
        # print("Costs: ", self.cost_list)
        # print("Profits: ", self.profit_list)

        # Available total fund (in lakhs)
        self.total_fund = 15

        # Initialize Memoization table (Dynamic programming)
        # Since profit is a floating point number and cannot be used for indexing,
        # indices of the Memoization table has to be managed separately
        self.mem = []
        self.mem_indices = []
        
        self.outputfile = output_file

        # Obtain the optimum preparations
        self.total_profit, self.total_cost, self.selected_preparation_list = self.get_optimum_preparations(len(self.preperation_list), self.total_fund)
        output_msg = f"The preparations that should be funded: {self.selected_preparation_list}\n"
        output_msg += f"Total PROFIT: {self.total_profit}\n"
        output_msg += f"Fund remaining: {round(self.total_fund - self.total_cost, 2)}\n"
        print(output_msg)
        self.write_to_file(output_msg)
        
    def read_input_file(self, input_file):
        '''
            Reads input_file
        '''
        try:
            with open(input_file, "r") as f:
                data = f.readlines()
                
            preperation_list = []
            cost_list = []
            profit_list = []
            for line in data:
                line_ = line.split("/")
                preperation_list.append(int(line_[0].strip()))
                cost_list.append(float(line_[1].strip()))
                profit_list.append(float(line_[2].strip()))

            return preperation_list, cost_list, profit_list

        except Exception as e:
            print(e)
            
    def write_to_file(self, message):
        '''
    	This is the helper function that writes a given string into 
    	the output file "outputPS15.txt"
        '''
        try:
            out_file = open(self.outputfile, 'a')
            out_file.write(message)
            out_file.close()
        except Exception as e:
            print(e)


    def get_optimum_preparations(self, n, total_fund):
        """
        Inputs:
            n           - No: of preparations
            total_fund  - Maximum amount of fund available

        Outputs:
            total_profit         
            total_cost
            selected_preparation_list
        """
        try:
            # Case 0: a) (Base case) Either no fund left or no preperations left
            if n == 0 or total_fund == 0:
                return 0,0,[]

            # Case 0: b) (Base case) Previously solved sub problem (Dynamic programming)
            # Get result from the memoization table
            mem_key = f"{n}_{round(total_fund,1)}"
            if mem_key in self.mem_indices:
                # print("Getting result from the memoization table. Key: ", mem_key)
                mem_index = self.mem_indices.index(mem_key)
                return self.mem[mem_index]

            # Case 1: Cost of the nth preparation is greater than current fund balance
            #         Skip nth preparation
            elif self.cost_list[n-1] > total_fund:
                self.mem.append(self.get_optimum_preparations(n-1, total_fund))
                self.mem_indices.append(f"{n}_{round(total_fund,1)}")
                return self.mem[-1]

            # Case 2: Cost of the nth preparation is less than or equal to current fund balance
            #         Return maximum of below 2 cases        
            #           a) Select nth preparation
            #           b) Drop nth preparation
            #           c) When both a and b have equal profits
            else:
                # a) Select nth preparation
                profit1, cost1, prep_list1 = self.get_optimum_preparations(n-1, total_fund-self.cost_list[n-1])
                profit1 += self.profit_list[n-1]

                # b) Drop nth preparation
                profit2, cost2, prep_list2 = self.get_optimum_preparations(n-1, total_fund)
                # a) Select nth preparation
                if profit1 > profit2:
                    total_profit = profit1
                    total_cost = cost1 + self.cost_list[n-1]
                    selected_preparation_list = prep_list1 + [self.preperation_list[n-1]]
                # c) When both a and b have equal profits
                elif profit1 == profit2:
                    # Choose solution with more preparations
                    if len(prep_list1) >= len(prep_list2):
                        total_profit = profit1
                        total_cost = cost1 + self.cost_list[n-1]
                        selected_preparation_list = prep_list1 + [self.preperation_list[n-1]]
                    else:
                        total_profit = profit2
                        total_cost = cost2
                        selected_preparation_list = prep_list2
                # b) Drop nth preparation
                else:
                    total_profit = profit2
                    total_cost = cost2
                    selected_preparation_list = prep_list2

                # self.mem[n][total_fund] =  (total_profit, total_cost, selected_preparation_list)
                # return self.mem[n][total_fund]
                self.mem.append((total_profit, total_cost, selected_preparation_list))
                self.mem_indices.append(f"{n}_{round(total_fund,1)}")
                return self.mem[-1]
            
        except Exception as e:
            print(e)

        


if __name__ == "__main__":
    fastFoodJoint('inputPS15.txt', 'outputPS15.txt')