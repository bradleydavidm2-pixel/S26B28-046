# "and" is multiplication 
# "or" is addition

print(True or False)
print(True and False)

test1=int(input('Enter score in Test-I: '))
test2=int(input('Enter score in Test-II: '))
test3=int(input('Enter score in Test-III: '))
avg=(test1+test2+test3)/3
print('Average score is {avg}')
print ('Thanks for your time')

subject1=int(input('Enter score in subject1:'))
subject2=int(input('Enter score in subject2:'))
subject3=int(input('Enter score in subject3:'))
subject4=int(input('Enter score in subject4:'))
subject5=int(input('Enter score in subject5:'))
avg=(subject1+subject2+subject3+subject4+subject5)/5
print('Average score is {avg}')

if avg>=80:
    print('You are an outstanding student!')
if avg>=70 and avg<80:
    print('You are a good student!')
if avg>=60 and avg<70:
    print('You are an average student!')
if avg>=50 and avg<60:
    print('You are a below average student!')
if avg>=40 and avg<50:
    print('You are a poor student !')
if avg<40:
    print('You need extra ordinary efforts!')
       
