import pickle
file = open('nomeegmail.pkl', 'rb')
abrir = pickle.load(file)
print(abrir)