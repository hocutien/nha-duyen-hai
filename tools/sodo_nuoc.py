import json, math, sys
sys.path.insert(0,'/home/claude/nha-duyen-hai/tools')
from plan_common import *
s=src(); P=Plan(3.8,20.4,-1.4,26.2,46)
BLU,HOT,GRY,BRN,D2='#1e88e5','#ff5722','#616161','#6d4c41','#90a4ae'
P.walls(walls(s))
P.rooms([('PHÒNG KHÁCH',16.2,6.4),('PHÒNG NGỦ 1',16.6,12.6),('PHÒNG NGỦ 2',16.6,16.0),('BẾP – ĂN',10.6,9.6),('KHU GIẶT',13.0,15.6),('WC + TẮM',9.9,17.4),('SÂN TRƯỚC',12.5,4.5),('ĐƯỜNG',14,-1.0)])
# --- dot 2 (net dut, xam)
P.line([[9.4,2.2],[13.0,1.6],[18.0,1.9],[20.3,2.2]],'#0277bd',2,True);P.text('Đợt 2: thoát sân 2 hố thu + Ø114 → ao',17.5,1.9,'middle','#0277bd',-8)
for a,b in [(9.4,2.2),(13.0,1.6)]: P.rect(a-0.25,b-0.25,0.5,0.5,'#eceff1','#0277bd',True)
P.line([[7.75,11.25],[7.75,6.8],[8.3,6.8]],D2,2,True);P.text('Đợt 2: vòi rửa xe',8.3,6.8,'start',D2)
P.line([[13.4,18.75],[13.4,19.0]],D2,2,True);P.text('Đợt 2: vòi sân sau',13.45,18.75,'start',D2,-6)
P.circle(6.6,8.9,0.65*34,'none','#26a69a',True);P.text('Đợt 2: bồn nước mưa 2.000L',6.6,8.9,'middle','#26a69a',4)
P.rect(15.0,19.4,0.35,0.25,'#e3f2fd',D2,True);P.text('Đợt 2: bơm tăng áp',15.4,19.35,'start',D2,10)
P.circle(13.6,19.6,0.13*34,'#eceff1',D2,True);P.text('Cột lọc (chỉ khi nước phèn)',13.6,20.2,'middle',D2,-4)
# --- cap
P.circle(12.0,19.75,6,'#bbdefb',BLU);P.text('Giếng khoan',12.0,19.75,'end',BLU,4,-10)
P.rect(12.5,19.35,0.45,0.3,'#bbdefb');P.text('Bơm 0,75kW',12.7,19.35,'middle','#37474f',14)
P.line([[12.0,19.75],[12.5,19.5]],BLU,2.5)
P.line([[12.95,19.5],[13.6,19.6],[15.45,19.75],[15.75,19.95]],BLU,2.5)
P.circle(15.9,20.05,0.55*34,'#e3f2fd',BLU);P.text('Bồn inox 1.000L',15.9,20.05,'middle','#0d47a1',2,0,10,True);P.text('chân 2,5m · phao điện',15.9,20.05,'middle','#37474f',14)
P.line([[15.9,20.05],[15.35,19.55]],BLU,3);P.line([[15.0,19.5],[14.6,19.5],[14.6,18.75],[7.75,18.75],[7.75,11.25]],BLU,3)
P.text('Ống chính Ø27 chôn 0,3m (~18m)',10.0,18.85,'middle',BLU,-6)
br=[([[11.85,18.75],[11.85,18.38]],(11.85,18.38),'Máy giặt 1,0m','start'),([[12.55,18.75],[12.55,18.38]],(12.55,18.38),'Lavabo','start'),
    ([[7.75,11.25],[8.25,11.25]],(8.25,11.25),'Chậu bếp (van dưới chậu)','start'),
    ([[9.5,18.75],[8.22,18.75],[8.22,18.1],[8.22,17.55]],(8.22,17.55),'Van + van 1 chiều + van an toàn vào bình','start'),
    ([[8.22,18.1],[8.22,18.2],[8.95,18.2]],(8.95,18.2),'Bồn cầu + vòi xịt','start'),([[8.22,17.55],[8.22,16.15]],None,'','start')]
