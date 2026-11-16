import json, math, sys
sys.path.insert(0,'/home/claude/nha-duyen-hai/tools')
from plan_common import *
s=src(); P=Plan(0.2,22.6,-1.4,21.4,46)
BLU,HOT,GRY,BRN,D2='#1e88e5','#e53935','#757575','#424242','#90a4ae'
P.walls(walls(s))
P.rooms([('PHÒNG KHÁCH',16.2,6.4),('PHÒNG NGỦ 1',16.6,12.6),('PHÒNG NGỦ 2',16.6,16.0),('BẾP – ĂN',10.6,9.6),('KHU GIẶT',13.0,15.6),('WC + TẮM',9.9,17.4),('SÂN TRƯỚC',12.5,4.5),('ĐƯỜNG',14,-1.0)])
# --- dot 2 (net dut, xam)
P.line([[13.0,2.2],[18.3,2.2],[20.3,2.3]],'#b0bec5',2,True);P.text('Đợt 2: chỉ nước mưa ra ao (hố thu + Ø114)',19.0,2.2,'middle','#78909c',-8)
P.rect(12.75,1.95,0.5,0.5,'#eceff1','#b0bec5',True)
P.line([[7.75,11.25],[7.75,6.8],[8.3,6.8]],BLU,2.5);P.circle(8.3,6.8,3.5,'#212121','#212121');P.rect(7.95,6.1,0.8,0.6,'#e0e0e0','#757575');P.rect(8.27,6.32,0.16,0.16,'#263238','#263238');P.line([[8.35,6.4],[7.3,6.4]],GRY,2,True);P.text('Vòi rửa tay chân',7.85,6.5,'end','#0d47a1',0,-6,10,True);P.text('+ bệ rửa chân, rửa xe',7.85,6.5,'end','#0d47a1',13,-6)
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
P.text('Ống chính Ø27 chôn 0,3m (~23m)',10.0,18.85,'middle',BLU,-6)
br=[([[11.85,18.75],[11.85,18.38]],(11.85,18.38),'Máy giặt 1,0m','start'),([[12.55,18.75],[12.55,18.38]],(12.55,18.38),'Lavabo','start'),
    ([[7.75,11.25],[8.25,11.25]],(8.25,11.25),'Chậu bếp (van dưới chậu)','start'),
    ([[9.5,18.75],[8.22,18.75],[8.22,18.1],[8.22,17.55]],(8.22,17.55),'Van + van 1 chiều + van an toàn vào bình','start'),
    ([[8.22,18.1],[8.22,18.2],[8.95,18.2]],(8.95,18.2),'Bồn cầu + vòi xịt','start'),([[8.22,17.55],[8.22,16.15]],None,'','start')]
for pts,v,t,anc in br:
    P.line(pts,BLU,2)
    if v: P.circle(v[0],v[1],3.5,'#212121','#212121')
for t,a,b,anc,dy in [('Máy giặt 1,0m',11.85,18.38,'end',-6),('Lavabo',12.55,18.38,'start',14),('Chậu rửa chén',8.25,11.25,'start',4),('Van khoá + 1 chiều + an toàn',8.6,17.5,'start',4),('Bồn cầu',8.95,18.2,'start',4)]:
    P.text(t,a,b,anc,'#37474f',dy)
