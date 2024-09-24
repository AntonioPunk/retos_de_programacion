def function_recur(number):
    if number >= 0:
        print(number)    
        function_recur(number-1)
        
function_recur(100)
