
def commaPrint(items):
    for i in range(len(items)):
        if i < len(items) - 1:
            print(items[i] + ', ', end='')
        else:
            print('and ' + items[i])

spam = []#'apples', 'bananas','tofu','cats']
commaPrint(spam)
