import cv2 as cv
img = cv.imread('diamond_layer_1.png', cv.IMREAD_UNCHANGED)

# 右左上下前後

helmets = [[8,16,16,24],
           [8,16,0,8],
           [0,8,8,16],
           [0,8,0,8],
           [8,16,8,16],
           [8,16,24,32]]

for i in range(len(helmets)):
     s = helmets[i]
     helmet = img[s[0]:s[1],s[2]:s[3]]
     cv.imwrite(f'helmet{i}.png', helmet)

chestplates =  [[20,32,28,32],
                [20,32,16,20],
                [0,1,0,1],
                [0,1,0,1],
                [20,32,20,28],
                [20,32,32,40]]

for i in range(len(helmets)):
     s = helmets[i]
     helmet = img[s[0]:s[1],s[2]:s[3]]
     cv.imwrite(f'chestplates{i}.png', helmet)
