import os
# Sinh trang so do dien chi tiet (mat bang + nguyen ly + bang tinh) tu cung toa do mo hinh 3D
import re, json, math, html
import os
TOOLS=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(TOOLS)
SRC=os.path.join(ROOT,'index.html')
s=open(SRC).read()
blk=s[s.index('// ---- DIEN CHI TIET'):s.index('// ---- NUOC CHI TIET')]
COL={'C1':'#c9a100','C2':'#e53935','C3':'#43a047','C4':'#546e7a','R1':'#9e9e9e','R2':'#ef6c00','R3':'#8e24aa','R4':'#ec407a','R5':'#00acc1','PE':'#7cb342','FD':'#212121'}
runs=[]  # (circ, pts)
for m in re.finditer(r"run\('(\w+)',(\[\[.*?\]\])(?:,[\d.]+)?\)",blk):
    try: runs.append((m.group(1),json.loads(m.group(2))))
    except Exception: pass
# R2 drops in forEach
for p in [[9.45,1.15],[12.25,1.15],[13.95,1.15],[12.9,2.05]]:
    runs.append(('R2',[[8.2,p[0],2.4],[8.07,p[0],2.4],[8.07,p[0],p[1]]]))
# R1 ong cho (pipe xam)
pass
def nums(t): return [float(x) for x in t.split(',')]
sk=[nums(m.group(1))+[m.group(2) or ''] for m in re.finditer(r"sk\(([\d.,]+?)(?:,(0x[0-9a-f]+))?\)",blk)]
sk.append([8.04+0.04,12.75,0.6,'r1'])
for b_ in (9.45,12.25,13.95,12.9): sk.append([8.07,b_,1.1,''])
sw=[nums(m.group(1)) for m in re.finditer(r"sw\(([\d.,]+)\)",blk)]
lp=[nums(m.group(1)) for m in re.finditer(r"lp\(([-\d.,]+)\)",blk)]
# --- chieu dai tuyen theo mach
def L(pts): return sum(math.dist(pts[i],pts[i+1]) for i in range(len(pts)-1))
route={}
for c,p in runs: route[c]=route.get(c,0)+L(p)
# --- walls
walls=[]
for m in re.finditer(r"wall\('([xy])',([\d.]+),([\d.]+),([\d.]+),([\d.]+),[\d.]+,(\[.*?\]\]|\[\]),",s):
    ax,x0,y0,Ln,T=m.group(1),*map(float,m.groups()[1:5]); ops=json.loads(m.group(6))
    if not (7<x0<19 and 5<y0<19): continue
    walls.append((ax,x0,y0,Ln,T,[o for o in ops if o[2]<0.1]))
# --- SVG mat bang
A0,A1,B0,B1=5.0,19.6,-1.2,20.3; S=46
def X(a): return (a-A0)*S
def Y(b): return (B1-b)*S
W,H=X(A1),Y(B0)
o=[]
o.append(f'<svg viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="10"><style>text{{paint-order:stroke;stroke:#fff;stroke-width:3px;stroke-linejoin:round}}</style>')
o.append(f'<rect width="{W:.0f}" height="{H:.0f}" fill="#fff"/>')
for ax,x0,y0,Ln,T,ops in walls:
    segs=[];cur=0
    for s0,s1,_,_ in sorted(ops): segs.append((cur,s0)); cur=s1
    segs.append((cur,Ln))
    for a,b in segs:
        if b-a<=0: continue
        if ax=='x': o.append(f'<rect x="{X(x0+a):.1f}" y="{Y(y0+T):.1f}" width="{(b-a)*S:.1f}" height="{max(T*S,3):.1f}" fill="#9e9e9e"/>')
        else: o.append(f'<rect x="{X(x0):.1f}" y="{Y(y0+b):.1f}" width="{max(T*S,3):.1f}" height="{(b-a)*S:.1f}" fill="#9e9e9e"/>')
# room names
for t,a,b in [('PHÒNG KHÁCH',16.2,6.3),('PHÒNG NGỦ 1',16.6,12.6),('PHÒNG NGỦ 2',16.6,15.3),('HÀNH LANG',14.8,15.2),('BẾP – ĂN',10.6,9.4),('KHU GIẶT',13.0,15.6),('WC + TẮM',9.9,17.6),('SÂN XE / SÂN TRƯỚC',10.9,5.6),('CỔNG',12.0,-0.9),('GIẾNG',12.0,20.0)]:
    o.append(f'<text x="{X(a):.0f}" y="{Y(b):.0f}" fill="#bdbdbd" font-size="11" font-weight="bold" text-anchor="middle">{t}</text>')
o.append(f'<rect x="{X(14.5):.1f}" y="{Y(18.0):.1f}" width="{0.5*S:.1f}" height="{11*S:.1f}" fill="#eceff1" stroke="#b0bec5"/>')
o.append(f'<text x="{X(14.75):.0f}" y="{Y(17.4):.0f}" font-size="9" text-anchor="middle" fill="#607d8b">máng chung</text>')
TAGDONE=set()
WIRES={'C1':'3×1,5','C2':'3×2,5','C3':'3×2,5','C4':'3×1,5','R1':'ống chờ Ø25','R2':'3×2,5','R3':'3×2,5','R4':'3×4','R5':'CVV 3×2,5'}
order=['FD','PE','R1','C4','C3','C2','R3','R4','R5','R2','C1']
for c in order:
    for cc,p in runs:
        if cc!=c: continue
        pts=' '.join(f'{X(q[0]):.1f},{Y(q[1]):.1f}' for q in p)
        dash=' stroke-dasharray="5 3"' if c in('R1','PE') or any(q[2]<0 for q in p) else ''
        k='FD' if c=='PE' else c
        stc='#263238' if c=='FD' else ('#7cb342' if c=='PE' else '#78909c')
        o.append(f'<polyline class="r r-{k}" points="{pts}" fill="none" stroke="{stc}" stroke-width="{3 if c=="FD" else 2}"{dash} stroke-linejoin="round"/>')
for m_ in re.finditer(r"LBL\('((C\d|R\d)[^']*)',([\d.]+),([\d.]+),",blk):
    c=m_.group(2); a,b=float(m_.group(3)),float(m_.group(4))
    if c in TAGDONE: continue
    TAGDONE.add(c)
    o.append(f'<text class="r r-{c}" x="{X(a):.0f}" y="{Y(b)-6:.0f}" font-size="10" font-weight="bold" fill="#263238">{c} · {WIRES[c]}</text>')
for a,b,z in lp:
    o.append(f'<g transform="translate({X(a):.1f},{Y(b):.1f})"><circle r="6" fill="#fff59d" stroke="#333"/><path d="M-4,-4L4,4M-4,4L4,-4" stroke="#333"/></g>')
for a,b,z in sw:
    o.append(f'<g transform="translate({X(a):.1f},{Y(b):.1f})"><circle r="3.5" fill="#333"/><path d="M0,0L8,-7" stroke="#333" stroke-width="1.5"/></g>')
for a,b,z,c in sk:
    fill='#455a64' if c=='0x455a64' else ('#bdbdbd' if c in('0xffe0b2','r1') else '#fff')
    o.append(f'<g transform="translate({X(a):.1f},{Y(b):.1f})"><path d="M-6,0A6,6 0 0 1 6,0Z" fill="{fill}" stroke="#333"/><line x1="0" y1="-6" x2="0" y2="-10" stroke="#333"/></g>')
o.append(f'<rect x="{X(15.42):.1f}" y="{Y(10.0):.1f}" width="{0.486*S:.1f}" height="{0.49*S:.1f}" fill="#8d6e63" stroke="#4e342e"/><text x="{X(15.66):.0f}" y="{Y(9.5)+12:.0f}" text-anchor="middle" fill="#4e342e" font-size="9">tủ mạng</text>')
# tu dien, quat, cot dia, hop noi
o.append(f'<rect x="{X(14.21)-5:.1f}" y="{Y(7.45):.1f}" width="12" height="{0.5*S:.1f}" fill="#263238"/><text x="{X(14.21)+10:.0f}" y="{Y(7.2)+3:.0f}" font-weight="bold">TỦ ĐIỆN</text>')
o.append(f'<rect x="{X(11.85):.1f}" y="{Y(-0.3):.1f}" width="16" height="8" fill="#fff" stroke="#333"/><text x="{X(11.85):.0f}" y="{Y(-0.3)+18:.0f}">Công tơ</text>')
for b in (4.3,):
    o.append(f'<g transform="translate({X(13.6):.1f},{Y(b):.1f})"><path d="M-7,0H7M-5,3H5M-3,6H3M0,-6V0" stroke="#7cb342" stroke-width="2"/></g>')
o.append(f'<text x="{X(13.6)-8:.0f}" y="{Y(5.5):.0f}" fill="#558b2f" text-anchor="end">1 cọc tiếp địa</text>')
o.append(f'<g transform="translate({X(11.3):.1f},{Y(11.2):.1f})"><circle r="9" fill="none" stroke="#333"/><path d="M0,0L8,-3M0,0L-6,6M0,0L-2,-8" stroke="#333" stroke-width="2"/></g><text x="{X(11.3)+12:.0f}" y="{Y(11.2)+4:.0f}">Quạt trần</text>')
o.append(f'<rect x="{X(9.35):.1f}" y="{Y(18.2):.1f}" width="14" height="6" fill="#78909c"/><text x="{X(9.35):.0f}" y="{Y(18.2)-3:.0f}">Quạt hút</text>')
o.append(f'<rect x="{X(8.12):.1f}" y="{Y(16.59):.1f}" width="{0.1*S:.1f}" height="{0.19*S:.1f}" fill="#fce4ec" stroke="#d81b60"/><text x="{X(8.3)+2:.0f}" y="{Y(16.5):.0f}" fill="#ad1457">Máy NL 4,5kW</text>')
o.append(f'<rect x="{X(12.5):.1f}" y="{Y(19.65):.1f}" width="{0.45*S:.1f}" height="{0.3*S:.1f}" fill="#bbdefb" stroke="#1565c0"/><text x="{X(12.5)-2:.0f}" y="{Y(19.65)-3:.0f}" text-anchor="end">Bơm giếng</text>')
o.append(f'<text x="{X(12.45):.0f}" y="{Y(-0.3)-10:.0f}" fill="#00838f">Đèn NLMT</text>')
# ghi chu thiet bi
notes=[('TV',17.7,7.05,'end',4),('Sofa',14.3,8.3,'start',4),('Bàn LV ×2',16.7,9.7,'middle',14),('Ổ máy lạnh 2,4m',17.0,12.1,'middle',16),('Đầu giường P1 ×2',16.7,13.75,'middle',14),('Ổ C4 tủ mạng',15.5,9.6,'middle',16),('Đầu giường P2 ×2',17.6,16.8,'end',4),
       ('Tủ lạnh',7.9,9.45,'end',4),('Mặt bếp',7.9,12.2,'end',8),('Ổ bếp từ đợt 2',7.9,12.62,'end',4),('Hút mùi',7.9,13.0,'end',0),('Đầu bàn',7.9,13.95,'end',4),('Ổ BE6500 #2',13.9,10.7,'end',4),
       ('Giặt + sấy 1,2m',11.6,17.6,'start',-8),('CT nóng lạnh',11.6,16.85,'start',18),('IP55 sân xe',8.6,7.64,'start',14),('IP55 hiên sau',15.8,18.58,'start',4)]
for t,a,b,anc,dy in notes:
    dx=12 if anc=='start' else 0
    o.append(f'<text x="{X(a)+dx:.0f}" y="{Y(b)+dy:.0f}" text-anchor="{anc}" fill="#37474f">{t}</text>')
# thuoc ti le
o.append(f'<g transform="translate(20,{H-20:.0f})"><path d="M0,0H{2*S}" stroke="#333" stroke-width="2"/><path d="M0,-4V4M{S},-3V3M{2*S},-4V4" stroke="#333"/><text x="{S}" y="-7" text-anchor="middle">2 m</text></g>')
o.append(f'<g transform="translate({W-40:.0f},40)"><path d="M0,14L0,-14M0,-14L-5,-4M0,-14L5,-4" stroke="#333" stroke-width="2"/><text y="28" text-anchor="middle">Sau nhà</text></g>')
o.append('</svg>')
plan='\n'.join(o)
# --- so do nguyen ly
CIRC=[('C1','MCB 1P 10A','3×1,5mm² (L+N+PE)','Đèn 10 bóng + quạt trần + quạt hút WC',0.4,'RCCB1'),
      ('C2','MCB 1P 20A','3×2,5mm² (L+N+PE)','Ổ cắm nhà chính: TV, sofa, bàn LV ×2, phòng ngủ 1 ×3, phòng ngủ 2 ×2',1.5,'RCCB1'),
      ('C3','MCB 1P 20A','3×2,5mm² (L+N+PE)','Máy lạnh 1,5HP phòng ngủ',1.2,'RCCB1'),
      ('C4','RCBO 1P+N 10A 30mA','3×1,5mm² (L+N+PE)','Tủ mạng (phòng khách cạnh bàn LV): UPS → PDU',0.15,'RCBO'),
      ('R2','RCBO 2P 20A 30mA','3×2,5mm² (L+N+PE)','Ổ bếp ×4: tủ lạnh, mặt bếp, hút mùi, đầu bàn + ổ BE6500 #2',2.2,'RCBO'),
      ('R4','RCBO 2P 25A 30mA','3×4mm² (L+N+PE)','Máy nước nóng trực tiếp Panasonic 4500W có sẵn (đấu cố định, ống riêng)',4.5,'RCBO'),
      ('R3','MCB 1P 20A','3×2,5mm² (L+N+PE)','Máy giặt + máy sấy (2 ổ đơn, ống riêng)',2.5,'RCCB'),
      ('R5','MCB 1P 16A','CVV 3×2,5mm² (L+N+PE)','Ngoài trời: đèn hiên ×2, đèn pha, IP55 ×2, bơm giếng 0,75kW',1.1,'RCCB'),
      ('R1','RCBO 2P 25A (đợt 2)','3×4mm² (đợt 2)','Bếp từ đôi 3,5kW – đợt 1 chỉ ống chờ Ø25',3.5,'D2')]
sw_=34*len(CIRC)+40
g=[f'<svg viewBox="0 0 900 {sw_+170}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11">','<rect width="900" height="100%" fill="#fff"/>']
g.append('<rect x="10" y="20" width="90" height="34" fill="#fff" stroke="#333"/><text x="55" y="41" text-anchor="middle">Công tơ EVN</text>')
g.append('<path d="M100,37H150" stroke="#212121" stroke-width="3"/><text x="104" y="30" font-size="9">CVV 2×25 ~15m</text>')
g.append('<rect x="150" y="22" width="70" height="30" fill="#eceff1" stroke="#333"/><text x="185" y="35" text-anchor="middle" font-weight="bold">CB tổng</text><text x="185" y="47" text-anchor="middle">2P 63A</text>')
g.append('<path d="M220,37H250" stroke="#333" stroke-width="2"/><path d="M250,37V' + str(sw_) + '" stroke="#333" stroke-width="4"/>')
g.append('<path d="M236,37V70" stroke="#333"/><rect x="200" y="70" width="38" height="22" fill="#fff3e0" stroke="#333"/><text x="219" y="85" text-anchor="middle">SPD</text><path d="M219,92V108" stroke="#7cb342" stroke-width="2"/><text x="160" y="106" font-size="9" fill="#558b2f">→ thanh PE</text>')
y=60; seen=set()
for i,(c,cb,day,tai,kw,kind) in enumerate(CIRC):
    y=60+i*34
    x0=250
    if kind in('RCCB','RCCB1'):
        if kind not in seen:
            seen.add(kind); cnt=sum(1 for q in CIRC if q[5]==kind)
            g.append(f'<path d="M250,{y}H262" stroke="#333" stroke-width="2"/><rect x="262" y="{y-12}" width="92" height="24" fill="#e1f5fe" stroke="#0277bd"/><text x="308" y="{y+4}" text-anchor="middle" font-size="9.5">RCCB {'#1' if kind=='RCCB1' else '#2'} 63A 30mA</text>')
            g.append(f'<path d="M360,{y}V{y+34*(cnt-1)}" stroke="#333" stroke-width="3"/>')
        x0=360
    else:
        pass
        g.append(f'<path d="M250,{y}H375" stroke="#333" stroke-width="2"/>')
        x0=375-0
    if kind in('RCCB','RCCB1'): g.append(f'<path d="M360,{y}H375" stroke="#333" stroke-width="2"/>')
    dash=' stroke-dasharray="4 3"' if kind=='D2' else ''
    g.append(f'<rect x="375" y="{y-11}" width="120" height="22" fill="#fff" stroke="#333"{dash}/><text x="435" y="{y+4}" text-anchor="middle" font-size="10">{cb}</text>')
    g.append(f'<path d="M495,{y}H525" stroke="#263238" stroke-width="3"{dash}/><text x="530" y="{y-2}" font-weight="bold" fill="#263238">{c} · {day}</text><text x="530" y="{y+11}" font-size="9.5" fill="#37474f">{html.escape(tai)}</text>')
yb=60+len(CIRC)*34
g.append(f'<text x="255" y="{yb}" font-size="10" fill="#607d8b">Còn ~6 module trống: thiết bị lớn sau này, máy lạnh 2, nhà xe, bơm tăng áp</text>')
g.append(f'<rect x="20" y="{yb+20}" width="230" height="24" fill="#f1f8e9" stroke="#7cb342"/><text x="135" y="{yb+36}" text-anchor="middle">Thanh PE (tiếp địa) trong tủ</text>')
g.append(f'<path d="M135,{yb+44}V{yb+80}" stroke="#7cb342" stroke-width="2" stroke-dasharray="5 3"/><text x="140" y="{yb+66}" font-size="9.5" fill="#558b2f">cáp đồng trần 16mm² ngầm 0,5m</text>')
for k in range(1):
    cx=105+60*k
    g.append(f'<path d="M{cx},{yb+80}V{yb+95}M{cx-12},{yb+95}H{cx+12}M{cx-8},{yb+100}H{cx+8}M{cx-4},{yb+105}H{cx+4}" stroke="#7cb342" stroke-width="2"/>')
g.append(f'<path d="M105,{yb+80}H165" stroke="#7cb342" stroke-width="2"/><text x="180" y="{yb+100}" font-size="9.5" fill="#558b2f">1 cọc đồng Ø16×2,4m · mọi mạch có chống giật 30mA</text>')
g.append(f'<text x="290" y="{yb+36}" font-size="10" fill="#37474f">Mỗi mạch một tuyến từ tủ, trong mạch rẽ nhánh; đủ 3 dây L – N – PE. Tủ 24 module (đợt 1 dùng 17).</text>')
g.append('</svg>')
one='\n'.join(g)
# --- so do tach soi tung mach
WC_={'L':'#e53935','N':'#1e88e5'}
def wire(x1,y1,x2,y2,w,dash=''):
    if w=='PE': return f'<path d="M{x1},{y1}L{x2},{y2}" stroke="#43a047" stroke-width="3"{dash}/><path d="M{x1},{y1}L{x2},{y2}" stroke="#fdd835" stroke-width="3" stroke-dasharray="5 5"/>'
    return f'<path d="M{x1},{y1}L{x2},{y2}" stroke="{WC_[w]}" stroke-width="2.5"{dash}/>'
def csvg(c,prot,ws,sw,loads,cond,note,d2=False):
    n=max(1,len(loads)); H=max(110,30+n*44)
    yL,yN,yP=40,56,90
    dash=' stroke-dasharray="6 4"' if d2 else ''
    q=[f'<svg viewBox="0 0 680 {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11"><style>text{{paint-order:stroke;stroke:#fff;stroke-width:3px}}</style><rect width="680" height="{H}" fill="#fff"/>']
    q.append(f'<rect x="10" y="26" width="110" height="78" rx="6" fill="#eceff1" stroke="#455a64"/><text x="65" y="56" text-anchor="middle" font-weight="bold">{c}</text><text x="65" y="74" text-anchor="middle" font-size="10">{prot}</text>')
    q.append(f'<rect x="135" y="28" width="200" height="74" rx="5" fill="#cfd8dc" fill-opacity=".35" stroke="#90a4ae" stroke-dasharray="4 3"/><text x="140" y="20" font-size="10" fill="#37474f">{cond}</text>')
    xs=345
    for w,yy in (('L',yL),('N',yN),('PE',yP)):
        if w in ws: q.append(wire(120,yy,xs,yy,w,dash))
    if sw:
        if sw=='CT 1 cực': q.append(f'<rect x="{xs}" y="29" width="62" height="22" rx="4" fill="#fff" stroke="#455a64"/><text x="{xs+31}" y="44" text-anchor="middle" font-size="10">{sw}</text>')
        else: q.append(f'<rect x="{xs}" y="30" width="62" height="36" rx="4" fill="#fff" stroke="#455a64"/><text x="{xs+31}" y="52" text-anchor="middle" font-size="10">{sw}</text>')
        if sw=='CT 1 cực' and 'N' in ws: q.append(wire(xs,yN,xs+62,yN,'N',dash))
        if 'PE' in ws: q.append(wire(xs,yP,xs+62,yP,'PE',dash))
        if sw=='CT 1 cực': q.append(f'<text x="{xs}" y="80" font-size="9" fill="#607d8b">cắt dây L</text>')
        else: q.append(f'<text x="{xs}" y="80" font-size="9" fill="#607d8b">cắt cả L và N</text>')
    xb=430
    ys=[30+i*44+14 for i in range(n)]
    for w,off in (('L',-10),('N',0),('PE',10)):
        if w not in ws: continue
        y0={'L':yL,'N':yN,'PE':yP}[w]
        x0=xs+62 if sw else xs
        xb_=xb+{'L':0,'N':8,'PE':16}[w]
        q.append(wire(x0,y0,xb_,y0,w,dash))
        top=min(y0,min(ys)+off); bot=max(y0,max(ys)+off)
        q.append(wire(xb_,top,xb_,bot,w,dash))
        for yy in ys: q.append(wire(xb_,yy+off,480,yy+off,w,dash))
    for i,(t,sub) in enumerate(loads):
        yy=ys[i]
        q.append(f'<rect x="480" y="{yy-16}" width="190" height="32" rx="5" fill="#fff" stroke="#455a64"{dash}/><text x="488" y="{yy-2}" font-weight="bold" font-size="10.5">{t}</text><text x="488" y="{yy+11}" font-size="9.5" fill="#546e7a">{sub}</text>')
    q.append('</svg>')
    return f'<h3 style="font-size:14px;margin:16px 0 4px">{c} – {note}</h3>'+''.join(q)
DIAG=[
 ('FD','CB tổng 2P 63A',['L','N','PE'],None,[('Công tơ EVN (≥63A) → tủ','CVV 2×25mm²: L đỏ + N xanh'),('Thanh PE trong tủ','từ 1 cọc đồng Ø16×2,4m, cáp đồng 16mm²')],'Cáp CVV 2×25 chôn 0,5m trong ống HDPE Ø50 · PE riêng từ cọc','Nguồn vào + tiếp địa'),
 ('C1','RCCB #1 + MCB 10A',['L','N','PE'],'CT 1 cực',[('Đèn ×10','PK, HL, 2 PN, bếp, giặt, WC'),('Quạt trần bàn ăn','qua hộp số'),('Quạt hút WC','CT chung với đèn WC')],'Ống PVC Ø16 · 3 sợi 1,5mm² (L+N+PE)','Đèn + quạt (PE cho quạt, đèn vỏ kim loại)'),
 ('C2','RCCB #1 + MCB 20A',['L','N','PE'],None,[('Ổ đôi phòng khách ×4','TV, sofa, bàn LV ×2 (1,1m)'),('Ổ đôi phòng ngủ 1 ×3','đầu giường, cao 1,0m'),('Ổ đôi phòng ngủ 2 ×2','đầu giường, cao 1,0m')],'Ống PVC Ø20 · 3 sợi 2,5mm² (L+N+PE)','Ổ cắm nhà chính'),
 ('C3','RCCB #1 + MCB 20A',['L','N','PE'],None,[('Ổ đơn máy lạnh','cao 2,4m cạnh dàn lạnh PN1')],'Ống PVC Ø20 · 3 sợi 2,5mm²','Máy lạnh 1,5HP'),
 ('C4','RCBO 10A 30mA',['L','N','PE'],None,[('Ổ đơn sau UPS','cao 0,6m → UPS → PDU')],'Ống PVC Ø16 · 3 sợi 1,5mm²','Tủ mạng'),
 ('R2','RCBO 2P 20A 30mA',['L','N','PE'],None,[('Ổ tủ lạnh','cao 1,1m'),('Ổ mặt bếp ×2','cách chậu ≥0,6m, cao 1,1m'),('Ổ hút mùi + đầu bàn','+ ổ BE6500 #2')],'Ống PVC Ø20 · 3 sợi 2,5mm²','Ổ cắm bếp'),
 ('R3','RCCB #2 + MCB 20A',['L','N','PE'],None,[('Ổ đơn máy giặt','cao 1,2m'),('Ổ đơn máy sấy','cao 1,2m')],'Ống PVC Ø20 riêng · 3 sợi 2,5mm²','Máy giặt + máy sấy'),
 ('R4','RCBO 25A 30mA',['L','N','PE'],'CT 2 cực',[('Máy nước nóng trực tiếp 4500W','Panasonic DH-4VP1VW · hộp nối kín · PE bắt vỏ')],'Ống PVC Ø25 riêng · 3 sợi 4mm² (mua mới)','Nóng lạnh (CT 2 cực ≥25A có đèn ngoài cửa WC)'),
 ('R5','RCCB #2 + MCB 16A',['L','N','PE'],None,[('Đèn hiên trước + sau','cảm biến'),('Đèn pha sân xe','cảm biến'),('Ổ IP55 ×2','sân xe, hiên sau'),('Bơm giếng 0,75kW','ổ IP55 + CT kín')],'Cáp CVV 3×2,5mm² đi nổi · đoạn chôn trong HDPE','Ngoài trời'),
 ('R1','RCBO 2P 25A (đợt 2)',['L','N','PE'],None,[('Hộp đấu bếp từ (đợt 2)','dưới mặt bếp 0,6m')],'Đợt 1: ống PVC Ø25 chờ + dây mồi · đợt 2 kéo 3×4mm²','Bếp từ (nét đứt = làm đợt 2)')]
multi=''.join(csvg(c,p,ws,sw,ld,cd,nt,d2=(c=='R1')) for c,p,ws,sw,ld,cd,nt in DIAG)
# --- bang tinh
rows=[]
CNT={'C1':(0,8,10,'+ quạt trần, quạt hút WC'),'C2':(9,0,0,''),'C3':(1,0,0,'ổ đơn'),'C4':(1,0,0,'ổ đơn'),'R2':(5,0,0,''),'R3':(2,0,0,'ổ đơn'),'R4':(0,1,0,'CT 2 cực + hộp đấu kín'),'R5':(2,0,3,'IP55; + bơm giếng'),'R1':(1,0,0,'ổ 32A đợt 2')}
def seglen_np(c):
    t=0
    for cc,p in runs:
        if cc!=c: continue
        for i in range(len(p)-1):
            if p[i][0]<14.05 and p[i+1][0]<14.05: t+=math.dist(p[i],p[i+1])
    return t
newwire=0
for c in ['C1','C2','C3','C4','R2','R3','R4','R5','R1']:
    ns,nw,nl,nt=CNT[c]
    r=route.get(c,0); ong=math.ceil(r*1.1)
    nwr=3
    day=0 if c=='R1' else math.ceil(ong*nwr+(ns+nw+nl)*0.6*nwr)
    rows.append((c,ong,day,ns,nw,nl,nt))
c1np=seglen_np('C1')
newwire=math.ceil(c1np*1.1*3)+sum(r[2] for r in rows if r[0] in('C3','C4','R2','R3'))
r4wire=[r[2] for r in rows if r[0]=='R4'][0]
info={'route':{k:round(v,1) for k,v in route.items()},'rows':rows,'c1np':round(c1np,1),'newwire':newwire,'r4wire':r4wire}
json.dump(info,open('/tmp/dien_info.json','w'),ensure_ascii=False)
CI={c[0]:c for c in CIRC}
tb=['<table><tr><th>Mạch</th><th>Bảo vệ</th><th>Dây</th><th>Tải ước (kW)</th><th>Ống ~m</th><th>Dây ~m (tổng các sợi)</th><th>Ổ</th><th>Công tắc</th><th>Đèn</th><th>Ghi chú</th></tr>']
tot=0
for c,ong,day,ns,nw,nl,nt in rows:
    _,cb,d,tai,kw,_=CI[c]; tot+=kw if c!='R1' else 0
    tb.append(f'<tr><td style="font-weight:bold">{c}</td><td>{cb}</td><td>{d}</td><td>{str(kw).replace(".",",")}</td><td>{ong}</td><td>{day if day else "đợt 2"}</td><td>{ns}</td><td>{nw}</td><td>{nl}</td><td>{nt}</td></tr>')
tb.append('</table>')
tot_r=round(tot,2)
import sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from plan_common import nav
NAV=nav('dien.html')
page=f'''<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sơ đồ điện chi tiết – nhà Duyên Hải</title>
<style>body{{font-family:Arial,sans-serif;margin:0;padding:12px;color:#263238;max-width:1100px;margin:auto}}h1{{font-size:20px}}h2{{font-size:16px;margin-top:22px;border-bottom:2px solid #eceff1;padding-bottom:4px}}
svg{{width:100%;height:auto;border:1px solid #eceff1;border-radius:6px}}table{{border-collapse:collapse;width:100%;font-size:13px}}td,th{{border:1px solid #cfd8dc;padding:4px 6px;text-align:left}}th{{background:#eceff1}}
.lg span{{display:inline-block;margin:2px 10px 2px 0;font-size:13px}}.lg i{{display:inline-block;width:22px;height:4px;vertical-align:middle;margin-right:4px}}a{{color:#1565c0}}ul{{font-size:14px;line-height:1.5}}
#fl button{{border:1px solid #b0bec5;background:#fff;border-radius:14px;padding:4px 10px;font-size:12px}}#fl button.on{{background:#263238;color:#fff}}@media print{{a.back{{display:none}},#fl{{display:none}}}}</style></head><body>
{NAV}
<h1>Sơ đồ điện chi tiết – nhà Duyên Hải (đợt 1, đã tối ưu)</h1>
<p style="font-size:14px">Cùng toạ độ với lớp <b>Điện</b> trong mô hình 3D. Nét liền: đi nổi trong nhà; nét đứt: đi ngầm hoặc ống chờ. Tỉ lệ thước 2m ở góc dưới.</p>
<div class="lg"><span><i style="background:#e53935"></i>Dây pha L (đỏ)</span><span><i style="background:#1e88e5"></i>Trung tính N (xanh dương)</span><span><i style="background:repeating-linear-gradient(90deg,#43a047 0 5px,#fdd835 5px 10px)"></i>Tiếp địa PE (vàng-xanh)</span><span><i style="background:#78909c"></i>Ống luồn trên mặt bằng</span><span><i style="background:#263238"></i>Cáp nguồn</span></div>
<div class="lg" style="font-size:13px">Ký hiệu: ⊗ đèn · ● công tắc (cao 1,25m) · ◓ ổ cắm (cao 1,0m; xám đậm = IP55 ngoài trời; xám nhạt = ổ chờ đợt 2)</div>
<h2>1. Mặt bằng bố trí điện</h2>
<p style="font-size:13px">Mặt bằng chỉ vẽ tuyến ống luồn (xám). Bấm một mạch để làm nổi tuyến của mạch đó; từng sợi dây vẽ ở mục 3.</p>
<div id="fl" style="display:flex;flex-wrap:wrap;gap:6px;margin:6px 0">{''.join(f'<button data-k="{k}">{t}</button>' for k,t in [('all','Tất cả'),('FD','Nguồn + PE'),('C1','C1 đèn'),('C2','C2 ổ nhà chính'),('C3','C3 máy lạnh'),('C4','C4 tủ mạng'),('R1','R1 bếp từ'),('R2','R2 ổ bếp'),('R3','R3 giặt sấy'),('R4','R4 nóng lạnh'),('R5','R5 ngoài trời')])}</div>
{plan}
<script>document.querySelectorAll('#fl button').forEach(b=>b.onclick=()=>{{const k=b.dataset.k;document.querySelectorAll('#fl button').forEach(x=>x.classList.toggle('on',x===b));document.querySelectorAll('.r').forEach(e=>{{const on=k==='all'||e.classList.contains('r-'+k);e.style.opacity=on?1:0.12;if(e.tagName==='polyline'){{e.style.strokeWidth=(k!=='all'&&on)?4:'';e.style.stroke=(k!=='all'&&on&&!e.classList.contains('r-FD'))?'#263238':'';}}}});}});</script>
<h2>2. Sơ đồ nguyên lý tủ điện</h2>
{one}
<h2>3. Sơ đồ tách sợi từng mạch</h2>
<p style="font-size:13px">Mỗi mạch đi ống riêng từ tủ. Vẽ đủ từng sợi theo màu chuẩn IEC 60445: L đỏ, N xanh dương, PE sọc vàng-xanh.</p>
{multi}
<h2>4. Bảng tính theo mạch</h2>
{''.join(tb)}
<p style="font-size:13px">Tổng tải lắp đặt đợt 1 ≈ <b>{str(tot_r).replace(".",",")} kW</b> (chưa gồm bếp từ). Hệ số đồng thời ~0,6 → ≈ {str(round(tot_r*0.6,1)).replace(".",",")} kW ≈ <b>{round(tot_r*0.6*1000/220)}A</b>; khi có bếp từ ≈ {round((tot_r+3.5)*0.6*1000/220)}A; đủ thiết bị tương lai ≈ 56A, <b>dưới CB tổng 63A</b> (xem mục 6). Chiều dài ống đo theo tuyến 3D +10%; dây = ống × 3 lõi + 0,6m mỗi thiết bị. C1, C2 ở nhà chính giữ dây cũ đi nổi nên <b>dây 1,5/2,5mm² mới chỉ cần ≈ {newwire} m</b> (C1 phần nhà phụ, C3, C4, R2, R3), dùng dây có sẵn; <b>R4 mua dây 4mm² ≈ {r4wire} m</b>; R5 dùng cáp CVV 3×2,5 (có PE) cho đoạn ngoài trời ≈ 18–20m.</p>
<h2>5. Quy cách thi công</h2>
<ul>
<li>Công tắc 1,25m cạnh mép cửa phía tay nắm; ổ cắm 1,0m (chừa nâng nền); bàn làm việc, mặt bếp 1,1m; giặt sấy 1,2m; máy lạnh 2,4m; ổ bếp từ dưới mặt bếp 0,6m.</li>
<li>Hộp công tắc 86 sâu, có dây N (để sau thay công tắc Zigbee). Màu dây: L đỏ/nâu, N xanh dương, PE vàng-xanh.</li>
<li>Nhà chính: dây cũ đang đi nổi – đo cách điện từng mạch ≥1 MΩ thì giữ cho C1, C2; dây mới đi ống nổi/nẹp sát trần, không đục tường.</li>
<li>Máy nước nóng trực tiếp 4500W: dây 4mm² đi ống riêng + RCBO 25A 30mA riêng, công tắc 2 cực ≥25A có đèn ngoài cửa WC, đấu cố định qua hộp kín, PE nối vỏ máy, không đặt ổ cắm trong WC.</li><li>Chống giật: C1–C3 qua RCCB 63A #1; C4, R2, R4 mỗi mạch RCBO riêng; R3, R5 qua RCCB 63A #2. Cỡ dây theo sức chịu khi đi ống, trời nóng: 1,5mm² ≤10A, 2,5mm² ≤20A, 4mm² ≤25A; R3, R4, R5 đi ống riêng cách ≥2cm, máng chung chỉ cho C3, C4. Dây cũ C2 phải đúng 2,5mm², nếu 1,5mm² thì hạ MCB xuống 16A. Nhà nối đất cọc riêng nên MCB không tự cắt khi rò ra vỏ; mạch nào cũng phải có 30mA.</li>
<li>R5 ngoài trời: cáp CVV <b>3×2,5</b> (có sợi PE cho ổ IP55 và bơm) đi nổi trên tường, chỉ chôn ~5m ra bơm trong ống HDPE sâu 0,5m. Đèn cổng dùng năng lượng mặt trời.</li>
<li>Kiểm tra trước khi đóng điện: bấm nút TEST trên RCCB và RCBO, đo điện trở đất, đo cách điện, thử đúng pha bằng ổ test 3 đèn.</li>
</ul>
<h2>6. Cáp nguồn và CB tổng (chốt 17/11: làm sẵn công suất lớn)</h2>
<ul>
<li>Đợt 1 tải đồng thời ≈ {round(tot_r*0.6*1000/220)}A; có bếp từ ≈ {round((tot_r+3.5)*0.6*1000/220)}A; đủ thiết bị tương lai (máy lạnh 2, xưởng mộc, máy rửa xe, bơm tăng áp) ≈ 56A.</li>
<li><b>Chọn: CB tổng 2P 63A + cáp CVV 2×25mm² ~15m chôn 0,5m trong ống HDPE Ø50.</b> Cáp 6mm² chôn ngầm chỉ chịu ~34–40A, 10mm² ~45–50A; 25mm² dư cho 63A, khỏi đào lại.</li>
<li>Hai RCCB loại 63A để khớp CB tổng (RCCB không tự cắt quá tải, phải ≥ CB phía trên).</li>
<li><b>Cần làm với Điện lực:</b> xem dòng định mức ghi trên công tơ. Loại 10(80)A hoặc 5(80)A thì dùng được; loại 10(40)A thì xin nâng công tơ trước khi đóng điện.</li>
</ul>
</body></html>'''
open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'dien.html'),'w').write(page)
print(json.dumps(info,ensure_ascii=False))