P.rect(8.15,16.65,0.42,0.75,'#fce4ec','#d81b60');P.text('Bình NL',8.6,17.0,'start','#ad1457',4)
P.line([[8.3,16.72],[8.22,16.15]],HOT,2.5);P.circle(8.2,16.05,4,'#b0bec5');P.text('Van trộn sen 1,1m',8.35,16.3,'start',HOT,-2)
# --- thoat: nuoc xam + nuoc den -> be tu hoai co ngan loc truoc hien nha chinh -> ranh tham
P.rect(8.25,11.05,0.3,0.4,'#cfd8dc');P.text('Bẫy mỡ',8.4,10.85,'start','#37474f',8)
P.line([[8.4,11.25],[7.55,11.25]],GRY,2,True)
P.line([[7.55,19.2],[7.55,8.05],[7.3,8.05]],GRY,2.5,True);P.text('Nước xám Ø60 →',7.5,14.0,'end',GRY,4)
for a,b in [(13.0,17.3),(12.25,18.2),(8.75,16.0)]: P.rect(a-0.08,b-0.08,0.16,0.16,'#263238','#263238')
P.line([[13.0,17.3],[13.0,18.2],[12.25,18.2],[12.25,19.2],[7.55,19.2]],GRY,2,True);P.text('Phễu thu sàn giặt',13.0,17.3,'start','#424242',4)
P.line([[8.75,16.0],[7.55,16.0]],GRY,2,True);P.text('Phễu thu sàn tắm',8.85,16.0,'start','#424242',14)
P.line([[17.8,12.9],[18.15,12.9]],GRY,1.5);P.text('Nước ngưng máy lạnh',18.15,12.9,'start','#424242',4)
P.line([[8.55,17.75],[7.3,17.75],[7.3,8.05],[7.3,1.15],[14.8,1.15]],BRN,3,True);P.text('Ống chính Ø90 (đen + xám) dốc ≥2%',7.2,4.5,'end',BRN,4)
P.rect(7.0,7.75,0.6,0.6,'#616161','#212121');P.text('Hố ga: xám nhập Ø90',6.95,8.05,'end','#212121',4)
P.rect(7.2,1.05,0.2,0.2,'#616161','#212121');P.text('Tê kiểm tra',7.45,1.15,'start','#212121',-8)
P.line([[7.6,0.6],[7.3,1.0]],GRY,2,True);P.text('Rửa xe: bẫy dầu-cát',8.0,0.45,'start','#424242',-4)
P.rect(14.8,0.55,2.3,1.2,'#cfd8dc','#263238');P.text('Bể 2.000L có ngăn lọc',15.95,1.15,'middle','#263238',0,None,10,True);P.text('cách giếng ~19m',15.95,1.15,'middle','#263238',13)
P.line([[17.1,1.15],[17.45,1.15],[17.45,0.3],[7.6,0.3],[7.6,0.8]],BRN,2,True);P.rect(17.3,0.15,0.35,0.3,'#212121','#212121');P.text('Nắp lật 1 chiều',17.7,0.3,'start','#212121',4)
P.rect(0.6,0.55,7.0,0.5,'#e8e4d4','#8d8a7a');P.line([[7.6,0.8],[0.6,0.8]],BRN,2,True);P.text('Rãnh thấm 7m dọc rào trước · cách ao ≥15m',3.6,0.8,'middle','#424242',-12)
P.line([[15.3,1.15],[14.0,2.35]],BRN,1.2);P.circle(13.9,2.35,3,'#9e9e9e','#424242');P.text('Ống thông hơi Ø42 dọc cột hiên',13.85,2.35,'end','#424242',-6)
plan=P.svg()
# --- so do nguyen ly
def bx(x,y,w,t1,t2='',fill='#e3f2fd',stroke='#1e88e5',dash=False):
    d=' stroke-dasharray="4 3"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="38" rx="6" fill="{fill}" stroke="{stroke}"{d}/><text x="{x+w/2}" y="{y+16}" text-anchor="middle" font-weight="bold">{t1}</text><text x="{x+w/2}" y="{y+30}" text-anchor="middle" font-size="9.5">{t2}</text>'
def ar(x1,y1,x2,y2,c='#1e88e5',dash=False): return f'<path d="M{x1},{y1}L{x2},{y2}" stroke="{c}" stroke-width="2"{" stroke-dasharray=\"4 3\"" if dash else ""} marker-end="url(#a)"/>'
g=['<svg viewBox="0 0 900 490" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11"><defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#555"/></marker></defs><rect width="900" height="500" fill="#fff"/>',
   '<text x="10" y="18" font-weight="bold" fill="#1565c0">CẤP NƯỚC</text>']
