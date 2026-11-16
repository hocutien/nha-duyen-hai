import sys
sys.path.insert(0,'/home/claude/nha-duyen-hai/tools')
from plan_common import *
s=src(); P=Plan(5.0,22.4,-1.4,22.2,44)
NET,FIB,D2,UG='#3949ab','#ff7043','#b0bec5','#1a237e'
P.walls(walls(s))
P.rooms([('PHÒNG KHÁCH',16.2,6.4),('PHÒNG NGỦ',16.6,12.6),('KHO',16.6,16.9),('HÀNH LANG',14.8,16.0),('BẾP – ĂN',10.6,9.6),('KHU GIẶT',13.0,15.6),('WC',9.9,17.4),('SÂN TRƯỚC',11.0,4.5),('CỔNG',12.0,-1.1)])
# dot 2
P.line([[15.25,8.6],[14.25,8.6],[8.1,8.6],[8.1,7.56],[7.95,7.56]],D2,2,True);P.rect(7.7,7.5,0.3,0.12,'#eceff1',D2,True);P.text('Đợt 2 · 13 hộp B sân xe (camera)',7.7,7.3,'start','#78909c',12,0)
P.line([[15.25,18.1],[16.4,18.1],[16.4,18.55]],D2,2,True);P.rect(16.25,18.5,0.3,0.12,'#eceff1',D2,True);P.text('Đợt 2 · 14–15 hộp C hiên sau (camera, AP vườn)',16.2,18.9,'middle','#78909c',-4)
P.line([[16.4,18.56],[16.4,21.8]],D2,2,True);P.text('Đợt 2 · ống HDPE ra hộp D bờ sông',16.5,21.0,'start','#78909c')
P.line([[17.45,14.3],[17.45,13.95],[16.85,13.95],[16.85,9.96]],D2,2,True);P.text('Đợt 2 · ống Ø25 trống tới bàn',18.1,11.5,'start','#78909c',0,8)
P.line([[15.25,13.5],[14.95,13.5]],D2,2,True);P.text('02 Zigbee (đợt 2)',14.9,13.5,'end','#78909c',4)
P.circle(17.5,14.4,4,'#eceff1',D2,True);P.text('Ống lên mái (đợt 2)',18.1,15.4,'start','#78909c',0,8)
# cap quang
P.line([[13.45,-1.4],[14.05,5.45],[14.3,5.75],[15.2,5.75],[15.2,14.25],[17.25,14.25]],FIB,1.6)
P.text('Cáp quang nhà mạng kéo treo từ cột vào góc nhà → ONT trong tủ mạng',13.6,1.0,'start',FIB,0)
# truc + nhanh dot 1
P.line([[17.3,14.3],[15.25,14.3]],NET,4);P.line([[15.25,5.85],[15.25,18.1]],NET,4)
P.text('Trục Ø32 đi nổi sát trần hành lang',15.1,16.8,'end',NET,4,-6,10,True)
drops=[([[15.25,12.5],[14.85,12.5]],(14.85,12.5),'01 AP-325 trần (cáp bấm RJ45)','end','ap'),
       ([[15.25,7.35],[17.76,7.35]],(17.76,7.35),'03–04 TV + BE6500 #1','end','rj'),
       ([[15.25,9.9],[16.6,9.9],[16.6,9.96]],(16.6,9.96),'05–06 bàn làm việc','middle','rj'),
       ([[17.05,14.3],[16.7,14.3],[16.7,14.06]],(16.7,14.06),'07–08 phòng ngủ','middle','rj'),
       ([[15.25,11.0],[14.25,11.0],[13.96,11.0]],(13.96,11.0),'09–10 BE6500 #2 (kệ 2m) + dự phòng','end','rj')]
for pts,pt,t,anc,k in drops:
    P.line(pts,NET,2)
    if k=='ap': P.circle(pt[0],pt[1],8,'#fafafa',NET)
    else: P.rect(pt[0]-0.07,pt[1]-0.07,0.14,0.14,'#e8eaf6',NET)
