import matplotlib.pyplot as plt

file_pth = "./data/3.png"
img = plt.imread(file_pth)
target = (0.5019608, 0, 0, 1)
width = img.shape[1]
height = img.shape[0]
x = []
y = []

for i in range(height):
   for j in range(width): 
       if abs(img[i, j, 0]-target[0])<0.01 and abs(img[i, j, 1]-target[1])<0.01 and abs(img[i, j, 2]-target[2])<0.01 and img[i,j,3] == target[3]:
           x.append(i)
           y.append(j)
            
l = len(x)
plt.subplot(121)
plt.imshow(img)

for i in range(l-1):
    if i != l-1 and x[i] == x[i+1]:
        continue
    for j in range(y[i], width):
        img[x[i], j, 0] = 0
        img[x[i], j, 1] = 0
        img[x[i], j, 2] = 0
         
plt.subplot(122)
plt.imshow(img)
plt.show()