g+= [bx(10,30,100,'Giếng khoan','có sẵn'),ar(110,49,135,49),bx(135,30,105,'Bơm 0,75kW','bảo dưỡng phốt, tụ'),ar(240,49,262,49),
     bx(262,30,110,'Cột lọc','chỉ khi nước phèn','#eceff1','#90a4ae',True),ar(372,49,395,49),bx(395,30,120,'Bồn inox 1.000L','mua cũ · chân 2,5m'),
     ar(515,49,537,49),bx(537,30,105,'Van tổng Ø34','đoạn 5m'),ar(642,49,662,49),bx(662,30,110,'Bơm tăng áp','đợt 2 (nối thẳng)','#eceff1','#90a4ae',True),
     ar(772,49,790,49),bx(790,30,100,'Ống chính Ø27','ngầm 0,3m ~23m')]
x=60
for t1,t2,d in [('Máy giặt','van 1,0m',False),('Lavabo','van góc',False),('Bồn cầu','van + vòi xịt',False),('Bình nóng lạnh','van an toàn → dây mềm → sen',False),('Chậu rửa chén','van, chừa tê RO',False),('Vòi trước nhà','rửa tay chân + rửa xe',False)]:
    g.append(bx(x,110,128,t1,t2,'#eceff1' if d else '#e3f2fd','#90a4ae' if d else '#1e88e5',d)); g.append(ar(840,68,x+64,110,'#90a4ae' if d else '#1e88e5',d)); x+=138
g.append('<text x="10" y="190" font-weight="bold" fill="#424242">THOÁT NƯỚC THẢI (không xả ra ao, không xả ra sông)</text>')
G2='#757575'
g+= [bx(10,200,150,'Chậu bếp','bẫy mỡ inox dưới chậu','#f5f5f5',G2),bx(10,243,150,'Khu giặt + lavabo','phễu sàn có bẫy mùi','#f5f5f5',G2),bx(10,286,150,'Sàn tắm WC','phễu thu có bẫy mùi','#f5f5f5',G2),bx(10,329,150,'Bệ rửa chân, rửa xe','bẫy dầu-cát','#f5f5f5',G2),
     ar(160,219,215,262,G2),ar(160,262,215,264,G2),ar(160,305,215,266,G2),ar(160,348,215,268,G2),bx(215,245,120,'Ống xám Ø60','dốc ≥2%','#f5f5f5',G2),ar(335,264,375,330,G2),
     bx(10,400,150,'Bồn cầu','ống Ø90 dán keo kín','#eeeeee','#424242'),ar(160,419,375,354,'#424242'),
     bx(375,323,120,'Hố ga','nhập chung Ø90','#eeeeee','#424242'),ar(495,342,520,342,'#424242'),
     bx(520,315,150,'Bể tự hoại 2.000L','có ngăn lọc vi sinh','#cfd8dc','#263238'),ar(595,353,595,380,'#424242'),
     bx(530,380,130,'Nắp lật 1 chiều','chống triều đẩy ngược','#eeeeee','#212121'),ar(595,418,595,440,'#424242'),
     bx(510,440,170,'Rãnh thấm 7m','dọc rào trước, cách ao ≥15m','#e8e4d4','#8d8a7a'),
     bx(700,200,180,'Nước mưa mái, sân','ra ao riêng (sạch)','#eceff1','#b0bec5',True),
     '<text x="700" y="330" font-size="10" fill="#455a64">Bể trước hiên nhà chính,</text><text x="700" y="344" font-size="10" fill="#455a64">cách giếng ~19m; đáy BT lót +</text><text x="700" y="358" font-size="10" fill="#455a64">2 đai neo chống nổi; hút bùn</text><text x="700" y="372" font-size="10" fill="#455a64">2–3 năm, lúc triều ròng.</text>']
