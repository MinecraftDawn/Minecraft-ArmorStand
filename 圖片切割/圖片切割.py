import cv2 as cv
import os

materials = ('chainmail','gold','iron','leather','netherite','diamond')

# 右左上下前後

helmets = [[8,16,16,24],
          [8,16,0,8],
          [0,8,8,16],
          [0,8,0,8],
          [8,16,8,16],
          [8,16,24,32]]

chestplates =  [[20,32,28,32],
               [20,32,16,20],
               [0,1,0,1],
               [0,1,0,1],
               [20,32,20,28],
               [20,32,32,40]]

leftBoots = [[26,32,4,8],
               [26,32,12,16],
               [0,1,0,1],
               [16,20,8,12],
               [26,32,8,12],
               [26,32,0,4]]

rightBoots = [[26,32,12,16],
               [26,32,4,8],
               [0,1,0,1],
               [16,20,8,12],
               [26,32,0,4],
               [26,32,8,12]]

leftArms =[[20,25,40,44],
          [20,25,48,52],
          [16,20,44,48],
          [0,1,0,1],
          [20,25,52,56],
          [20,25,44,48]]

rightArms =[[20,25,48,52],
          [20,25,40,44],
          [16,20,44,48],
          [0,1,0,1],
          [20,25,44,48],
          [20,25,52,56]]

leftLegs = [[20,29,8,12],
          [20,29,0,4],
          [16,20,8,12],
          [0,1,0,1],
          [20,29,4,8],
          [20,29,12,16]]

rightLegs = [[20,29,0,4],
          [20,29,8,12],
          [16,20,8,12],
          [0,1,0,1],
          [20,29,12,16],
          [20,29,4,8]]

waists =  [[27,32,16,20],
          [27,32,28,32],
          [0,1,0,1],
          [0,1,0,1],
          [27,32,20,28],
          [27,32,32,40]]

armors = {'helmets':helmets,
          'chestplates':chestplates,
          'leftBoots': leftBoots,
          'rightBoots': rightBoots,
          'leftArms': leftArms,
          'rightArms': rightArms,
          'leftLegs': leftLegs,
          'rightLegs': rightLegs}

for material in materials:
     if not os.path.exists(material):
          os.makedirs(material)

for material in materials:
     img = cv.imread(f'{material}_layer_1.png', cv.IMREAD_UNCHANGED)

     for k,v in armors.items():
          name = k[:-1]
          for i in range(len(v)):
               part = v[i]
               skin = img[part[0]:part[1],part[2]:part[3]]
               cv.imwrite(f'{material}/{name}{i}.png', skin)


     img = cv.imread(f'{material}_layer_2.png', cv.IMREAD_UNCHANGED)


     for i in range(len(leftLegs)):
          s = leftLegs[i]
          leftLeg = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'{material}/leftLeg{i}.png', leftLeg)


     for i in range(len(rightLegs)):
          s = rightLegs[i]
          rightLeg = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'{material}/rightLeg{i}.png', rightLeg)


     for i in range(len(waists)):
          s = waists[i]
          waist = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'{material}/waist{i}.png', waist)


     
     '''
     for i in range(len(helmets)):
          s = helmets[i]
          helmet = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'helmet{i}.png', helmet)



     for i in range(len(chestplates)):
          s = chestplates[i]
          chestplate = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'chestplate{i}.png', chestplate)


     for i in range(len(leftBoots)):
          s = leftBoots[i]
          leftBoot = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'leftBoot{i}.png', leftBoot)


     for i in range(len(rightBoots)):
          s = rightBoots[i]
          rightBoot = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'rightBoot{i}.png', rightBoot)


     for i in range(len(leftArms)):
          s = leftArms[i]
          leftArm = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'leftArm{i}.png', leftArm)


     for i in range(len(rightArms)):
          s = rightArms[i]
          rightArm = img[s[0]:s[1],s[2]:s[3]]
          cv.imwrite(f'rightArm{i}.png', rightArm)


     '''     






