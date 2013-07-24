import requests
import json
class PythonClub(object):
    '''
    base class to get and post answers to the Python club
    '''
    def __init__(self, challenge_number):
        '''
        populate the knowns and instaciate the class
        usage: pc= PythonClub(int)
        '''
        self.challenge_number = challenge_number
        self.url = 'http://thepythonclub.org:808%s/'%self.challenge_number
        self.answer = None
        
    def challenge_url(self):
        return self.url+'challenge'+ str(self.challenge_number)
    
    def getChallenge(self):
        '''
        returns the string representation of the challenge question 
        usage: 
        '''
        #challenge_url = self.url+'challenge'+ challenge_number
        return requests.get(self.challenge_url()).text
    
    def solution(self):
        '''
        override the solution for the python challenge here... must return the answer for the challenge
        '''
        pass
    
    def submit(self):
        ''' 
        this will submit an answer to PythonClub once a solution is known 
        '''
        answer = {'answer': self.solution() }
        return requests.post(self.challenge_url(), data=json.dumps(answer)).text