g.append('</svg>')
one='\n'.join(g)
b9,t9=bom_table(['9. Nước cấp + thoát']); b2,t2=bom_table(['2. Bể tự hoại + ống thoát'])
page=f'''<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sơ đồ nước chi tiết – nhà Duyên Hải</title>{STYLE}</head><body>
{nav('nuoc.html')}
<h1>Sơ đồ cấp – thoát nước chi tiết (phương án vừa đủ dọn vào ở)</h1>
<p style="font-size:14px">Cùng toạ độ với lớp <b>Nước</b> trong mô hình 3D. Nét liền: cấp nước; nét đứt đậm: ống thoát chôn ngầm; <span class="d2">nét đứt xám: đợt 2</span>.</p>
<div class="lg"><span><i style="background:{BLU}"></i>Nước lạnh</span><span><i style="background:{HOT}"></i>Nước nóng</span><span><i style="background:{GRY}"></i>Thoát nước xám Ø60</span><span><i style="background:{BRN}"></i>Ống chính Ø90 ra bể</span><span><i style="background:#b0bec5"></i>Nước mưa (đợt 2)</span><span><i style="background:#212121;width:8px;height:8px"></i>Van khoá</span></div>
<h2>1. Phản biện trước khi vẽ – phần cắt cho vừa đủ</h2>
<ul>
<li>Giữ đủ chỗ dùng hằng ngày: bếp, WC + tắm nóng lạnh, máy giặt, lavabo.</li>
<li><b>Nước thải:</b> trước đường không có cống chung; ao sau nhà có triều, giữ nuôi cá tôm. Vì vậy nước xám và nước đen gom chung vào <b>1 bể tự hoại nhựa 2.000L nằm ngang có ngăn lọc vi sinh</b>, nước sau bể thấm vào <b>rãnh thấm 7m dọc rào trước bên trái</b> (cách ao ≥15m, cách giếng ≥19m). Ao chỉ nhận nước mưa.</li>
<li>Không dẫn ống ra sông: ao lấy nước từ sông theo con nước nên nước thải sẽ quay lại ao, và xả ra nguồn nước phải đạt QCVN 14:2025 cột B.</li>
<li>Bể đặt trước hiên nhà chính: nơi đất khô duy nhất cách giếng ≥15m, không nằm dưới dốc cổng, xe hút đậu ngoài đường. Triều cao nhất thấp hơn nền 0,30m nên toàn hệ kín, có nắp lật 1 chiều; ao lúc ròng thấp hơn nền ~2m nên rãnh thấm rút được.</li>
<li>Chủ nhà không tự đào: thuê máy đào mini nửa ngày + 1 thợ phụ (hố bể, rãnh ống, rãnh thấm ~11m³).</li>
<li><b>Rửa chén:</b> chậu rửa trên mặt bếp nhà phụ (van dưới chậu + bẫy mỡ inox).</li>
<li><b>Thêm vòi rửa tay chân khi về nhà</b> ở góc sân xe cạnh cửa nhà phụ: nối Ø27 thêm ~5m, 1 vòi đồng + van, bệ láng xi măng 0,8×0,6m có phễu thu nối vào đường thoát bếp (dốc 2%) → <b>thêm ≈ 0,6tr</b>. Đặt ở đây để dùng chung rửa xe, khỏi làm vòi rửa xe riêng; không chôn đường thoát riêng ra ao.</li>
<li>Vẫn để đợt 2: vòi sân sau, bơm tăng áp, thoát sân Ø114, bồn nước mưa.</li>
<li>Không cắt: bồn trên chân 2,5m (mái nhà chính lợp tôn, không đặt bồn lên được; hạ bồn thì sen + bình nóng lạnh yếu áp), xét nghiệm nước giếng (nhà có bầu), van an toàn bình nóng lạnh.</li>
<li>Cột lọc chỉ lắp khi xét nghiệm báo phèn/sắt cao.</li>
</ul>
<h2>2. Mặt bằng cấp – thoát</h2>
{plan}
<h2>3. Sơ đồ nguyên lý</h2>
{one}
<h2>3b. Chi tiết bình nóng lạnh: 2 ống nóng – lạnh</h2>
<svg viewBox="0 0 680 230" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11"><style>text{{paint-order:stroke;stroke:#fff;stroke-width:3px}}</style><rect width="680" height="230" fill="#fff"/>
<rect x="560" y="20" width="90" height="120" rx="10" fill="#fce4ec" stroke="#d81b60"/><text x="605" y="76" text-anchor="middle" font-weight="bold">Bình có sẵn</text><text x="605" y="92" text-anchor="middle" font-size="10">đáy cách sàn ≥1,8m</text>
<path d="M20 190H630V140" fill="none" stroke="#1e88e5" stroke-width="4"/><path d="M585 140V170H400" fill="none" stroke="#e53935" stroke-width="4"/><path d="M230 190V158H330" fill="none" stroke="#1e88e5" stroke-width="4"/>
<rect x="330" y="140" width="70" height="46" rx="5" fill="#eceff1" stroke="#455a64"/><text x="365" y="160" text-anchor="middle" font-size="10">Van trộn</text><text x="365" y="174" text-anchor="middle" font-size="10">sen 1,1m</text>
<rect x="95" y="181" width="14" height="18" rx="2" fill="#212121"/><text x="102" y="216" text-anchor="middle" font-size="10">Van khoá</text>
<rect x="160" y="181" width="14" height="18" rx="2" fill="#616161"/><text x="167" y="216" text-anchor="middle" font-size="10">Van 1 chiều</text>
<circle cx="230" cy="190" r="5" fill="#1e88e5"/><text x="236" y="216" font-size="10">Tê chia</text>
<rect x="500" y="181" width="14" height="18" rx="2" fill="#ffb300"/><text x="507" y="216" text-anchor="middle" font-size="10">Van an toàn (ống xả xuống phễu sàn)</text>
<text x="24" y="180" font-size="10" fill="#1e88e5">Lạnh: ống Ø21 nhánh WC + dây mềm inox vào bình</text><text x="420" y="162" font-size="10" fill="#e53935">Nóng: dây cấp mềm inox 1m</text>
<text x="24" y="20" font-size="11" fill="#37474f">2 ống riêng: lạnh (xanh) vào đáy bình qua 3 van; nóng (đỏ) từ bình ra van trộn.</text><text x="24" y="36" font-size="11" fill="#37474f">Nhánh lạnh thứ 2 từ tê chia vào van trộn để pha nước.</text></svg>
<h2>4. Vật tư đợt 1</h2>
<p><b>Mục 9 – Cấp + thoát nước</b></p>{b9}
<p><b>Mục 2 – Bể tự hoại có ngăn lọc + ống chính + rãnh thấm</b></p>{b2}
<p style="font-size:13px">Cộng 2 mục ≈ <b>{(t9+t2)/1000:.1f}tr</b> chưa VAT, dự phòng. Đợt 2 (bơm tăng áp, thoát nước mưa sân Ø114, vòi sân sau, bồn nước mưa) xem bảng dự toán.</p>
<h2>5. Quy cách thi công</h2>
<ul>
<li>Ống cấp uPVC dán keo, chôn ≥0,3m, qua chỗ xe chạy thì lồng ống bảo vệ. Thử áp: bịt đầu, mở bồn, để 24 giờ không rò mới lấp.</li>
<li>Mỗi nhánh có van khoá riêng để sửa chỗ nào khoá chỗ đó.</li>
<li>Bình nóng lạnh: đầu nước lạnh vào lắp van khoá + van 1 chiều + van an toàn, ống xả van an toàn dẫn xuống phễu sàn, không bịt. Nóng xuống van trộn bằng dây cấp mềm inox.</li>
<li>Ống thoát dốc ≥2%, mỗi thiết bị có siphon/bẫy mùi; nước xám (đã qua bẫy mỡ) nhập ống chính Ø90 tại hố ga rồi vào bể.</li>
<li>Bể: đáy bê tông lót 10cm + 2 đai neo chống nổi; đào lúc triều ròng, đóng cừ tràm chống sạt lề đường; hút bùn 2–3 năm/lần, hút lúc triều ròng rồi châm nước lại ngay.</li>
<li>Rãnh thấm: rộng 0,5m, sâu ~0,8m, ống Ø60 đục lỗ trong lớp đá/gạch vỡ bọc vải địa; không để nước mưa chảy vào.</li>
<li>Bồn cũ: kiểm tra mối hàn, súc rửa bằng nước + chlorine trước khi dùng; neo chân bồn xuống đế bê tông.</li>
</ul></body></html>'''
open('/home/claude/nha-duyen-hai/nuoc.html','w').write(page); print('nuoc ok',round(t9),round(t2))
