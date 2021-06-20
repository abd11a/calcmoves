from itertools import product       # A Python prog to demo Cartesian product
                                    # (c) Abdullah H. Mohammed, June 2021

vals = ['+2', '/5', '*10']                  # LEVEL 23
ops = { vals[0]: (lambda x: x+2), 
        vals[1]: (lambda x: x//5),
        vals[2]: (lambda x: x*10), }

move_count = 4
starting_value = 15
target = 10
print_perms = 1==0  # set to true or false

moves = product (vals,repeat=move_count) 
 
for i in list(moves):
    res = starting_value
    commands = ''
    
    for j in range (move_count):
        commands +=  i[j]+' '
        res = ops[i[j]] (res)

    if print_perms:
     print (commands,'=>>',res)

    if res == target:
        print (commands,'=>>',res)
        print ('FOUND!\n')