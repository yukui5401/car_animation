# Brooke Yang - Assig #7 - Pygame - Animate a Truck
# Input:        N/A.
# Processing:   N/A.
# Output:       Animate a truck in 2 dimensions.


# Declaration Section
import pygame, math, time
from pygame import KEYDOWN, K_ESCAPE


# Step 1: Setup Game
pygame.init()
window = pygame.display.set_mode([1200, 800])
pygame.display.set_caption("Pygame - Draw a Truck")
skyBlue = (0, 191, 255)
yellow = (255, 215, 0)
blue = (142, 229, 238)
truckClr = (238, 59, 59)
white = (238,238,224)
lightWhite = (248, 248, 255)
greyWhite = (201, 201, 201)
lightGrey = (171, 171, 171)
grey = (128, 128, 128)
blueGrey = (122, 139, 139)
darkGrey = (131, 139, 139)
lightRed = (255, 64, 64)
red = (205, 55, 0)
darkRed = (139, 26, 26)
orange = (255, 128, 0)
green = (0, 139, 69)
brown = (139, 121, 94)
lightBrown = (205, 170, 125)
darkBlue = (74, 112, 139)
black = (54, 54, 54)
lightBlack = (64, 64, 64)
darkBlack = (40, 40, 40)
move = -350
lap = 1