P.text('01 AP-325 trần',14.6,12.5,'end',NET,4)
P.text('03–04 TV + BE6500 #1',17.6,7.35,'end',NET,-6)
P.text('05–06 bàn làm việc',16.6,9.7,'middle',NET,12)
P.text('07–08 phòng ngủ',16.7,13.85,'middle',NET,14)
P.text('09–10 BE6500 #2 + dự phòng',13.8,11.0,'end',NET,4)
P.line([[15.25,5.85],[14.25,5.85],[13.85,5.85],[11.8,-0.2]],UG,2.5,True);P.rect(11.72,-0.28,0.16,0.16,'#424242')
P.text('11–12 ống HDPE Ø32 ngầm ra cổng (chung rãnh cáp nguồn, bịt nắp)',12.2,2.4,'start',UG,4)
P.rect(17.05,14.25,0.5,0.49,'#8d6e63','#4e342e');P.text('TỦ MẠNG (kho)',18.1,14.6,'start','#4e342e',0,8,10,True)
P.text('ONT · hEX · switch',18.1,14.6,'start','#4e342e',13,8);P.text('M720q · NAS · UPS',18.1,14.6,'start','#4e342e',26,8)
plan=P.svg()
# --- so do logic
def bx(x,y,w,t1,t2='',fill='#e8eaf6',stroke='#3949ab',dash=False,h=38):
    d=' stroke-dasharray="4 3"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}"{d}/><text x="{x+w/2}" y="{y+16}" text-anchor="middle" font-weight="bold">{t1}</text><text x="{x+w/2}" y="{y+30}" text-anchor="middle" font-size="9.5">{t2}</text>'
def ln(x1,y1,x2,y2,c='#3949ab',dash=False,lab=''):
    t=f'<path d="M{x1},{y1}L{x2},{y2}" stroke="{c}" stroke-width="2"{" stroke-dasharray=\"4 3\"" if dash else ""}/>'
    if lab: t+=f'<text x="{(x1+x2)/2+4}" y="{(y1+y2)/2-4}" font-size="9.5" fill="#455a64">{lab}</text>'
    return t
g=['<svg viewBox="0 0 900 430" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11"><rect width="900" height="430" fill="#fff"/>']
g+= [bx(20,20,130,'Cáp quang nhà mạng','kéo treo, miễn phí','#fbe9e7','#ff7043'),ln(150,39,190,39,'#ff7043'),bx(190,20,110,'ONT','đặt trong tủ mạng'),
     ln(300,39,350,39,lab='ether1 WAN'),bx(350,20,150,'MikroTik hEX','router · DHCP · AdGuard DNS'),
     bx(560,20,140,'4G dự phòng','ether4 · khi cần','#eceff1','#90a4ae',True),ln(500,39,560,39,'#90a4ae',True),
     ln(380,58,180,120,lab='ether2'),ln(425,58,425,120,lab='ether3'),ln(470,58,690,120,lab='ether5'),
     bx(100,120,170,'Cục cấp nguồn PoE+ (802.3at)','dùng đồ có sẵn; chưa có thì đợt 2','#fff8e1','#f9a825'),ln(185,158,185,190),bx(110,190,150,'01 Aruba AP-325','trần hành lang · SSID theo VLAN'),
     bx(340,120,170,'Switch thường có sẵn','≥8 cổng · VLAN 20'),bx(610,120,170,'09 BE6500 #2 (AP)','nhà phụ, dây về tủ'),ln(690,158,690,190),bx(620,190,150,'10 dự phòng','cáp chờ ở bếp','#eceff1','#90a4ae',True)]
x=20
for t1,t2 in [('DS220j + WD','trong tủ'),('M720q','Proxmox · HA'),('03 BE6500 #1','TV cắm LAN của BE6500'),('05–06 bàn làm việc','2 cổng'),('07–08 phòng ngủ','1 dùng, 1 dự phòng')]:
    g.append(ln(425,158,x+75,260)); g.append(bx(x,260,150,t1,t2)); x+=170
g+= [bx(20,330,260,'Đợt 2: switch PoE TL-SG2210MP / CSS610','gom AP-325, Zigbee, camera, AP vườn','#eceff1','#90a4ae',True),
     bx(300,330,260,'Đợt 2: tủ gỗ 12U + patch panel 24 cổng','đợt 1 cáp cuộn chờ, đánh số 2 đầu','#eceff1','#90a4ae',True),
     bx(580,330,300,'Đợt 2: camera cổng (11–12), sân xe (13), hiên sau (14)','+ AP vườn (15), hộp D bờ sông (16)','#eceff1','#90a4ae',True)]
