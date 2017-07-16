#! python3
'''
quizGenerator creates multiple choice quizzes with random question order and
 stores an answer key for each
 '''
import random

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
    'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
    'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho':
    'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina':
    'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma':
    'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota':
    'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah':
    'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
    'Washington': 'Olympia', 'Iowa': 'Des Moines', 'West Virginia':
    'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# genereate 35 quiz files
for quizNum in range(3):
    # create quiz and answer key
    quizFile = open('capital quiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('capitalquiz%s_answerKey.txt' % (quizNum + 1), 'w')
    # print header on quiz
    quizFile.write(
        'Name:' + ('_' * 10) + ' ' * 3 +
        'Date:' + ('_' * 10) + ' ' * 3 +
        'Class:' + ('_' * 10) + '\n\n')
    quizFile.write(
        (' ' * 20) + 'State Capitals Quiz (Form %s)' %
        (quizNum + 1))
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(len(capitals) - 1):
        # gets correct and other answers, shuffles them and makes a list
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # writes question
        quizFile.write(
            '%s. What is the Capital of %s?\n' % (questionNum + 1,
                                                  states[questionNum]))
        # writes multiple choice
        for i in range(4):
            quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
        answerFile.write(
            '%s. %s\n' % (questionNum + 1,
                          'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()
