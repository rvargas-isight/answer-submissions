from PythonClub.PythonClub import PythonClub

import base64
class challenge_one(PythonClub):
    '''
    Example challenge: I am Jack's base64 encoded string: "c2Zhb3psenJ0YmRxcmp2cW95c3Z2dXBweHNlY2hhcHo=" -> sfaozlzrtbdqrjvqoysvvuppxsechapz
    '''
    def __init__ (self, ):
        PythonClub.__init__(self, 1)
    
    def solution(self):
        return base64.b64decode(self.getChallenge()[36:-1])
        #verbose solution
        '''
        #get the string representation of the challenge
        challenge = self.getChallenge()
        #we only need character 36 to one minus the last character to decode the base64 string
        _slice = challenge[36:-1]
        #return the answer
        return base64.b64decode(_slice)
        '''

class challenge_two(PythonClub):
    '''
    I am Jack's unsolved equation: "one plus six plus ten equals ?"
    '''
    def __init__ (self):
        PythonClub.__init__(self, 2)
        self.num_words= '''Zero
One
Two
Three
Four
Five
Six
Seven
Eight
Nine
Ten
Eleven
Twelve
Thirteen
Fourteen
Fifteen
Sixteen
Seventeen
Eighteen
Nineteen
Twenty
Twenty-one
Twenty-two
Twenty-three
Twenty-four
Twenty-five
Twenty-six
Twenty-seven
Twenty-eight
Twenty-nine
Thirty
Thirty-one'''
        self.operators = ['plus', 'minus']
        self.total = 0
        self.token = 'plus'
        
    def textMath(self, li):
        num2words = {}
        words2num={}
        ls = self.num_words.split()
        for i in range(len(ls)):
            #print ls[i]
            num2words[i]=ls[i].lower()
            words2num[ls[i].lower()]=i

        for i in range(len(li)):
            #even indcies are integers
            if i % 2 == 0:
                if self.token == 'plus':
                    self.total += words2num[li[i]]
                else:
                    self.total -= words2num[li[i]]
            #odd indicies are the operators
            else:
                self.token = li[i] 
        #print self.total
        return num2words[self.total]
        
    def solution(self):
        return self.textMath(self.getChallenge()[32:-10].split())
        #verbose solution 
        '''
        challenge = self.getChallenge()
        #print challenge
        ls = challenge[32:-10]
        print ls
        result=  self.textMath(ls.split())
        #print result 
        return result
        '''
        
import re
import requests
import json
import base64
class challenge_three(PythonClub):
    '''
    Example: I am Jack's desired password for: "Jonathan" -> GREATpirate4
    '''
    def __init__ (self, ):
        PythonClub.__init__(self, 3)
    
    def solution(self):
        text = self.getChallenge()
        user=re.search(r':\s+"(\w+)"', text).group(1)
        users = "http://thepythonclub.org/tmp/"+re.search(r'(user\w+.json)', text).group(1)
        users = json.loads(requests.get(users).text)
        uid = None
        for uuid in users:
            if users[uuid]['Name']== user:
                uid= uuid
                continue
        pwd  = "http://thepythonclub.org/tmp/"+re.search(r'(pass\w+.json)', text).group(1)
        pwds = json.loads(requests.get(pwd).text)
        return base64.b64decode(pwds[uid])

if __name__ == "__main__":
    print challenge_one().submit()
    print challenge_two().submit()
    print challenge_three().submit()