# Step 2: Poll for Events
while True:
   delay = 0.001
   event = pygame.event.poll()
   if event.type == pygame.QUIT:
       break
   elif event.type == KEYDOWN and event.key == K_ESCAPE:
       break


   # Step 3: Update Game
   if move < 1550:
       move += 2
   elif move >= 1550 and lap < 4:
       lap += 1
       move = -350
       delay = 1
       if lap == 2:
           truckClr = (162, 205, 90)
       elif lap == 3:
           truckClr = (0, 104, 139)
       else:
           truckClr = (247, 247, 247)
   else:
       break
   sun = [(1050, 150), (930, 170), (1150, 140), (970, 228), (1120, 88), (960, 100), (1120, 200), (1030, 70), (1065, 233)]
   houseFrame = [(692, 729), (692, 550), (850, 420), (1008, 550), (1008, 729)]
   houseSurface = [(706, 729), (706, 556), (850, 433), (994, 556), (994, 729)]
   chimney = (920, 450, 35, 269)
   chimneyTop = (916, 438, 43, 14)
   chimneyDesign = [(920, 452, 35, 2), (936, 460, 18, 5), (920, 472, 9, 5), (920, 482, 25, 5)]
   houseRoof = [(680, 564), (850, 420), (1020, 564), (850, 420)]
   houseDesign = [[706, 700], [994, 700], [724, 544], [978, 544]]
   houseFloor = [(692, 708, 317, 22), (692, 725, 317, 5)]
   houseStair = [(752, 708, 98, 22), (740, 719, 120, 11)]
   houseDoor = (765, 566, 72, 142)
   doorDesign = [(775, 575, 20, 50), (775, 650, 20, 50), (806, 575, 20, 50), (806, 650, 20, 50), (775, 630, 51, 15)]
   doorknob = (832, 638)
   rectWindow = (880, 568, 65, 110)
   windowDesign = [(887, 576, 24, 45), (887, 625, 24, 45), (915, 576, 24, 45), (915, 625, 24, 45)]
   circleWindow = (850, 503)
   truckFrame = [(50 + move, 590), (300 + move, 590), (320 + move, 655), (347 + move, 665), (347 + move, 710), (50 + move, 710)]
   tireCentre = [(130 + move, 710), (310 + move, 710)]
   designLine1 = [(60 + move, 700), (101 + move, 700), (160 + move, 700), (236 + move, 700)]  # lower lines
   designLine2 = [(60 + move, 670), (236 + move, 670)]  # upper line
   designLine3 = [(53 + move, 590), (53 + move, 710)]  # rear of truck
   roof = (50 + move, 586, 254, 9)
   doorFrame = [(240 + move, 615), (290 + move, 615), (290 + move, 682), (275 + move, 708), (240 + move, 708)]
   wheelWell = [(105 + move, 685, 50, 50), (285 + move, 685, 50, 50)]  # rectangles for drawing arcs
   leftWheelHole = [(130 + move, 702), (130 + move, 718), (124 + move, 705), (124 + move, 715), (136 + move, 705), (136 + move, 715)]
   rightWheelHole = [(310 + move, 702), (310 + move, 718), (304 + move, 705), (304 + move, 715), (316 + move, 705), (316 + move, 715)]
   leftScreen = [(242 + move, 617, 47, 41), (247 + move, 620, 38, 32)]  # shade/frame and blue transparency
   rightScreen = [(292 + move, 617), (305 + move, 617), (317 + move, 655), (292 + move, 655)]  # frame/blue transparency
   leftScreenDoor = [(268 + move, 619), (268 + move, 654)]
   rightScreenShade = [(297 + move, 617), (305 + move, 655), (292 + move, 651, 25, 4)]  # shade
   bumper = (335 + move, 700, 15, 11)
   designBumper = [(335 + move, 703), (348 + move, 703)]
   lights = [(58 + move, 600, 8, 3), (292 + move, 600, 8, 3), (331 + move, 673, 8, 3)]
   handle = (282 + move, 662, 5, 10)
   mirrorStand = [(303 + move, 615), (303 + move, 660), (299 + move, 627), (303 + move, 627), (299 + move, 638), (303 + move, 638)]
   mirror = (297 + move, 624, 3, 17)
   font = pygame.font.SysFont("Times New Roman", 37, True, 1)
   text = font.render("Delivery!", True, black)


   # Step 4: Draw Surface
   window.fill(skyBlue)  # sky
   pygame.draw.rect(window, darkBlack, ((0, 730), (1200, 70)), 0)  # road
   pygame.draw.circle(window, yellow, sun[0], 40, 0)
   for rays in range(1, 9, 2):
       pygame.draw.line(window, yellow, sun[rays], sun[rays + 1], 3)
   pygame.draw.rect(window, lightBrown, chimney, 0)
   pygame.draw.rect(window, lightBrown, chimneyTop, 0, 5)
   for design in chimneyDesign:
       pygame.draw.rect(window, brown, design, 0, 5)
   pygame.draw.polygon(window, greyWhite, houseFrame, 0)
   pygame.draw.polygon(window, white, houseSurface, 0)
   pygame.draw.line(window, red, houseRoof[0], houseRoof[1], 14)
   pygame.draw.line(window, red, houseRoof[2], houseRoof[3], 14)
   for line in range(0,7):
       pygame.draw.line(window, lightGrey, houseDesign[0], houseDesign[1], 3)
       houseDesign[0][1] -= 22
       houseDesign[1][1] -= 22
   for design in range(0,6):
       pygame.draw.line(window, lightGrey, houseDesign[2], houseDesign[3], 3)
       houseDesign[2][1] -= 18
       houseDesign[3][1] -= 18
       houseDesign[2][0] += 21
       houseDesign[3][0] -= 21
   pygame.draw.rect(window, grey, houseFloor[0], 0)
   pygame.draw.rect(window, lightBlack, houseFloor[1], 0)
   pygame.draw.rect(window, greyWhite, houseStair[0], 0)
   pygame.draw.rect(window, greyWhite, houseStair[1], 0)
   pygame.draw.rect(window, lightRed, houseDoor, 0)
   for index in doorDesign:
       pygame.draw.rect(window, darkRed, index, 1)
   pygame.draw.circle(window, white, doorknob, 2, 0)
   pygame.draw.rect(window, lightWhite, rectWindow, 0)
   for rect in windowDesign:
       pygame.draw.rect(window, blue, rect, 0)
   pygame.draw.circle(window, lightWhite, circleWindow, 22, 0)
   pygame.draw.circle(window, blue, circleWindow, 17, 0)
   pygame.draw.polygon(window, truckClr, truckFrame, 0)  # truck shape
   pygame.draw.polygon(window, lightGrey, doorFrame, 1)  # door frame
   pygame.draw.line(window, greyWhite, designLine1[0], designLine1[1], 4)  # design line
   pygame.draw.line(window, greyWhite, designLine1[2], designLine1[3], 4)
   pygame.draw.line(window, greyWhite, designLine2[0], designLine2[1], 4)
   pygame.draw.line(window, lightGrey, designLine3[0], designLine3[1], 1)
   pygame.draw.rect(window, greyWhite, roof, 0, 2)  # truck roof
   pygame.draw.arc(window, black, wheelWell[0], math.radians(0), math.radians(180), 7)  # left wheel well
   pygame.draw.arc(window, black, wheelWell[1], math.radians(0), math.radians(180), 7)  # right wheel well
   for count in range(0, 2):
       pygame.draw.circle(window, lightBlack, tireCentre[count], 20, 0)  # tire
       pygame.draw.circle(window, grey, tireCentre[count], 12, 0)  # wheel hub
       pygame.draw.circle(window, greyWhite, tireCentre[count], 4, 0)  # inner hub
   for count in range(0, 6):
       pygame.draw.circle(window, black, leftWheelHole[count], 1, 0)  # left wheel holes
       pygame.draw.circle(window, black, rightWheelHole[count], 1, 0)  # right wheel holes
   pygame.draw.rect(window, black, leftScreen[0], 0, 5)  # left window shade
   pygame.draw.rect(window, darkBlue, leftScreen[1], 0, 5)  # left window transparency
   pygame.draw.rect(window, blueGrey, leftScreen[0], 2, 5)  # left window frame
   pygame.draw.line(window, lightBlack, leftScreenDoor[0], leftScreenDoor[1], 2)  # left window door
   pygame.draw.polygon(window, darkBlue, rightScreen, 0)  # right window transparency
   pygame.draw.line(window, black, rightScreenShade[0], rightScreenShade[1], 2)  # right window shade
   pygame.draw.rect(window, black, rightScreenShade[2], 0)  # right window shade
   pygame.draw.polygon(window, blueGrey, rightScreen, 2)  # right window frame
   pygame.draw.line(window, black, mirrorStand[0], mirrorStand[1], 1)  # mirror stand
   pygame.draw.circle(window, black, mirrorStand[0], 1.5, 0)  # mirror stand top
   pygame.draw.circle(window, black, mirrorStand[1], 1.5, 0)  # mirror stand bottom
   pygame.draw.rect(window, greyWhite, mirror, 0, 1)  # mirror
   pygame.draw.line(window, darkBlack, mirrorStand[2], mirrorStand[3], 1)  # top mirror arm
   pygame.draw.line(window, darkBlack, mirrorStand[4], mirrorStand[5], 1)  # bottom mirror arm
   pygame.draw.rect(window, darkGrey, bumper, 0, 2, 0, 3)  # bumper
   pygame.draw.line(window, lightBlack, designBumper[0], designBumper[1], 1)  # bumper color
   pygame.draw.rect(window, lightBlack, handle, 0, 2)  # door handle
   for count in range(0, 3):
       pygame.draw.rect(window, orange, lights[count], 0)  # lights
   window.blit(text, ([80 + move, 615]))  # text


   # Step 5: Display Surface
   pygame.display.update()
   time.sleep(delay)
pygame.quit()
quit()


