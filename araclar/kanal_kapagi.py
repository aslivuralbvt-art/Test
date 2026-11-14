#!/usr/bin/env python3
# Bedenine Yolculuk YouTube kanal kapağı, doğa teması (2560x1440).
# Kullanım: python3 araclar/kanal_kapagi.py <kareler_klasoru> A B C
# Gerekenler (klasörde): ai_pool.png (bahçe arka planı), cut_real.png / cut_ai_pool.png (MediaPipe selfie_multiclass ile arka planı ayrılmış kişi).
import sys, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
S=sys.argv[1]; W,H=2560,1440
FD='/usr/share/fonts/opentype/inter/'
def F(n,s): return ImageFont.truetype(FD+n,s)
SAGE=(138,154,123); DARK=(38,52,38); CREAM=(247,242,232); TERRA=(196,106,74)
SX0,SY0=(W-1546)//2,(H-423)//2; SX1,SY1=SX0+1546,SY0+423

def nature_bg():
    pool=Image.open(f'{S}/ai_pool.png').convert('RGB')
    trees=pool.crop((0,0,1080,400))                      # garden / trees area
    bg=trees.resize((W,int(400*W/1080)),Image.LANCZOS)
    bg=bg.resize((W,H),Image.LANCZOS).filter(ImageFilter.GaussianBlur(34))
    bg=ImageEnhance.Color(bg).enhance(1.25); bg=ImageEnhance.Brightness(bg).enhance(1.05)
    bg=bg.convert('RGBA')
    # warm sunlight glow top-left
    glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    gd.ellipse([-500,-700,1500,700],fill=(255,240,200,120))
    bg.alpha_composite(glow.filter(ImageFilter.GaussianBlur(200)))
    # bokeh dots
    rnd=random.Random(3); bk=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(bk)
    for _ in range(70):
        x,y=rnd.randrange(W),rnd.randrange(H); r=rnd.randrange(14,60)
        bd.ellipse([x-r,y-r,x+r,y+r],fill=(255,250,225,rnd.randrange(25,70)))
    bg.alpha_composite(bk.filter(ImageFilter.GaussianBlur(6)))
    return bg

def leaf(d,cx,cy,length,width,ang,col):
    pts=[]
    for i in range(41):
        t=i/40; x=t*length; y=math.sin(math.pi*t)*width/2*(1-0.2*t)
        pts.append((x,y))
    pts+= [(x,-y) for x,y in reversed(pts)]
    ca,sa=math.cos(ang),math.sin(ang)
    d.polygon([(cx+x*ca-y*sa, cy+x*sa+y*ca) for x,y in pts],fill=col)
    d.line([(cx,cy),(cx+length*0.9*ca,cy+length*0.9*sa)],fill=tuple(max(0,c-35) for c in col[:3])+(col[3],),width=max(2,int(width/14)))

def branch(layer,x0,y0,ang,length,kind,seed,scale=1.0):
    rnd=random.Random(seed); d=ImageDraw.Draw(layer)
    pts=[]; x,y,a=x0,y0,ang
    for i in range(60):
        pts.append((x,y)); a+=rnd.uniform(-0.012,0.018); x+=math.cos(a)*length/60; y+=math.sin(a)*length/60
    d.line(pts,fill=(92,104,78,255),width=int(7*scale),joint='curve')
    greens=[(122,142,108),(139,158,121),(104,126,96),(158,172,136),(96,116,84)]
    for i in range(4,60,4 if kind=='olive' else 5):
        px,py=pts[i]; t=i/60; base=math.atan2(pts[min(i+1,59)][1]-py,pts[min(i+1,59)][0]-px)
        for side in (-1,1):
            col=rnd.choice(greens)+(255,)
            if kind=='olive':
                leaf(d,px,py,(120-50*t)*scale,(30-8*t)*scale,base+side*rnd.uniform(0.5,0.9),col)
            else: # eucalyptus round leaves
                r=(46-18*t)*scale; off=r*0.9
                cx=px+math.cos(base+side*1.4)*off; cy=py+math.sin(base+side*1.4)*off
                d.ellipse([cx-r,cy-r*0.92,cx+r,cy+r*0.92],fill=col)
                d.line([(px,py),(cx,cy)],fill=(92,104,78,255),width=int(3*scale))

