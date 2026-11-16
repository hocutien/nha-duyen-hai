import re, json, math
SRC='/home/claude/nha3d.html'
def src(): return open(SRC).read()
def walls(s):
    out=[]
    for m in re.finditer(r"wall\('([xy])',([\d.]+),([\d.]+),([\d.]+),([\d.]+),[\d.]+,(\[.*?\]\]|\[\]),",s):
        ax,x0,y0,Ln,T=m.group(1),*map(float,m.groups()[1:5]); ops=json.loads(m.group(6))
        if not (7<x0<19 and 5<y0<19): continue
        out.append((ax,x0,y0,Ln,T,[o for o in ops if o[2]<0.1]))
    return out
class Plan:
    def __init__(s,A0,A1,B0,B1,S):
        s.A0,s.A1,s.B0,s.B1,s.S=A0,A1,B0,B1,S; s.o=[]
        s.W,s.H=s.X(A1),s.Y(B0)
    def X(s,a): return (a-s.A0)*s.S
    def Y(s,b): return (s.B1-b)*s.S
    def add(s,t): s.o.append(t)
    def walls(s,ws):
        S=s.S
        for ax,x0,y0,Ln,T,ops in ws:
            segs=[];cur=0
            for s0,s1,_,_ in sorted(ops): segs.append((cur,s0)); cur=s1
            segs.append((cur,Ln))
            for a,b in segs:
                if b-a<=0: continue
                if ax=='x': s.add(f'<rect x="{s.X(x0+a):.1f}" y="{s.Y(y0+T):.1f}" width="{(b-a)*S:.1f}" height="{max(T*S,3):.1f}" fill="#9e9e9e"/>')
                else: s.add(f'<rect x="{s.X(x0):.1f}" y="{s.Y(y0+b):.1f}" width="{max(T*S,3):.1f}" height="{(b-a)*S:.1f}" fill="#9e9e9e"/>')
    def rooms(s,lst):
        for t,a,b in lst: s.add(f'<text x="{s.X(a):.0f}" y="{s.Y(b):.0f}" fill="#bdbdbd" font-size="11" font-weight="bold" text-anchor="middle">{t}</text>')
    def line(s,pts,col,w=2,dash=False):
        p=' '.join(f'{s.X(q[0]):.1f},{s.Y(q[1]):.1f}' for q in pts)
        s.add(f'<polyline points="{p}" fill="none" stroke="{col}" stroke-width="{w}"{" stroke-dasharray=\"5 3\"" if dash else ""} stroke-linejoin="round"/>')
    def text(s,t,a,b,anc='start',col='#37474f',dy=4,dx=None,size=10,bold=False):
        if dx is None: dx=10 if anc=='start' else (-10 if anc=='end' else 0)
        s.add(f'<text x="{s.X(a)+dx:.0f}" y="{s.Y(b)+dy:.0f}" text-anchor="{anc}" fill="{col}" font-size="{size}"{" font-weight=\"bold\"" if bold else ""}>{t}</text>')
    def rect(s,a,b,w,d,fill,stroke='#333',dash=False):
        s.add(f'<rect x="{s.X(a):.1f}" y="{s.Y(b+d):.1f}" width="{w*s.S:.1f}" height="{d*s.S:.1f}" fill="{fill}" stroke="{stroke}"{" stroke-dasharray=\"4 3\"" if dash else ""}/>')
    def circle(s,a,b,r,fill,stroke='#333',dash=False):
        s.add(f'<circle cx="{s.X(a):.1f}" cy="{s.Y(b):.1f}" r="{r}" fill="{fill}" stroke="{stroke}"{" stroke-dasharray=\"3 2\"" if dash else ""}/>')
    def svg(s,north=True):
        S=s.S
        extra=[f'<g transform="translate(20,{s.H-20:.0f})"><path d="M0,0H{2*S}" stroke="#333" stroke-width="2"/><path d="M0,-4V4M{S},-3V3M{2*S},-4V4" stroke="#333"/><text x="{S}" y="-7" text-anchor="middle">2 m</text></g>']
        if north: extra.append(f'<g transform="translate({s.W-40:.0f},40)"><path d="M0,14L0,-14M0,-14L-5,-4M0,-14L5,-4" stroke="#333" stroke-width="2"/><text y="28" text-anchor="middle">Sau nhà</text></g>')
        return f'<svg viewBox="0 0 {s.W:.0f} {s.H:.0f}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="10"><style>text{{paint-order:stroke;stroke:#fff;stroke-width:3px;stroke-linejoin:round}}</style><rect width="{s.W:.0f}" height="{s.H:.0f}" fill="#fff"/>'+'\n'.join(s.o+extra)+'</svg>'
def dist(pts): return sum(math.dist(pts[i],pts[i+1]) for i in range(len(pts)-1))
STYLE='''<style>body{font-family:Arial,sans-serif;margin:0;padding:12px;color:#263238;max-width:1100px;margin:auto}h1{font-size:20px}h2{font-size:16px;margin-top:22px;border-bottom:2px solid #eceff1;padding-bottom:4px}
svg{width:100%;height:auto;border:1px solid #eceff1;border-radius:6px}table{border-collapse:collapse;width:100%;font-size:13px}td,th{border:1px solid #cfd8dc;padding:4px 6px;text-align:left}th{background:#eceff1}
.lg span{display:inline-block;margin:2px 10px 2px 0;font-size:13px}.lg i{display:inline-block;width:22px;height:4px;vertical-align:middle;margin-right:4px}a{color:#1565c0}ul{font-size:14px;line-height:1.5}
.d2{color:#78909c}@media print{a.back{display:none}}</style>'''
def nav(cur):
    items=[('dien.html','⚡ Điện'),('nuoc.html','💧 Nước'),('mang.html','🌐 Mạng')]
    return '<p><a class="back" href="./">← Mô hình 3D</a> · '+' · '.join(f'<b>{t}</b>' if h==cur else f'<a href="{h}">{t}</a>' for h,t in items)+'</p>'
def bom_table(groups,phase1=True):
    R=json.load(open('/home/claude/nha-duyen-hai/tools/out/dutoan.json'))
    rows=[x for x in R if x[0] in groups]
    t=['<table><tr><th>Cấu thành</th><th>KL</th><th>ĐVT</th><th>Đơn giá (nghìn)</th><th>Thành tiền (nghìn)</th><th>Loại</th><th>Ghi chú</th></tr>']
    tot=0
    for x in rows:
        tot+=x[8]
        t.append(f'<tr><td>{x[1]}</td><td>{str(x[3]).replace(".",",")}</td><td>{x[2]}</td><td>{f"{x[4]:,.0f}".replace(",",".")}</td><td>{f"{x[8]:,.0f}".replace(",",".")}</td><td>{x[5]}</td><td>{x[7]}</td></tr>')
    t.append(f'<tr><th colspan="4">Cộng (chưa VAT)</th><th>{f"{tot:,.0f}".replace(",",".")}</th><th colspan="2"></th></tr></table>')
    return '\n'.join(t),tot
