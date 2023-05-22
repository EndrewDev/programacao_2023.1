import pickle

file = open('nomeegmail.pkl', 'rb')
open = pickle.load(file)

print(open)