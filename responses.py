import re


def Bot_Response(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        Bot_Response(message, ['hello', 'hi', 'hey', 'da'],
                     'Hello there, my name is doc ð '),

        Bot_Response(message, ['bye', 'goodbye'], 'pokalea nemba ð¥º!'),

        Bot_Response(message, ['pic', 'photo'], 'https://telegra.ph/file/3a7a36e0af99c49fdaf27.jpg'),

        Bot_Response(message, ['cmd', 'type cmd'], 'click here for more /list'),

        Bot_Response(message, ['how', 'are', 'you'],
                     'I\'m fine thanks âº!'),
        Bot_Response(message, ['ha', 'mm', 'ok'],
                     'yayað'),
        # new
        Bot_Response(message, ['how', 'you', 'created'],
                     'I was created by using python ð§âð» github https://github.com/azin7'),

        # Name
        Bot_Response(message, ['your', 'name'],
                     'My name is doc\'s Bot, nice to meet you !'),
        # Help
        Bot_Response(message, ['help', 'please'],
                     'I will do my best to assist you âº!'),
        # Website
        Bot_Response(message, ['link', 'links', ], 'https://telegra.ph/file/3a7a36e0af99c49fdaf27.jpg'),

        # Song
        Bot_Response(message, ['play', 'song', ],
                     'https://youtu.be/E5jIaox0iUc'),

        # Notes
        Bot_Response(message, ['azoo', 'azo', ],
                     'Hey, azoo will be available'),

        Bot_Response(message, ['socials', 'socials', ],
                     'Here you Go\n /socials'),

        Bot_Response(message, ['source', 'code', ],
                     'Here you Go\n /source_code'),

        # Joke
        Bot_Response(message, [
                     'nude', 'nudes', ], 'joke beno ena pm ba ð'),

        # When Querry
        Bot_Response(message, ['when', '?', 'query', 'question', 'inform',
                     'developer'], 'Inquire with the developer about this. @azi7x ð§âð»ð'),

        # When Website
        Bot_Response(message, ['website', 'az7i', 'web', 'developer'],
                     'https://linktr.ee/Zioi'),

        # When Projects
        Bot_Response(message, ['projects', 'project', 'proj','pro','projec', 'proje'],
                     'Here you Go\n /projects'),

        # When photo
        Bot_Response(message, ['7i', 'foto', 'dev','dey','azi77', 'pro'], 
                     'https://telegra.ph/file/3a7a36e0af99c49fdaf27.jpg'),
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand ð¥².'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response