for pts,v,t,anc in br:
    P.line(pts,BLU,2)
    if v: P.circle(v[0],v[1],3.5,'#c62828','#c62828')
for t,a,b,anc,dy in [('Máy giặt 1,0m',11.85,18.38,'end',-6),('Lavabo',12.55,18.38,'start',14),('Chậu bếp',8.25,11.25,'start',4),('Van khoá + 1 chiều + an toàn',8.6,17.5,'start',4),('Bồn cầu',8.95,18.2,'start',4)]:
    P.text(t,a,b,anc,'#37474f',dy)
P.rect(8.15,16.65,0.42,0.75,'#fce4ec','#d81b60');P.text('Bình NL',8.6,17.0,'start','#ad1457',4)
P.line([[8.3,16.72],[8.22,16.15]],HOT,2.5);P.circle(8.2,16.05,4,'#b0bec5');P.text('Van trộn sen 1,1m',8.35,16.3,'start',HOT,-2)
# --- thoat nuoc xam
P.rect(8.25,11.05,0.3,0.4,'#cfd8dc');P.text('Bẫy mỡ',8.4,10.85,'start','#37474f',8)
P.line([[8.4,11.25],[7.55,11.25],[7.55,19.45]],GRY,2.5,True)
P.rect(7.25,19.45,0.6,0.6,'#424242');P.text('Hố lắng nước xám',7.2,19.75,'end','#212121',4)
P.line([[7.55,20.05],[6.8,25.5]],GRY,2.5,True);P.text('→ ra ao (Ø60, dốc ≥2%)',6.9,24.8,'start','#424242')
for a,b in [(13.0,17.3),(12.25,18.2),(8.75,16.0)]: P.rect(a-0.08,b-0.08,0.16,0.16,'#263238','#263238')
P.line([[13.0,17.3],[13.0,18.2],[12.25,18.2],[12.25,19.2],[7.85,19.75]],GRY,2,True);P.text('Phễu thu sàn giặt',13.0,17.3,'start','#424242',4)
P.line([[8.75,16.0],[10.6,16.0],[10.6,19.15],[7.85,19.7]],GRY,2,True);P.text('Phễu thu sàn tắm',8.85,16.0,'start','#424242',14)
P.line([[17.8,12.9],[18.15,12.9]],GRY,1.5);P.text('Nước ngưng máy lạnh',18.15,12.9,'start','#424242',4)
# --- nuoc den
P.line([[8.55,17.75],[7.3,17.75],[7.3,8.2],[9.2,7.3],[10.6,5.2]],BRN,3,True)
P.rect(7.0,7.9,0.6,0.6,'#6d4c41','#3e2723');P.text('Hố ga kiểm tra',7.0,8.2,'end','#3e2723',4)
P.rect(9.95,2.9,1.3,2.2,'#d7ccc8','#3e2723');P.text('Bể tự hoại 3 ngăn',10.6,4.3,'middle','#3e2723',0,0,10,True);P.text('cách giếng 15,9m',10.6,4.3,'middle','#3e2723',13)
P.line([[10.6,2.85],[10.6,1.0],[10.2,-0.6]],BRN,2,True);P.text('→ rãnh ven đường',10.2,-0.6,'start','#3e2723',4)
P.line([[11.1,4.9],[12.6,5.6],[13.88,6.0]],BRN,1.2);P.circle(13.88,6.0,3,'#8d6e63','#3e2723');P.text('Ống thông hơi Ø42 lên mái',13.88,6.0,'end','#3e2723',-6)
P.text('Ống xí Ø90 riêng, dốc ≥2%',7.3,12.5,'end',BRN,4)
plan=P.svg()
# --- so do nguyen ly
def bx(x,y,w,t1,t2='',fill='#e3f2fd',stroke='#1e88e5',dash=False):
    d=' stroke-dasharray="4 3"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="38" rx="6" fill="{fill}" stroke="{stroke}"{d}/><text x="{x+w/2}" y="{y+16}" text-anchor="middle" font-weight="bold">{t1}</text><text x="{x+w/2}" y="{y+30}" text-anchor="middle" font-size="9.5">{t2}</text>'
