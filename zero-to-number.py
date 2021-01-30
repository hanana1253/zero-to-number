#Start make zero-to-number game

# ex) input = 3 / output = 1 + 2 + 3

# Print prompt message to get the number from user and save the value into input_num variable.
sum_ = 0
input_num = int(input('Please enter the number (1 ~ 10) : '))

for i in range(0,input_num+1):
    sum_ += 1
    
print(sum_)
