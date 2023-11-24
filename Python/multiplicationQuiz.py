#MultiplicationQuiz

import pyinputplus as pyip
import random, time
numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    # using input regular expressions to force restricting the input to the correct answer
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                        blockRegexes=[('.*', 'Incorrect!')],
                        timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Sorry out of time!")
    except pyip.RetryLimitException:
        print("Sorry. out of tries")
    else:
        print("Correct!")
        correctAnswers += 1
    #endelse
    time.sleep(1)
    print("Score: %s /%s" % (correctAnswers, numberOfQuestions))