def ar(x1,y1,x2,y2,c='#1e88e5',dash=False): return f'<path d="M{x1},{y1}L{x2},{y2}" stroke="{c}" stroke-width="2"{" stroke-dasharray=\"4 3\"" if dash else ""} marker-end="url(#a)"/>'
g=['<svg viewBox="0 0 900 470" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11"><defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#555"/></marker></defs><rect width="900" height="470" fill="#fff"/>',
   '<text x="10" y="18" font-weight="bold" fill="#1565c0">CẤP NƯỚC</text>']
g+= [bx(10,30,100,'Giếng khoan','có sẵn'),ar(110,49,135,49),bx(135,30,105,'Bơm 0,75kW','bảo dưỡng phốt, tụ'),ar(240,49,262,49),
     bx(262,30,110,'Cột lọc','chỉ khi nước phèn','#eceff1','#90a4ae',True),ar(372,49,395,49),bx(395,30,120,'Bồn inox 1.000L','mua cũ · chân 2,5m'),
     ar(515,49,537,49),bx(537,30,105,'Van tổng Ø34','đoạn 5m'),ar(642,49,662,49),bx(662,30,110,'Bơm tăng áp','đợt 2 (nối thẳng)','#eceff1','#90a4ae',True),
     ar(772,49,790,49),bx(790,30,100,'Ống chính Ø27','ngầm 0,3m ~18m')]
x=60
for t1,t2,d in [('Máy giặt','van 1,0m',False),('Lavabo','van góc',False),('Bồn cầu','van + vòi xịt',False),('Bình nóng lạnh','van an toàn → dây mềm → sen',False),('Chậu bếp','van, chừa tê RO',False),('Vòi sân sau · rửa xe','đợt 2',True)]:
    g.append(bx(x,110,128,t1,t2,'#eceff1' if d else '#e3f2fd','#90a4ae' if d else '#1e88e5',d)); g.append(ar(840,68,x+64,110,'#90a4ae' if d else '#1e88e5',d)); x+=138
g.append('<text x="10" y="190" font-weight="bold" fill="#424242">THOÁT NƯỚC XÁM</text>')
g+= [bx(10,200,140,'Chậu bếp','bẫy mỡ inox dưới chậu','#f5f5f5','#616161'),bx(10,245,140,'Khu giặt','máy giặt + lavabo + phễu sàn','#f5f5f5','#616161'),bx(10,290,140,'Sàn tắm WC','phễu thu có bẫy mùi','#f5f5f5','#616161'),
     ar(150,219,240,262,'#616161'),ar(150,264,240,264,'#616161'),ar(150,309,240,266,'#616161'),bx(240,245,150,'Hố lắng chung','sau nhà, gạch + nắp BT','#e0e0e0','#424242'),ar(390,264,450,264,'#616161'),bx(450,245,120,'Ao','ống Ø60 dốc ≥2%','#e0f2f1','#00897b')]
g.append('<text x="10" y="365" font-weight="bold" fill="#5d4037">NƯỚC ĐEN (BỒN CẦU)</text>')
g+= [bx(10,375,120,'Bồn cầu','ống Ø90 riêng','#efebe9','#6d4c41'),ar(130,394,160,394,'#6d4c41'),bx(160,375,130,'Hố ga kiểm tra','góc rẽ','#efebe9','#6d4c41'),ar(290,394,320,394,'#6d4c41'),
     bx(320,375,170,'Bể tự hoại 3 ngăn','~2m³ · cách giếng 15,9m','#efebe9','#6d4c41'),ar(490,394,520,394,'#6d4c41'),bx(520,375,140,'Rãnh ven đường','nước sau bể','#efebe9','#6d4c41'),
     '<text x="680" y="390" font-size="10" fill="#5d4037">Ống thông hơi Ø42 từ bể lên</text><text x="680" y="403" font-size="10" fill="#5d4037">góc nhà chính, cao hơn mái 0,7m</text>']