def leaves_layer():
    L=Image.new('RGBA',(W,H),(0,0,0,0))
    branch(L,-120,120,0.33,720,'euca',1,1.15)
    branch(L,-80,1330,-0.42,700,'olive',2,1.1)
    branch(L,W+60,120,math.pi-0.45,720,'olive',3,1.1)
    branch(L,W+120,1360,math.pi+0.36,740,'euca',4,1.2)
    branch(L,W//2-200,-60,math.pi/2+0.25,330,'olive',5,0.8)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); sh.paste((20,30,20,110),(10,18),L.split()[3])
    out=Image.new('RGBA',(W,H),(0,0,0,0)); out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12))); out.alpha_composite(L)
    return out

def text_block(img,x,center=False):
    d=ImageDraw.Draw(img)
    def put(y,t,f,c):
        if center:
            b=d.textbbox((0,0),t,font=f); xx=(W-(b[2]-b[0]))//2-b[0]
        else: xx=x
        d.text((xx,y),t,font=f,fill=c)
    put(SY0+40,'Ben Aslı  ·  Her gün yeni Shorts',F('Inter-ExtraBold.otf',36),(160,72,42))
    put(SY0+88,'Bedenine' if not center else 'Bedenine Yolculuk',F('InterDisplay-Black.otf',118 if not center else 140),DARK)
    if not center: put(SY0+208,'Yolculuk',F('InterDisplay-Black.otf',118),(96,118,86))
    put(SY0+348 if not center else SY0+270,'Mükemmel değil, sürdürülebilir.',F('Inter-SemiBold.otf',38 if not center else 46),DARK)

def cream_wash(img,box,alpha=170,blur=90):
    m=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(m).rounded_rectangle(box,radius=200,fill=CREAM+(alpha,))
    img.alpha_composite(m.filter(ImageFilter.GaussianBlur(blur)))

def person(img,cut,crop,height,cx,top):
    p=Image.open(f'{S}/{cut}.png').crop(crop)
    p=p.resize((int(p.width*height/p.height),height),Image.LANCZOS)
    p=ImageEnhance.Brightness(p).enhance(1.03)
    # soften hard photo edges: fade bottom 35% and side 10%
    import numpy as np
    a=np.asarray(p.split()[3]).astype('float32')/255; hh,ww=a.shape
    yy=np.linspace(0,1,hh)[:,None]; xx=np.linspace(0,1,ww)[None,:]
    fb=np.clip((1-yy)/0.35,0,1); fs=np.clip(np.minimum(xx,1-xx)/0.10,0,1)
    a=a*fb*fs; p.putalpha(Image.fromarray((a*255).astype('uint8')))
    # halo
    h=Image.new('RGBA',(W,H),(0,0,0,0)); r=int(height*0.42)
    ImageDraw.Draw(h).ellipse([cx-r,top+int(height*0.30)-r,cx+r,top+int(height*0.30)+r],fill=(255,248,228,200))
    img.alpha_composite(h.filter(ImageFilter.GaussianBlur(70)))
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); sh.paste((10,20,10,90),(cx-p.width//2+14,top+16),p.split()[3])
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(20)))
    img.alpha_composite(p,(cx-p.width//2,top))

def build(kind):
    img=nature_bg()
    if kind=='C':
        cream_wash(img,[SX0+180,SY0+10,SX1-180,SY1-10],185,80)
        img.alpha_composite(leaves_layer()); text_block(img,0,center=True)
    else:
        cream_wash(img,[SX0-40,SY0+10,SX0+780,SY1-10],175,80)
        img.alpha_composite(leaves_layer())
        if kind=='A':   # real photo: head & shoulders
            person(img,'cut_real',(0,300,788,1500),600,SX1-320,SY0+12)
        else:           # AI pool face
            person(img,'cut_ai_pool',(120,330,1000,1500),620,SX1-330,SY0-10)
        text_block(img,SX0+40)
    out=img.convert('RGB'); out.save(f'{S}/banner_{kind}.jpg',quality=92)
    g=img.copy(); gd=ImageDraw.Draw(g); gd.rectangle([SX0,SY0,SX1,SY1],outline=(0,120,255),width=8)
    g.convert('RGB').resize((1280,720)).save(f'{S}/guide_{kind}.jpg')
    out.crop((SX0,SY0,SX1,SY1)).save(f'{S}/mobile_{kind}.jpg')
for k in sys.argv[2:]: build(k)
