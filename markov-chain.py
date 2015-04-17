import sys
from sys import argv
from random import choice
import string

class SimpleMarkovGenerator(object):
    character_limit = float('inf')

    def read_files(self, text_filename):
        """Given a list of files, make chains from them."""

        opened_text_filename = open(text_filename)
        read_text_filename = opened_text_filename.read()

        return read_text_filename

    def make_chains(self, read_text_filename):
        """Takes input text as string; returns dictionary of markov chains."""

        word_list = read_text_filename.split()

        markov_dict = {}

        # for index, item in enumerate(word_list):
        for index in range(len(word_list) - 2):
            key = (word_list[index], word_list[index + 1])
            value = word_list[index + 2]

            if key not in markov_dict:
                markov_dict[key] = []
            markov_dict[key].append(value)
            
        chains = markov_dict
  
        return chains


    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""
        
        #start chain only with capital words
        for key in chains:
            key = choice(chains.keys())
            if key[0][0] in string.ascii_uppercase:
                break

        markov_str = key[0] + " " + key[1]

        while key in chains:
            key_value = choice(chains[key])
            add_charc = len(markov_str + " " + key_value)
            if add_charc >= self.character_limit:
                break
            else:
                markov_str = markov_str + " " + key_value
                key = (key[1], key_value,)
        print add_charc
        print len(markov_str)
        return markov_str

class TweetableMarkovGenerator(SimpleMarkovGenerator):
    character_limit = 140


if __name__ == "__main__":

    script, text_filename = argv

    #SimpleMarkovGenerator()
    instance = SimpleMarkovGenerator()
     # Get a Markov chain
    chain_dict = instance.make_chains(instance.read_files(text_filename))
    # # # Produce random text
    random_text = instance.make_text(chain_dict)
    print "SimpleMarkov: ", random_text

    #TweetableMarkovGenerator()
    instant_tweet = TweetableMarkovGenerator()
    tweet_dict = instant_tweet.make_chains(instant_tweet.read_files(text_filename))
    random_tweet = instant_tweet.make_text(tweet_dict)
    print "TweetableMarkov: ", random_tweet  


    
        
            
        
    # """
    # for statement looks through out txt file using the dict keys as unique identifiers
    # every time the for loop finds a matching pair, the loop will take the next word (the third word) 
    # append the list associated with that uniue key

    # check: print dict
    # """


        # for index, item in enumerate(word_list):

        #     if index == (len(word_list) - 2):
        #         print "I'm at the end"
        #         break
        #     else: 
        #         print "I am not at the end yet."
        #         # key_value = (item[index -2 ]) #item[index + 1])




    # # Change this to read input_text from a file, deciding which file should
    # # be used by examining the `sys.argv` arguments (if neccessary, see the
    # # Python docs for sys.argv)

    # # input_text = "green-eggs.txt"


