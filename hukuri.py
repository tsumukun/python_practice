rtfd             TXT.rtf   .	   hukuri.py  L   ¬       {\rtf1\ansi\ansicpg1252\cocoartf2576
\cocoatextscaling1\cocoaplatform1{\fonttbl\f0\fnil\fcharset0 .SFUI-Bold;\f1\fnil\fcharset0 .SFUI-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\deftab560
\pard\pardeftab560\slleading20\sa60\pardirnatural\partightenfactor0

\f0\b\fs56 \AppleTypeServices\AppleTypeServicesF2293774 \cf0 hukuri.py\
\pard\pardeftab560\sb180\sa160\pardirnatural\partightenfactor0

\f1\b0\fs34 \AppleTypeServices\AppleTypeServicesF2293774 \cf0 {{\NeXTGraphic hukuri.py \width0 \height0 \appleattachmentpadding0 \appleembedtype0 \appleaqc
}¬}\pard\pardeftab560\sb180\sa160\pardirnatural\partightenfactor0
\cf0 \
}   D         TXT.rtf	   hukuri.py      WÖ_¶          ¢Ö_             ¤  year = int(input('å¹´æ°:'))
r_i = int(input('å©åã%:'))
gaku_i = int(input('æã®æè³é¡:'))
kai = year *12
r=r_i/100
gaku = gaku_i

i=0
for i in range(kai) :
	if i ==0:
		gaku = gaku * (1+r/12)
	else:
		gaku = gaku * (1+r/12)+ gaku_i
	gaku_r=round(gaku,2)
	print(i+1,gaku_r)

toshi_gaku = gaku_i*kai
risoku = round((gaku_r - toshi_gaku),2)
print('æå¥éé¡'+str(toshi_gaku))
print('å©æ¯é¡:'+str(risoku))

