# (*args , **kwargs)in python)

def add(a, b ,c ) :
    print(a+b+c)

add(2,4,7)

## using args argumnet 

def add(*args):
    # print(args) # This line is a comment and can be removed
    sum_total = 0 # It is a good practice to avoid using 'sum' as a variable name
    for i in args:
        sum_total += i
    return sum_total # Return the calculated total

# Call the function and store the result in a variable
result = add(2, 4, 7, 8, 9, 10)

# Print the final result
print(result)
   
def multiply(*args) :
    # print(args) 

    multiply = 1 
    for i in args : 
        multiply = multiply * i 

    return multiply
    
mul_result = multiply(2,4,6,8,10)
print("The multiple is mul_result is : " , mul_result )

## another 

def myfunc(*args) : 
    for arg in args :
        print(arg)

myfunc("welcome", "to", "Nepal") 


# keyword arguments (*kwrgs)

def keyword_args(**kwrgs) :
    for k , val in kwrgs.items() : 
        print (k , ":" ,val) 


keyword_args(s1 = 'Python', s2 = 'is', s3 ='Awesome')
print(keyword_args)


# another 
def introduce(**kwrgs) :
    detils = []
    for k , val in kwrgs.items() :
        detils.append(k + ":" + str(val))
    return " , " .join(detils) 

print(introduce(Name="Alice", Age=25, City="New York"))  



def company_details(**kwrgs) : 
    for k , val in kwrgs.items() : 
     print(k , val )

print(company_details(name = "Abuzer_company" , address = "brt_06"))


