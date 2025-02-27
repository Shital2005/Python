import pickle 
f=open('binary.dat','wb')
pickle.dump = (1.1,f)
pickle.dump = (2.2,f)
f.close()