import pyttsx
engine = pyttsx.init()
engine.say('HELLO ammulu')
engine.setProperty('rate', 100)

engine.say('Python supports a concept called "list comprehensions". It can be used to construct lists in a very natural, easy way, like a mathematician is used to do.The following are common ways to describe lists (or sets, or tuples, or vectors) in mathematics. ')


engine.say('Hai Swapna')

engine.say('Hai Swapna are you  mad')
voice = engine.getProperty('voice')
print voice

#engine.say('Python supports a concept called "list comprehensions". It can be used to construct lists in a very natural, easy way, like a mathematician is used to do.The following are common ways to describe lists (or sets, or tuples, or vectors) in mathematics. ')

engine.runAndWait()


