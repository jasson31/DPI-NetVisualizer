import h5py

filename = "99.h5"

h5 = h5py.File(filename,'r')

pos = h5['positions']
print(pos)
for i in range(int(pos.shape[0])):
    print(pos[i])

h5.close()