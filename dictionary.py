import random

ques={1:'what is your name?',2:'how are you?',3:'what is your favourite food?',4:'what is your hobby?',5:'what is your dream?',6:'where do you live?',7:'which is your favourite subject?',8:'what is your favourite game?',9:'who is your best friend?',10:'did you feel good after talking to me?'}
ans={'what is your name?':'Sreebrata Das','how are you?':'very good','what is your favourite food?':'All types of bengali sweets','what is your hobby?':'dancing','what is your dream?':'IAF officer','where do you live':'behala','which is your favourite subject?':'maths','what is your favourite game?':'cricket','who is your best friend?':'Rudrajit Choudhuri','did you feel good after talking to me?':'Yes i loved it'}

r=random.randint(1,10)

print(ques[r])
n=input('Enter Answer: ')

if (n==ans[ques[r]]):
    print('Correct Answer')
else:
    print('Incorrect Answer')
    