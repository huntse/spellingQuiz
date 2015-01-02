# coding: utf-8

import readline
import random
import json
from Speaker import Speaker

class SpellingQuiz(object):
    """Encapsulates a specific spelling quiz"""

    def __init__(self):
        with open("config.json") as config_file:
            config = json.load(config_file)
        self.speechEngine = Speaker()
        self.name = config['name']
        self.words = config['words']
        self.explanations = config['explanations']


    def mainMenu(self):
        """Get a selection from the main menu"""
        categories="\n\t\t".join(self.words.keys())
        print("""
            Hey there %s!  Welcome to spelling quiz.  
            
            I can ask you about: 
            %s.
            
            Would you like to:
                a)Practise words from a category you pick
                b)Practise words from a category I pick
                c)Practise words which I pick from the whole list
                d)go for champion speller
                
        """ % (self.name, categories))
        ans=raw_input("Type a, b, c, or d, or press enter to quit:")
        return ans

    def pickCategory(self, categories):
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

    def testList(self, wordList):
        """Test a specific list of words"""
        totalCount=len(wordList)
        correct=0
        wrong=[]
        msg = "OK %s, type the words after you hear them.  Just press 'enter' to hear the word again." % self.name
        print(msg)
        self.speechEngine.say(msg)
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
                self.speechEngine.say(prompt % word)
                if word in self.explanations:
                    self.speechEngine.say("For example, '%s'." % self.explanations[word])
                ans = raw_input("%d of %d: Type the word you just heard, or press 'enter' to hear it again.  =>" % (idx, totalCount))
                if(ans!=""):
                    gotIt=True
                    if(ans==word):
                        correct = correct + 1
                    else:
                        wrong = wrong + [word]
                
        return (totalCount, correct, wrong)
            
    def assess(self, count, correct, wrong, champion=False):
        if count == correct:
            print("Nice one!  You got %d out of %d" % (correct, count))
            if champion:
                print("""
                
                    -------------------------------------------
                    >>>YOU ARE OFFICIALLY A CHAMPION SPELLER<<<
                    -------------------------------------------
                
                """)
                self.speechEngine.say("Well done! You are a champion speller!")
        else:
            print("You got %d out of %d, and these are the words you got wrong: %s" % (correct, count, wrong))
            

    def runTest(self):
      allWords = reduce(lambda xs, x: xs + x, self.words.values())
      done=False
      while not done:
          ans=self.mainMenu()
          if(ans==""):
              print("OK.  See you again soon!")
              done=True
          else:
              print("\n\n\n")
              category=''
              if ans=='a':
                  category=self.pickCategory(self.words.keys())
                  print("OK.  You picked '%s'." % category)
              if ans=='b':
                  category=random.choice(self.words.keys())
                  print("Thanks for letting me pick!  I chose '%s'." % category)
              if category:
                  selection = self.words[category]
                  random.shuffle(selection)
                  self.assess(*self.testList(selection))
              if ans=='c':
                  selection = random.sample(allWords,len(allWords)/3)
                  self.assess(*self.testList(selection))
              if ans=='d':
                  selection = allWords
                  random.shuffle(selection)
                  self.assess(*self.testList(selection), champion=True)
                
# vim: set sw=4 ts=4 et:
