# Sinh trang so do dien chi tiet (mat bang + nguyen ly + bang tinh) tu cung toa do mo hinh 3D
import re, json, math, html
SRC='/home/claude/nha3d.html'
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
m=re.search(r"pipe\((\[\[14.25,7.2,1.95\].*?\]\]),0xbdbdbd",blk); runs.append(('R1',json.loads(m.group(1))))
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
for t,a,b in [('PHÒNG KHÁCH',16.2,6.3),('PHÒNG NGỦ',16.6,12.6),('KHO',16.6,16.9),('HÀNH LANG',14.8,15.2),('BẾP – ĂN',10.6,9.4),('KHU GIẶT',13.0,15.6),('WC + TẮM',9.9,17.6),('SÂN XE / SÂN TRƯỚC',10.9,5.6),('CỔNG',12.0,-0.9),('GIẾNG',12.0,20.0)]:
    o.append(f'<text x="{X(a):.0f}" y="{Y(b):.0f}" fill="#bdbdbd" font-size="11" font-weight="bold" text-anchor="middle">{t}</text>')
o.append(f'<rect x="{X(14.5):.1f}" y="{Y(18.0):.1f}" width="{0.5*S:.1f}" height="{11*S:.1f}" fill="#eceff1" stroke="#b0bec5"/>')
o.append(f'<text x="{X(14.75):.0f}" y="{Y(17.4):.0f}" font-size="9" text-anchor="middle" fill="#607d8b">máng chung</text>')
order=['FD','PE','R1','C4','C3','C2','R3','R4','R5','R2','C1']
for c in order:
    for cc,p in runs:
        if cc!=c: continue
        pts=' '.join(f'{X(q[0]):.1f},{Y(q[1]):.1f}' for q in p)
        dash=' stroke-dasharray="5 3"' if c in('R1','PE') or any(q[2]<0 for q in p) else ''
        o.append(f'<polyline points="{pts}" fill="none" stroke="{COL[c]}" stroke-width="{3 if c=="FD" else 2}"{dash} stroke-linejoin="round"/>')
for a,b,z in lp:
    o.append(f'<g transform="translate({X(a):.1f},{Y(b):.1f})"><circle r="6" fill="#fff59d" stroke="#333"/><path d="M-4,-4L4,4M-4,4L4,-4" stroke="#333"/></g>')
for a,b,z in sw:
    o.append(f'<g transform="translate({X(a):.1f},{Y(b):.1f})"><circle r="3.5" fill="#333"/><path d="M0,0L8,-7" stroke="#333" stroke-width="1.5"/></g>')
for a,b,z,c in sk:
    fill='#455a64' if c=='0x455a64' else ('#bdbdbd' if c in('0xffe0b2','r1') else '#fff')
    o.append(f'<g transform="translate({X(a):.1f},{Y(b):.1f})"><path d="M-6,0A6,6 0 0 1 6,0Z" fill="{fill}" stroke="#333"/><line x1="0" y1="-6" x2="0" y2="-10" stroke="#333"/></g>')
# tu dien, quat, cot dia, hop noi
o.append(f'<rect x="{X(14.21)-5:.1f}" y="{Y(7.45):.1f}" width="12" height="{0.5*S:.1f}" fill="#263238"/><text x="{X(14.21)+10:.0f}" y="{Y(7.2)+3:.0f}" font-weight="bold">TỦ ĐIỆN</text>')
o.append(f'<rect x="{X(11.85):.1f}" y="{Y(-0.3):.1f}" width="16" height="8" fill="#fff" stroke="#333"/><text x="{X(11.85):.0f}" y="{Y(-0.3)+18:.0f}">Công tơ</text>')
for b in (4.3,6.7):
    o.append(f'<g transform="translate({X(13.6):.1f},{Y(b):.1f})"><path d="M-7,0H7M-5,3H5M-3,6H3M0,-6V0" stroke="#7cb342" stroke-width="2"/></g>')
o.append(f'<text x="{X(13.6)-8:.0f}" y="{Y(5.5):.0f}" fill="#558b2f" text-anchor="end">2 cọc tiếp địa</text>')
o.append(f'<g transform="translate({X(11.3):.1f},{Y(11.2):.1f})"><circle r="9" fill="none" stroke="#333"/><path d="M0,0L8,-3M0,0L-6,6M0,0L-2,-8" stroke="#333" stroke-width="2"/></g><text x="{X(11.3)+12:.0f}" y="{Y(11.2)+4:.0f}">Quạt trần</text>')
o.append(f'<rect x="{X(9.35):.1f}" y="{Y(18.2):.1f}" width="14" height="6" fill="#78909c"/><text x="{X(9.35):.0f}" y="{Y(18.2)-3:.0f}">Quạt hút</text>')
o.append(f'<rect x="{X(8.15):.1f}" y="{Y(17.4):.1f}" width="{0.42*S:.1f}" height="{0.75*S:.1f}" fill="#fce4ec" stroke="#d81b60"/><text x="{X(8.6)+2:.0f}" y="{Y(17.0):.0f}" fill="#ad1457">Bình NL</text>')
o.append(f'<rect x="{X(12.5):.1f}" y="{Y(19.65):.1f}" width="{0.45*S:.1f}" height="{0.3*S:.1f}" fill="#bbdefb" stroke="#1565c0"/><text x="{X(12.5)-2:.0f}" y="{Y(19.65)-3:.0f}" text-anchor="end">Bơm giếng</text>')
o.append(f'<text x="{X(12.45):.0f}" y="{Y(-0.3)-10:.0f}" fill="#00838f">Đèn NLMT</text>')
# ghi chu thiet bi
notes=[('TV',17.7,7.05,'end',4),('Sofa',14.3,8.3,'start',4),('Bàn LV ×2',16.7,9.7,'middle',14),('Ổ máy lạnh 2,4m',17.0,12.1,'middle',16),('Đầu giường ×2',16.7,13.75,'middle',14),('Ổ tủ mạng (C4)',16.3,14.75,'middle',0),('Ổ kho',16.4,18.0,'middle',14),
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
CIRC=[('C1','MCB 1P 10A','1,5','Đèn 13 bóng + quạt trần + quạt hút WC',0.4,'MCB'),
      ('C2','MCB 1P 20A','2,5','Ổ cắm nhà chính: TV, sofa, bàn LV ×2, phòng ngủ ×3, kho',1.5,'MCB'),
      ('C3','MCB 1P 20A','2,5','Máy lạnh 1,5HP phòng ngủ',1.2,'MCB'),
      ('C4','MCB 1P 10A','1,5','Tủ mạng: UPS → PDU',0.15,'MCB'),
      ('R2','RCBO 2P 20A 30mA','2,5','Ổ bếp ×4: tủ lạnh, mặt bếp, hút mùi, đầu bàn + ổ BE6500 #2',2.2,'RCBO'),
      ('R3','MCB 1P 20A','2,5','Máy giặt + máy sấy (2 ổ đơn)',2.5,'RCCB'),
      ('R4','MCB 1P 20A','2,5','Bình nóng lạnh có sẵn (đấu cố định)',2.5,'RCCB'),
      ('R5','MCB 1P 16A','CVV 2×2,5','Ngoài trời: đèn hiên ×2, đèn pha, IP55 ×2, bơm giếng 0,75kW',1.1,'RCCB'),
      ('R1','RCBO 2P 32A (đợt 2)','4','Bếp từ đôi 3,5kW – đợt 1 chỉ ống chờ Ø25',3.5,'D2')]
sw_=34*len(CIRC)+40
g=[f'<svg viewBox="0 0 900 {sw_+170}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11">','<rect width="900" height="100%" fill="#fff"/>']
g.append('<rect x="10" y="20" width="90" height="34" fill="#fff" stroke="#333"/><text x="55" y="41" text-anchor="middle">Công tơ EVN</text>')
g.append('<path d="M100,37H150" stroke="#212121" stroke-width="3"/><text x="104" y="30" font-size="9">CVV 2×6 ~15m</text>')
g.append('<rect x="150" y="22" width="70" height="30" fill="#eceff1" stroke="#333"/><text x="185" y="35" text-anchor="middle" font-weight="bold">CB tổng</text><text x="185" y="47" text-anchor="middle">2P 40A</text>')
g.append('<path d="M220,37H250" stroke="#333" stroke-width="2"/><path d="M250,37V' + str(sw_) + '" stroke="#333" stroke-width="4"/>')
g.append('<path d="M236,37V70" stroke="#333"/><rect x="200" y="70" width="38" height="22" fill="#fff3e0" stroke="#333"/><text x="219" y="85" text-anchor="middle">SPD</text><path d="M219,92V108" stroke="#7cb342" stroke-width="2"/><text x="160" y="106" font-size="9" fill="#558b2f">→ thanh PE</text>')
y=60; rccb_y=None
for i,(c,cb,day,tai,kw,kind) in enumerate(CIRC):
    y=60+i*34
    x0=250
    if kind=='RCCB':
        if rccb_y is None:
            rccb_y=y
            g.append(f'<path d="M250,{y}H262" stroke="#333" stroke-width="2"/><rect x="262" y="{y-12}" width="92" height="24" fill="#e1f5fe" stroke="#0277bd"/><text x="308" y="{y+4}" text-anchor="middle" font-size="9.5">RCCB 2P 40A 30mA</text>')
            g.append(f'<path d="M360,{y}V{y+68}" stroke="#333" stroke-width="3"/>')
        x0=360
    else:
        g.append(f'<path d="M250,{y}H{x0+110 if False else 375}" stroke="#333" stroke-width="2"/>') if False else None
        g.append(f'<path d="M250,{y}H375" stroke="#333" stroke-width="2"/>')
        x0=375-0
    if kind=='RCCB': g.append(f'<path d="M360,{y}H375" stroke="#333" stroke-width="2"/>')
    dash=' stroke-dasharray="4 3"' if kind=='D2' else ''
    g.append(f'<rect x="375" y="{y-11}" width="120" height="22" fill="#fff" stroke="#333"{dash}/><text x="435" y="{y+4}" text-anchor="middle" font-size="10">{cb}</text>')
    g.append(f'<path d="M495,{y}H525" stroke="{COL[c]}" stroke-width="4"{dash}/><text x="530" y="{y-2}" font-weight="bold" fill="{COL[c]}">{c} · {day}mm²{' (đợt 2)' if kind=='D2' else ''}</text><text x="530" y="{y+11}" font-size="9.5" fill="#37474f">{html.escape(tai)}</text>')
yb=60+len(CIRC)*34
g.append(f'<text x="255" y="{yb}" font-size="10" fill="#607d8b">Dự phòng 2–3 module: nhà xe, bơm tăng áp, sân vườn (đợt 2)</text>')
g.append(f'<rect x="20" y="{yb+20}" width="230" height="24" fill="#f1f8e9" stroke="#7cb342"/><text x="135" y="{yb+36}" text-anchor="middle">Thanh PE (tiếp địa) trong tủ</text>')
g.append(f'<path d="M135,{yb+44}V{yb+80}" stroke="#7cb342" stroke-width="2" stroke-dasharray="5 3"/><text x="140" y="{yb+66}" font-size="9.5" fill="#558b2f">cáp đồng trần 16mm² ngầm 0,5m</text>')
for k in range(2):
    cx=105+60*k
    g.append(f'<path d="M{cx},{yb+80}V{yb+95}M{cx-12},{yb+95}H{cx+12}M{cx-8},{yb+100}H{cx+8}M{cx-4},{yb+105}H{cx+4}" stroke="#7cb342" stroke-width="2"/>')
g.append(f'<path d="M105,{yb+80}H165" stroke="#7cb342" stroke-width="2"/><text x="180" y="{yb+100}" font-size="9.5" fill="#558b2f">2 cọc đồng Ø16×2,4m cách 2,4m · đo &gt;10 Ω mới đóng cọc 3</text>')
g.append(f'<text x="290" y="{yb+36}" font-size="10" fill="#37474f">Mỗi mạch đi ống riêng từ tủ, đủ 3 dây L – N – PE. Tủ 12 module.</text>')
g.append('</svg>')
one='\n'.join(g)
# --- bang tinh
rows=[]
CNT={'C1':(0,8,10,'+ quạt trần, quạt hút WC'),'C2':(8,0,0,''),'C3':(1,0,0,'ổ đơn'),'C4':(1,0,0,'ổ đơn'),'R2':(5,0,0,''),'R3':(2,0,0,'ổ đơn'),'R4':(0,1,0,'CT 2 cực + hộp đấu kín'),'R5':(2,0,3,'IP55; + bơm giếng'),'R1':(1,0,0,'ổ 32A đợt 2')}
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
    day=0 if c=='R1' else math.ceil(ong*3+(ns+nw+nl)*0.6*3)
    rows.append((c,ong,day,ns,nw,nl,nt))
c1np=seglen_np('C1')
newwire=math.ceil(c1np*1.1*3)+sum(r[2] for r in rows if r[0] in('C3','C4','R2','R3','R4'))
info={'route':{k:round(v,1) for k,v in route.items()},'rows':rows,'c1np':round(c1np,1),'newwire':newwire}
json.dump(info,open('/tmp/dien_info.json','w'),ensure_ascii=False)
CI={c[0]:c for c in CIRC}
tb=['<table><tr><th>Mạch</th><th>Bảo vệ</th><th>Dây</th><th>Tải ước (kW)</th><th>Ống ~m</th><th>Dây ~m (L+N+PE)</th><th>Ổ</th><th>Công tắc</th><th>Đèn</th><th>Ghi chú</th></tr>']
tot=0
for c,ong,day,ns,nw,nl,nt in rows:
    _,cb,d,tai,kw,_=CI[c]; tot+=kw if c!='R1' else 0
    tb.append(f'<tr><td style="color:{COL[c]};font-weight:bold">{c}</td><td>{cb}</td><td>{d}</td><td>{str(kw).replace(".",",")}</td><td>{ong}</td><td>{day if day else "đợt 2"}</td><td>{ns}</td><td>{nw}</td><td>{nl}</td><td>{nt}</td></tr>')
tb.append('</table>')
tot_r=round(tot,2)
import sys
sys.path.insert(0,'/home/claude/nha-duyen-hai/tools')
from plan_common import nav
NAV=nav('dien.html')
page=f'''<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sơ đồ điện chi tiết – nhà Duyên Hải</title>
<style>body{{font-family:Arial,sans-serif;margin:0;padding:12px;color:#263238;max-width:1100px;margin:auto}}h1{{font-size:20px}}h2{{font-size:16px;margin-top:22px;border-bottom:2px solid #eceff1;padding-bottom:4px}}
svg{{width:100%;height:auto;border:1px solid #eceff1;border-radius:6px}}table{{border-collapse:collapse;width:100%;font-size:13px}}td,th{{border:1px solid #cfd8dc;padding:4px 6px;text-align:left}}th{{background:#eceff1}}
.lg span{{display:inline-block;margin:2px 10px 2px 0;font-size:13px}}.lg i{{display:inline-block;width:22px;height:4px;vertical-align:middle;margin-right:4px}}a{{color:#1565c0}}ul{{font-size:14px;line-height:1.5}}
@media print{{a.back{{display:none}}}}</style></head><body>
{NAV}
<h1>Sơ đồ điện chi tiết – nhà Duyên Hải (đợt 1, đã tối ưu)</h1>
<p style="font-size:14px">Cùng toạ độ với lớp <b>Điện</b> trong mô hình 3D. Nét liền: đi nổi trong nhà; nét đứt: đi ngầm hoặc ống chờ. Tỉ lệ thước 2m ở góc dưới.</p>
<div class="lg">{''.join(f'<span><i style="background:{COL[c]}"></i>{c}</span>' for c in ['C1','C2','C3','C4','R1','R2','R3','R4','R5'])}<span><i style="background:#212121"></i>Cáp nguồn</span><span><i style="background:#7cb342"></i>Tiếp địa PE</span></div>
<div class="lg" style="font-size:13px">Ký hiệu: ⊗ đèn · ● công tắc (cao 1,25m) · ◓ ổ cắm (cao 1,0m; xám đậm = IP55 ngoài trời; xám nhạt = ổ chờ đợt 2)</div>
<h2>1. Mặt bằng bố trí điện</h2>
{plan}
<h2>2. Sơ đồ nguyên lý tủ điện</h2>
{one}
<h2>3. Bảng tính theo mạch</h2>
{''.join(tb)}
<p style="font-size:13px">Tổng tải lắp đặt đợt 1 ≈ <b>{str(tot_r).replace(".",",")} kW</b> (chưa gồm bếp từ). Hệ số đồng thời ~0,6 → ≈ {str(round(tot_r*0.6,1)).replace(".",",")} kW ≈ <b>{round(tot_r*0.6*1000/220)}A</b>; <b style="color:#c62828">khi có bếp từ ≈ {round((tot_r+3.5)*0.6*1000/220)}A, vượt CB 40A</b> nếu bếp từ + máy sấy + nóng lạnh chạy cùng lúc (xem mục 5). Chiều dài ống đo theo tuyến 3D +10%; dây = ống × 3 lõi + 0,6m mỗi thiết bị. C1, C2 ở nhà chính giữ dây cũ đi nổi nên <b>dây mới chỉ cần ≈ {newwire} m</b> (C1 phần nhà phụ, C3, C4, R2, R3, R4), dùng dây có sẵn; R5 dùng cáp CVV 2×2,5 cho đoạn ngoài trời ≈ 18–20m.</p>
<h2>4. Quy cách thi công</h2>
<ul>
<li>Công tắc 1,25m cạnh mép cửa phía tay nắm; ổ cắm 1,0m (chừa nâng nền); bàn làm việc, mặt bếp 1,1m; giặt sấy 1,2m; máy lạnh 2,4m; ổ bếp từ dưới mặt bếp 0,6m.</li>
<li>Hộp công tắc 86 sâu, có dây N (để sau thay công tắc Zigbee). Màu dây: L đỏ/nâu, N xanh dương, PE vàng-xanh.</li>
<li>Nhà chính: dây cũ đang đi nổi – đo cách điện từng mạch ≥1 MΩ thì giữ cho C1, C2; dây mới đi ống nổi/nẹp sát trần, không đục tường.</li>
<li>Bình nóng lạnh: công tắc 2 cực có đèn ngoài cửa WC, đấu cố định qua hộp kín, PE nối vỏ bình, không đặt ổ cắm trong WC.</li>
<li>R5 ngoài trời: cáp CVV 2×2,5 đi nổi trên tường, chỉ chôn ~5m ra bơm trong ống HDPE sâu 0,5m. Đèn cổng dùng năng lượng mặt trời.</li>
<li>Kiểm tra trước khi đóng điện: bấm nút TEST trên RCCB và RCBO, đo điện trở đất, đo cách điện, thử đúng pha bằng ổ test 3 đèn.</li>
</ul>
<h2>5. Điểm cần chốt trước khi chôn cáp nguồn</h2>
<ul>
<li>Đợt 1 (chưa có bếp từ): tải đồng thời ≈ 32A → CB tổng 40A + cáp CVV 2×6 đủ.</li>
<li>Đợt 2 có bếp từ 3,5kW: nếu bếp từ + máy sấy + nóng lạnh chạy cùng lúc ≈ 41–43A → nhảy CB 40A. Cáp nguồn chôn ngầm, thay sau phải đào lại.</li>
<li><b>Đã chọn phương án A (vừa đủ dọn vào ở):</b> giữ 6mm² + CB 40A, quy ước không chạy máy sấy cùng lúc bếp từ (0đ).</li>
<li>Phương án B (không chọn lúc này): chôn luôn CVV 2×10mm² (~15m) + CB tổng 50A, thêm ước ≈ 0,7tr; trước đó xem dòng định mức trên công tơ EVN (ví dụ 10(40)A thì CB tổng không vượt 40A, phải xin nâng công tơ).</li>
</ul>
</body></html>'''
open('/home/claude/nha-duyen-hai/dien.html','w').write(page)
print(json.dumps(info,ensure_ascii=False))
