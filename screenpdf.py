from PIL import Image
import os.path,time
import datetime
import re
from PIL import Image

img1 = Image.open('Untitled.png').convert('RGB')


t = os.listdir('/home/erin/Pictures/')

tdy = datetime.date.today()

print("Input\n1 for DM \n2 for CS\n3 for MoPs\n4 for HT\n5 for TE\n6 for MS")
period = int(input())

regrex = re.compile('^Screenshot from '+str(tdy)+'(.){9}\.png$')

l = list(filter(regrex.match, t))
l.sort()

img_list = []

for i in l:
    im = Image.open('/home/erin/Pictures/'+i).convert("RGB")
    img_list.append(im)

if period ==1:
    img1.save('/home/erin/MEGAsync/Fifth Sem/Dynamics Of Machines/SS/'+str(tdy)+'.pdf',
              save_all=True, append_images=img_list)
elif period ==2:
    img1.save('/home/erin/MEGAsync/Fifth Sem/Control System Eng/SS/'+str(tdy)+'.pdf',
              save_all=True, append_images=img_list)
elif period ==3:
    img1.save('/home/erin/MEGAsync/Fifth Sem/Management Of Production System/SS/'+str(tdy)+'.pdf',
              save_all=True, append_images=img_list)
elif period == 4:
    img1.save('/home/erin/MEGAsync/Fifth Sem/Principle of Heat Transfer/SS/'+str(tdy)+'.pdf',
              save_all=True, append_images=img_list)
elif period == 5:
    img1.save('/home/erin/MEGAsync/Fifth Sem/Thermal Eng I/SS/'+str(tdy)+'.pdf',
              save_all=True, append_images=img_list)
elif period == 6:
    img1.save('/home/erin/MEGAsync/Fifth Sem/Manufacturing Science/SS/'+str(tdy)+'.pdf',
              save_all=True, append_images=img_list)

for i in l:
    os.unlink("/home/erin/Pictures/"+str(i))

