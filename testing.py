# Number of n digit stepping numbers
# naive approach is to run a loop for n digit number and check for every number if it is stepping
# In dp[i][j], i denotes number of digits and denotes last digit
# if there is only 1 digit: if i==1 dp(i,j) = 1
# if last digit is 0: id i == 0 dp(i,j) = dp(i-1, j+1)
# if last digit is 9 else if j == 9  dp(i,j) =dp(i-1, j-1)
# if not 0 nor 9 else:  dp(i,j) = dp(i-1, j-1) + dp (i-1, j+1)
# result is sum dp (n,j) where j varies from 1 to 9

# Python3 program to calculate
# the number of n digit
# stepping numbers.

# function that calculates
# the answer
def answer(n):
    # dp[i][j] stores count of
    # i digit stepping numbers
    # ending with digit j.
    dp = [[0 for x in range(10)]
          for y in range(n + 1)];

    # if n is 1 then answer
    # will be 1.
    if (n == 1):
        return 10;
    for j in range(10):
        dp[1][j] = 1;
        # Compute values for count
        # of digits more than 1.
    for i in range(2, n + 1):
        for j in range(10):

            # If ending digit is 0
            if (j == 0):
                dp[i][j] = dp[i - 1][j + 1];

                # If ending digit is 9
            elif (j == 9):
                dp[i][j] = dp[i - 1][j - 1];

                # For other digits.
            else:
                dp[i][j] = (dp[i - 1][j - 1] +
                            dp[i - 1][j + 1]);

                # stores the final answer
    sum = 0;
    for j in range(1, 10):
        sum = sum + dp[n][j];
    return sum;
# Driver Code
n = 2;
print(answer(n));