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

for i in range(len(chestplates)):
     s = chestplates[i]
     chestplate = img[s[0]:s[1],s[2]:s[3]]
     cv.imwrite(f'chestplate{i}.png', chestplate)


leftLegs = [[26,32,4,8],
            [26,32,12,16],
            [0,1,0,1],
            [16,20,8,12],
            [26,32,8,12],
            [26,32,0,4]]

for i in range(len(leftLegs)):
     s = leftLegs[i]
     leftLeg = img[s[0]:s[1],s[2]:s[3]]
     cv.imwrite(f'leftLeg{i}.png', leftLeg)


rightLegs = [[26,32,12,16],
             [26,32,4,8],
             [0,1,0,1],
             [16,20,8,12],
             [26,32,0,4],
             [26,32,8,12]]

for i in range(len(rightLegs)):
     s = rightLegs[i]
     rightLeg = img[s[0]:s[1],s[2]:s[3]]
     cv.imwrite(f'rightLeg{i}.png', rightLeg)
