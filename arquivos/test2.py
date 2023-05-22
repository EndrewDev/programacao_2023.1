import pickle

file = open('nomeegmail.pkl', 'rb').read()
open = pickle.load(file)

print(open)