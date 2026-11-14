#!/usr/bin/env python3
# Bedenine Yolculuk YouTube kanal kapağı (2560x1440). Kullanım: python3 araclar/kanal_kapagi.py <kareler_klasoru> <cikti_klasoru>
# Kareler: pool_face.png, pool_dog.png, med_face.png (videolardan ffmpeg ile alınır).
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
S,OUT=sys.argv[1],sys.argv[2]; W,H=2560,1440
FD='/usr/share/fonts/opentype/inter/'
def F(n,s): return ImageFont.truetype(FD+n,s)
SAGE=(138,154,123); DARK=(47,58,47); CREAM=(245,239,230); TERRA=(196,106,74); SAND=(226,214,196)
# safe area (all devices)
SX0,SY0=(W-1546)//2,(H-423)//2; SX1,SY1=SX0+1546,SY0+423
def img(n): return ImageEnhance.Color(Image.open(f'{S}/{n}.png').convert('RGB')).enhance(1.05)

# background: wide blurred pool scene + cream wash
pool=img('pool_dog')
bg=pool.crop((0,0,1080,1300)).resize((W,int(1300*W/1080)),Image.LANCZOS).crop((0,0,W,H)).filter(ImageFilter.GaussianBlur(28)).convert('RGBA')
wash=Image.new('RGBA',(W,H),CREAM+(0,)); wd=ImageDraw.Draw(wash)
for x in range(W):  # cream stronger on left (text side)
    a=int(235-120*max(0,(x-900)/(W-900)))
    wd.line([(x,0),(x,H)],fill=CREAM+(a,))
bg.alpha_composite(wash)
# soft decorative circles
deco=Image.new('RGBA',(W,H),(0,0,0,0)); dd=ImageDraw.Draw(deco)
dd.ellipse([SX0-420,SY0-260,SX0+120,SY0+280],fill=SAGE+(70,))
dd.ellipse([SX0+250,SY1-60,SX0+560,SY1+250],fill=TERRA+(45,))
dd.ellipse([SX1-60,SY0-380,SX1+420,SY0+100],fill=SAGE+(55,))
bg.alpha_composite(deco.filter(ImageFilter.GaussianBlur(30)))
d=ImageDraw.Draw(bg)

# --- text block (left part of safe area) ---
tx=SX0+40
d.text((tx,SY0+40),'Ben Aslı  ·  Her gün yeni Shorts',font=F('Inter-Bold.otf',36),fill=TERRA)
title=F('InterDisplay-Black.otf',118)
d.text((tx-4,SY0+88),'Bedenine',font=title,fill=DARK)
d.text((tx-4,SY0+208),'Yolculuk',font=title,fill=SAGE)
d.text((tx,SY0+348),'Mükemmel değil, sürdürülebilir.',font=F('Inter-SemiBold.otf',36),fill=DARK)

# --- photo cards (right part of safe area) ---
def card(im,box,size,radius=36,border=8):
    c=im.crop(box).resize(size,Image.LANCZOS)
    m=Image.new('L',size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,size[0]-1,size[1]-1],radius=radius,fill=255)
    fr=Image.new('RGBA',(size[0]+2*border,size[1]+2*border),(0,0,0,0))
    ImageDraw.Draw(fr).rounded_rectangle([0,0,fr.size[0]-1,fr.size[1]-1],radius=radius+border,fill=(255,255,255,255))
    fr.paste(c,(border,border),m); return fr
def place(fr,xy,label=None):
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([xy[0]+10,xy[1]+18,xy[0]+fr.size[0]+10,xy[1]+fr.size[1]+18],radius=44,fill=(0,0,0,80))
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18))); bg.alpha_composite(fr,xy)
    if label:
        f=F('Inter-Bold.otf',26); dd=ImageDraw.Draw(bg); b=dd.textbbox((0,0),label,font=f); w=b[2]-b[0]
        x=xy[0]+(fr.size[0]-w)//2-18; y=xy[1]+fr.size[1]-62
        dd.rounded_rectangle([x,y,x+w+36,y+44],radius=22,fill=CREAM+(240,)); dd.text((x+18-b[0],y+9-b[1]),label,font=f,fill=DARK)
cw,ch=250,360
y0=SY0+(423-ch-16)//2
xs=[SX1-3*(cw+16)-3*22, SX1-2*(cw+16)-2*22, SX1-(cw+16)-22]
place(card(img('pool_dog'),(0,365,1080,1920),(cw,ch)),(xs[0],y0),'Esneme')
place(card(img('pool_face'),(60,280,1000,1633),(cw,ch)),(xs[1],y0-0),None)
place(card(img('med_face'),(80,60,1000,1385),(cw,ch)),(xs[2],y0),'Nefes')

out=bg.convert('RGB'); out.save(f'{OUT}/bedenine-yolculuk-kanal-kapagi-2560x1440.jpg',quality=92)

# --- previews: TV(full), desktop(2560x423), mobile(1546x423) + guide overlay ---
g=bg.copy(); gd=ImageDraw.Draw(g)
gd.rectangle([0,SY0,W,SY1],outline=(255,0,0),width=6)
gd.rectangle([SX0,SY0,SX1,SY1],outline=(0,120,255),width=6)
g.convert('RGB').resize((1280,720)).save(f'{S}/guide.jpg')
out.crop((0,SY0,W,SY1)).resize((1280,212)).save(f'{S}/desktop.jpg')
out.crop((SX0,SY0,SX1,SY1)).save(f'{S}/mobile.jpg')