g.append('</svg>')
topo='\n'.join(g)
pt=['<table><tr><th>Số</th><th>Đầu kia</th><th>Cắm vào (đợt 1)</th><th>Ghi chú</th></tr>']
for r in [('01','Trần hành lang – Aruba AP-325','hEX ether2 qua cục PoE+','Không có cục PoE+ thì để đợt 2, 2 BE6500 vẫn phủ nhà'),('02','Trần hành lang – Zigbee PoE','–','Đợt 2; đợt 1 dùng USB Zigbee cắm M720q'),
          ('03','Phòng khách – BE6500 #1','Switch thường','TV cắm cổng LAN của BE6500, khỏi kéo thêm'),('04','Phòng khách – dự phòng','–','Cáp có sẵn, chờ'),
          ('05–06','Bàn làm việc','Switch thường',''),('07','Phòng ngủ','Switch thường',''),('08','Phòng ngủ – dự phòng','–',''),
          ('09','Bếp – BE6500 #2','hEX ether5','Nguồn từ ổ R2 cạnh kệ'),('10','Bếp – dự phòng','–',''),('11–12','Ống ngầm ra cổng','–','Chỉ ống + dây mồi, bịt nắp; camera đợt 2')]:
    pt.append('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>')
pt.append('</table>')
b8,t8=bom_table(['8. Mạng + ống chờ']); bD,tD=bom_table(['Đợt 2 – Tủ mạng gỗ tự đóng + thiết bị mạng'])
page=f'''<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sơ đồ mạng chi tiết – nhà Duyên Hải</title>{STYLE}</head><body>
{nav('mang.html')}
<h1>Sơ đồ mạng chi tiết (phương án vừa đủ dọn vào ở)</h1>
<p style="font-size:14px">Cùng toạ độ với lớp <b>Mạng</b> trong mô hình 3D. Nét đậm: trục ống Ø32; nét mảnh: nhánh Ø20; nét đứt xanh đậm: ống ngầm; <span class="d2">nét đứt xám: đợt 2</span>.</p>
<div class="lg"><span><i style="background:{NET}"></i>Cáp mạng đợt 1</span><span><i style="background:{FIB}"></i>Cáp quang</span><span><i style="background:{UG}"></i>Ống ngầm ra cổng</span><span><i style="background:{D2}"></i>Đợt 2</span></div>
<h2>1. Phản biện trước khi vẽ – phần cắt cho vừa đủ</h2>
<ul>
<li>Mọi ống mạng trong nhà đều <b>đi nổi</b>, sau này thêm không phải đục tường → đợt 1 chỉ kéo những đường dùng ngay: wifi 2 BE6500 (nối dây), điểm phát trên trần, TV, bàn làm việc, phòng ngủ.</li>
<li>Việc phải làm ngay dù chưa dùng: <b>ống HDPE ra cổng</b>, vì chôn chung rãnh cáp nguồn đang đào; để sau phải đào lại.</li>
<li>Dời sang đợt 2: ống Ø25 trống tới bàn, nhánh hộp B, C, ống lên mái, 2 ống qua mí lộ, hộp IP66, dây đồng 6mm² tới tủ mạng (chỉ cần khi lắp chống sét mạng) → mục Mạng từ 1,72tr còn <b>{t8/1000:.2f}tr</b>.</li>
<li>Thiết bị dùng đồ có sẵn: hEX, switch thường, 2 BE6500, AP-325, NAS, M720q, UPS, cáp CAT6, hạt mạng. TV cắm LAN của BE6500 #1 nên switch thường 8 cổng là đủ.</li>
</ul>
<h2>2. Mặt bằng đi cáp</h2>
{plan}
<h2>3. Sơ đồ kết nối đợt 1</h2>
{topo}
<h2>4. Bảng cổng (dán nhãn số ở 2 đầu cáp)</h2>
{''.join(pt)}
<h2>5. Vật tư</h2>
<p><b>Đợt 1 – Mục 8</b></p>{b8}
<p><b>Đợt 2 – tủ mạng gỗ + thiết bị</b></p>{bD}
<h2>6. Quy cách thi công</h2>
<ul>
<li>Ống mạng cách dây điện ≥30cm, không đi chung ống; chỗ cắt ngang dây điện thì cắt vuông góc.</li>
<li>Bấm đầu T568B cả hai đầu; test từng đường bằng máy test cáp, đạt 1Gbps mới đóng mặt ổ.</li>
<li>Đợt 1 chưa có tủ: ONT, hEX, switch, NAS, M720q đặt trên kệ sắt trong kho (không đặt trên nóc tủ lạnh), UPS cắm ổ C4.</li>
<li>2 BE6500 chế độ AP, nối dây về switch; cùng tên wifi + mật khẩu; kênh 5GHz khác nhau.</li>
</ul></body></html>'''
open('/home/claude/nha-duyen-hai/mang.html','w').write(page); print('mang ok',round(t8),round(tD))
