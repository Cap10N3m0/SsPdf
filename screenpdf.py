from PIL import Image
import os.path,time
import datetime
import re
from PIL import Image

img1 = Image.open('Untitled.png').convert('RGB') #First Page of pdf


t = os.listdir('Location of Pictures Directory') #Directory where ss is saved

tdy = datetime.date.today()

print("Input\n1 for DM \n2 for CS\n3 for MoPs\n4 for HT\n5 for TE\n6 for MS")
period = int(input())

regrex = re.compile('^Screenshot from '+str(tdy)+'(.){9}\.png$')

l = list(filter(regrex.match, t))
l.sort()

img_list = []

for i in l:
    im = Image.open('Location of Pictures Directory/'+i).convert("RGB") #Change Here
    img_list.append(im)

if period ==1:
    img1.save('Location of 1st course/SS/'+str(tdy)+'.pdf', #Here
              save_all=True, append_images=img_list)
elif period ==2:
    img1.save('Location of 2nd course/SS/'+str(tdy)+'.pdf', #Here 
              save_all=True, append_images=img_list)
elif period ==3:
    img1.save('Location of 3rd course/SS/'+str(tdy)+'.pdf', #Here
              save_all=True, append_images=img_list)
elif period == 4:
    img1.save('Location of 4th course/SS/'+str(tdy)+'.pdf', #Here
              save_all=True, append_images=img_list)
elif period == 5:
    img1.save('Location of 5th course/SS/'+str(tdy)+'.pdf', #Here
              save_all=True, append_images=img_list)
elif period == 6:
    img1.save('Location of 6th course/SS/'+str(tdy)+'.pdf', #Here
              save_all=True, append_images=img_list)

for i in l:
    os.unlink("Location of Pictures Directory/"+str(i)) #Here

