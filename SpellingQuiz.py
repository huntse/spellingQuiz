# coding: utf-8

import readline
import random
from Speaker import Speaker

def mainMenu(words):
    """Get a selection from the main menu"""
    categories="\n\t\t".join(words.keys())
    print("""
        Hey there Iris!  Welcome to spelling quiz.  
        
        I can ask you about: 
        %s.
        
        Would you like to:
            a)Practise words from a category you pick
            b)Practise words from a category I pick
            c)Practise words which I pick from the whole list
            d)go for champion speller
            
    """ % categories)
    ans=raw_input("Type a, b, c, or d, or press enter to quit:")
    return ans

def pickCategory(categories):
    """Present a menu of choices for the user to pick a category"""
    idx=0
    choices={}
    print "Type a number to pick a category"
    for cat in categories:
        idx = idx + 1
        choices[idx] = cat
        print "\t%d for %s" % (idx, cat)
    done = False
    while not done:
        ans = raw_input("Type 1 to %d or enter to go back:" % idx)
        if ans != "":
            try:
                selection = choices[int(ans)]
                return selection
            except (ValueError, KeyError):
                pass
        else:
            return ""

def testList(speechEngine, explanations, wordList):
    """Test a specific list of words"""
    totalCount=len(wordList)
    correct=0
    wrong=[]
    msg = "OK Iris, type the words after you hear them.  Just press 'enter' to hear the word again."
    print(msg)
    speechEngine.say(msg)
    idx = 0
    prompts = [
        "Please spell '%s'.",
        "Can you spell '%s'?",
        "I bet you can't spell '%s'!"
    ]
    for word in wordList:
        idx = idx + 1
        gotIt=False
        while not gotIt:
            prompt = random.choice(prompts)
            speechEngine.say(prompt % word)
            if word in explanations:
                speechEngine.say("For example, '%s'." % explanations[word])
            ans = raw_input("%d of %d: Type the word you just heard, or press 'enter' to hear it again.  =>" % (idx, totalCount))
            if(ans!=""):
                gotIt=True
                if(ans==word):
                    correct = correct + 1
                else:
                    wrong = wrong + [word]
            
    return (totalCount, correct, wrong)
        
def assess(speechEngine, count, correct, wrong, champion=False):
    if count == correct:
        print("Nice one!  You got %d out of %d" % (correct, count))
        if champion:
            print("""
            
                -------------------------------------------
                >>>YOU ARE OFFICIALLY A CHAMPION SPELLER<<<
                -------------------------------------------
            
            """)
            speechEngine.say("Well done! You are a champion speller!")
    else:
        print("You got %d out of %d, and these are the words you got wrong: %s" % (correct, count, wrong))
        

def runTest():
  words = {
        '-ly': [ 'bravely', 'loudly', 'proudly', 'slightly', 'suddenly', 'wisely', 'boastfully', 'carefully', 'faithfully', 'gratefully', 'hopefully', 'spitefully', 'usefully', 'usually', 'fearlessly', 'accidentally', 'occasionally', 'probably', 'gently', 'smiley' ],
        'Double Consonant': [ 'accomodate', 'accompany', 'aggressive', 'appreciate', 'attached', 'committee', 'communicate', 'correspond', 'embarrass', 'exaggerate', 'necessary', 'opportunity', 'recommend', 'sufficient', 'suggest', 'written', 'swallow', 'sudden', 'kettle' ],
        'wh': [ 'which', 'whisper', 'whether', 'whirling', 'whinged', 'whirred', 'wheezing', 'wherever', 'whinny', 'whose', 'whoever', 'anywhere', 'elsewhere', 'everywhere', 'somewhere', 'meanwhile', 'worthwhile', 'overwhelming', 'whimsical', 'whetted', 'wholeheartedly' ],
        'Silent w': [ 'wrapper', 'wrangle', 'wrath', 'wreckage', 'wren', 'wrestle', 'wretched', 'wriggle', 'wrinkle', 'wrist', 'wrong', 'wrought', 'write', 'wry', 'whole', 'answer', 'sword', 'wreath', 'writhe', 'awry' ],
        'homophones': [ 'right', 'write', 'hair', 'hare', 'weigh', 'way', 'night', 'knight', 'waste', 'waist', 'break', 'brake', 'blue', 'blew' ],
        'high frequency': ['with']
  }
  explanations = {
      'whether':    "She didn't know whether to laugh or cry.",
      'which':      "I would go out tonight, but I can't decide which dress to wear.",
      'whinny':     'They heard the horses whinny as they came closer to the field.',
      'whirred':    'The strange machine whirred quietly as it was turned on.',
      'whole':      "He hadn't yet told them the whole story.",
      'whose':      '"Whose smelly socks are these?" asked the teacher in disgust.',
      'wrapper':    'The boy licked his lips greedily as he took out the chocolate bar and tore open the wrapper.',
      'right':      "He wanted to tell them, but couldn't think of the right way",
      'hair':       "The worst thing about the weekend was when she had to wash her hair",
      'weigh':      "'How on earth are we going to weigh an angry hippopotamus?' he asked, scratching his head",
      'way':        '"Do you know the way to Chiswick?" she asked',
      'night':      'The howling wind kept them up all night.',
      'knight':     'The knight put on his armour, then rode into battle.',
      'waste':      'The entire cake was ruined!  It was all such a waste.',
      'break':      '"Stop! You will break it!" shouted the angry mother.',
      'brake':      'He pulled up the brake and they screeched to a halt.',
      'blue':       "I've got a blue hotel room, with a blue bedspread.",
      'blew':       "She lifted the magical instrument to her lips, and blew.",
      'write':      'She opened her diary, and began to write',
      'wry':        'A wry smile spread across her lips and she began to tell her story',

  }
  allWords = reduce(lambda xs, x: xs + x, words.values())
  speechEngine = Speaker()
  done=False
  while not done:
      ans=mainMenu(words)
      if(ans==""):
          print("OK.  See you again soon!")
          done=True
      else:
          print("\n\n\n")
          category=''
          if ans=='a':
              category=pickCategory(words.keys())
              print("OK.  You picked '%s'." % category)
          if ans=='b':
              category=random.choice(words.keys())
              print("Thanks for letting me pick!  I chose '%s'." % category)
          if category:
              selection = words[category]
              random.shuffle(selection)
              assess(speechEngine, *testList(speechEngine, explanations, selection))
          if ans=='c':
              selection = random.sample(allWords,len(allWords)/3)
              assess(speechEngine, *testList(speechEngine, explanations, selection))
          if ans=='d':
              selection = allWords
              random.shuffle(selection)
              assess(speechEngine, *testList(speechEngine, explanations, selection), champion=True)
            
# vim: set sw=4 ts=4 et:
