#MagicEightbalList

import random

responses = ['it is certain','It is decidedly so','Yes','No',
            'Ask again later','Concentrate and ask again',
            'My reply is No','Outlook is not good','Very doubtful']

#answer = random.choice(responses)
answer = responses[random.randint(0,len(responses))]
print('Answer: ' + answer)

def eggs(someParameter):
    someParameter.append('Hello')
spam = [1,2,3]
eggs(spam)
print(spam)