g.append('<text x="600" y="210" font-size="10.5" fill="#455a64">Nước xám không vào bể tự hoại</text><text x="600" y="224" font-size="10.5" fill="#455a64">để bể không đầy nhanh.</text>')
g.append('</svg>')
one='\n'.join(g)
b9,t9=bom_table(['9. Nước cấp + thoát']); b2,t2=bom_table(['2. Bể tự hoại + ống thoát'])
page=f'''<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sơ đồ nước chi tiết – nhà Duyên Hải</title>{STYLE}</head><body>
{nav('nuoc.html')}
<h1>Sơ đồ cấp – thoát nước chi tiết (phương án vừa đủ dọn vào ở)</h1>
<p style="font-size:14px">Cùng toạ độ với lớp <b>Nước</b> trong mô hình 3D. Nét liền: cấp nước; nét đứt đậm: ống thoát chôn ngầm; <span class="d2">nét đứt xám: đợt 2</span>.</p>
<div class="lg"><span><i style="background:{BLU}"></i>Cấp lạnh</span><span><i style="background:{HOT}"></i>Nước nóng (dây cấp mềm)</span><span><i style="background:{GRY}"></i>Thoát nước xám</span><span><i style="background:{BRN}"></i>Nước đen → bể tự hoại</span><span><i style="background:#c62828;height:8px;width:8px;border-radius:4px"></i>Van khoá</span><span><i style="background:{D2}"></i>Đợt 2</span></div>
<h2>1. Phản biện trước khi vẽ – phần cắt cho vừa đủ</h2>
<ul>
<li>Giữ đủ chỗ dùng hằng ngày: bếp, WC + tắm nóng lạnh, máy giặt, lavabo; thoát nước xám riêng ra 1 hố lắng, nước đen ra bể tự hoại.</li>
<li>Cắt sang đợt 2: vòi rửa xe sân trước, vòi sân sau (ống chính Ø27 từ 30m còn ~18m, bớt 1 van) → <b>bớt ≈ 0,22tr</b>; bơm tăng áp, thoát sân Ø114, bồn nước mưa vẫn để đợt 2.</li>
<li>Không cắt: bồn trên chân 2,5m (mái nhà chính lợp tôn, không đặt bồn lên được; hạ bồn thì sen + bình nóng lạnh yếu áp), xét nghiệm nước giếng (nhà có bầu), van an toàn bình nóng lạnh.</li>
<li>Cột lọc chỉ lắp khi xét nghiệm báo phèn/sắt cao.</li>
</ul>
<h2>2. Mặt bằng cấp – thoát</h2>
{plan}
<h2>3. Sơ đồ nguyên lý</h2>
{one}
<h2>4. Vật tư đợt 1</h2>
<p><b>Mục 9 – Cấp + thoát nước</b></p>{b9}
<p><b>Mục 2 – Bể tự hoại + ống xí</b></p>{b2}
<p style="font-size:13px">Cộng 2 mục ≈ <b>{(t9+t2)/1000:.1f}tr</b> chưa VAT, dự phòng. Đợt 2 (bơm tăng áp, thoát sân Ø114, vòi rửa xe + sân sau, bồn nước mưa) xem bảng dự toán.</p>
<h2>5. Quy cách thi công</h2>
<ul>
<li>Ống cấp uPVC dán keo, chôn ≥0,3m, qua chỗ xe chạy thì lồng ống bảo vệ. Thử áp: bịt đầu, mở bồn, để 24 giờ không rò mới lấp.</li>
<li>Mỗi nhánh có van khoá riêng để sửa chỗ nào khoá chỗ đó.</li>
<li>Bình nóng lạnh: đầu nước lạnh vào lắp van khoá + van 1 chiều + van an toàn, ống xả van an toàn dẫn xuống phễu sàn, không bịt. Nóng xuống van trộn bằng dây cấp mềm inox.</li>
<li>Ống thoát dốc ≥2%, mỗi thiết bị có siphon/bẫy mùi; nước xám và nước đen đi riêng.</li>
<li>Bồn cũ: kiểm tra mối hàn, súc rửa bằng nước + chlorine trước khi dùng; neo chân bồn xuống đế bê tông.</li>
</ul></body></html>'''
open('/home/claude/nha-duyen-hai/nuoc.html','w').write(page); print('nuoc ok',round(t9),round(t2))
