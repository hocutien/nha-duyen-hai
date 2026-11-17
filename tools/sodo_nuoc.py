import os
import json, math, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from plan_common import *
s=src(); P=Plan(0.2,22.6,-1.4,21.4,46)
BLU,HOT,GRY,BRN,D2='#1e88e5','#e53935','#757575','#424242','#90a4ae'
P.walls(walls(s))
P.rooms([('PHÒNG KHÁCH',16.2,6.4),('PHÒNG NGỦ 1',16.6,12.6),('PHÒNG NGỦ 2',16.6,16.0),('BẾP – ĂN',10.6,9.6),('KHU GIẶT',13.0,15.6),('WC + TẮM',9.9,17.4),('SÂN TRƯỚC',12.5,4.5),('ĐƯỜNG',14,-1.0)])
# --- dot 2 (net dut, xam)
P.line([[13.0,2.2],[18.3,2.2],[20.3,2.3]],'#b0bec5',2,True);P.text('Đợt 2: chỉ nước mưa ra ao (hố thu + Ø114)',19.0,2.2,'middle','#78909c',-8)
P.rect(12.75,1.95,0.5,0.5,'#eceff1','#b0bec5',True)
P.line([[7.62,11.25],[7.62,6.9],[8.3,6.9]],BLU,2.5);P.circle(8.3,6.9,3.5,'#212121','#212121');P.rect(8.1,6.1,0.8,0.6,'#e0e0e0','#757575');P.rect(8.42,6.32,0.16,0.16,'#263238','#263238');P.line([[8.5,6.4],[7.65,6.4]],GRY,2);P.text('Vòi rửa tay chân',9.0,6.9,'start','#0d47a1',0,None,10,True);P.text('+ bệ rửa chân cao 0,3m',9.0,6.9,'start','#0d47a1',13)
P.line([[13.4,18.75],[13.4,19.0]],D2,2,True);P.text('Đợt 2: vòi sân sau',13.45,18.75,'start',D2,-6)
P.circle(6.9,20.5,0.65*46,'none','#26a69a',True);P.text('Đợt 2: bồn nước mưa',6.9,20.5,'middle','#26a69a',4)
P.rect(15.0,19.4,0.35,0.25,'#e3f2fd',D2,True);P.text('Đợt 2: bơm tăng áp (chỉ khi máy giặt thiếu áp)',15.4,19.35,'start',D2,10)
P.circle(13.6,19.6,0.13*34,'#eceff1',D2,True);P.text('Cột lọc (chỉ khi nước phèn)',13.6,20.2,'middle',D2,-4)
# --- cap
P.circle(12.0,19.75,6,'#bbdefb',BLU);P.text('Giếng khoan',12.0,19.75,'end',BLU,4,-10)
P.rect(12.5,19.35,0.45,0.3,'#bbdefb');P.text('Bơm 0,75kW',12.7,19.35,'middle','#37474f',14)
P.line([[12.0,19.75],[12.5,19.5]],BLU,2.5)
P.line([[12.95,19.5],[13.6,19.6],[15.45,19.75],[15.75,19.95]],BLU,2.5)
P.circle(15.9,20.05,0.55*34,'#e3f2fd',BLU);P.text('Bồn inox 1.000L',15.9,20.05,'middle','#0d47a1',2,0,10,True);P.text('chân 2,5m · phao điện',15.9,20.05,'middle','#37474f',14)
P.line([[15.9,20.05],[15.35,19.55]],BLU,3);P.line([[15.0,19.5],[14.6,19.5],[14.6,18.75],[7.95,18.75],[7.62,18.6],[7.62,11.25]],BLU,3)
P.text('Ống cấp Ø27 chôn 0,3m sau nhà',11.0,18.85,'middle',BLU,-6);P.text('Ø27 đi nổi trên tường, cao 0,7m (trên ống thoát)',7.5,14.6,'end',BLU,4)
br=[([[11.85,18.75],[11.85,18.38]],(11.85,18.38),'Máy giặt 1,0m','start'),([[12.55,18.75],[12.55,18.38]],(12.55,18.38),'Lavabo','start'),
    ([[7.62,11.25],[8.25,11.25]],(8.25,11.25),'Chậu bếp (van dưới chậu)','start'),
    ([[9.5,18.75],[8.22,18.75],[8.22,18.1],[8.22,16.5]],(8.22,16.5),'Van khoá vào máy nước nóng','start'),
    ([[8.22,18.1],[8.22,18.2],[8.95,18.2]],(8.95,18.2),'Bồn cầu + vòi xịt','start')]
for pts,v,t,anc in br:
    P.line(pts,BLU,2)
    if v: P.circle(v[0],v[1],3.5,'#212121','#212121')
for t,a,b,anc,dy in [('Máy giặt 1,0m',11.85,18.38,'end',-6),('Lavabo',12.55,18.38,'start',14),('Chậu rửa chén',8.25,11.25,'start',4),('Van khoá',8.3,16.7,'start',4),('Bồn cầu',8.95,18.2,'start',4)]:
    P.text(t,a,b,anc,'#37474f',dy)
P.rect(8.12,16.4,0.1,0.19,'#fce4ec','#d81b60');P.text('Máy NL trực tiếp 4,5kW có bơm',8.35,16.45,'start','#ad1457',4)
P.line([[8.2,16.45],[8.22,16.05]],HOT,2.5);P.circle(8.22,16.05,4,'#b0bec5');P.text('Sen của máy',8.35,16.05,'start',HOT,10)
# --- thoat: ong chinh O90 doc 1,5% -> be tu hoai san truoc bep -> bai tham du kien
P.rect(8.25,11.05,0.3,0.4,'#cfd8dc');P.text('Bẫy mỡ',8.4,10.85,'start','#37474f',8)
P.line([[8.4,11.25],[7.3,11.25]],GRY,2)
P.rect(8.67,15.92,0.16,0.16,'#263238','#263238');P.line([[8.75,16.0],[7.3,16.0]],GRY,2);P.text('Phễu sàn tắm',8.85,16.0,'start','#424242',14)
P.line([[12.55,18.25],[12.55,18.0]],GRY,2);P.circle(11.86,18.05,3,'#757575','#424242');P.text('Ống đứng máy giặt (không phễu sàn)',12.0,17.75,'start','#424242',4)
P.line([[17.8,12.9],[18.15,12.9]],GRY,1.5);P.text('Nước ngưng máy lạnh',18.15,12.9,'start','#424242',4)
P.line([[12.55,18.0],[8.55,18.0],[7.3,17.4],[7.3,6.7],[9.0,5.0],[9.0,4.65]],BRN,3);P.text('Ống chính Ø90 dốc 1,5% · đi nổi chân tường',7.2,13.0,'end',BRN,4)
for a_,b_ in [(7.3,17.4),(7.3,6.7)]: P.rect(a_-0.08,b_-0.08,0.16,0.16,'#616161','#212121')
P.text('Nắp kiểm tra',7.2,17.4,'end','#212121',4);P.text('Nắp kiểm tra',7.2,6.7,'end','#212121',4)
P.circle(7.45,17.7,3,'#9e9e9e','#424242');P.text('Thông hơi Ø60 lên mái',7.4,18.1,'end','#424242',-4)
P.rect(8.4,2.3,1.2,2.3,'#cfd8dc','#263238');P.text('Bể 2.000L',9.0,3.6,'middle','#263238',0,None,10,True);P.text('có ngăn lọc',9.0,3.6,'middle','#263238',13)
P.text('cách giếng ≥15,3m',9.7,3.0,'start','#263238',4)
P.line([[9.0,2.3],[9.0,1.6],[2.25,1.6],[1.65,2.2]],BRN,2,True);P.rect(8.92,1.52,0.16,0.16,'#616161','#212121');P.text('Ra bãi thấm Ø90 dốc 1,2% · đan BT qua lối xe',5.6,1.6,'middle','#424242',-8)
P.rect(1.0,2.0,1.3,6.3,'#e8e4d4','#8d8a7a',True);P.line([[1.65,2.2],[1.65,8.3]],'#8d6e63',2,True);P.text('Bãi thấm DỰ KIẾN ~10m²',1.65,5.6,'start','#424242',0,14,10,True);P.text('chốt sau khi thử thấm',1.65,5.6,'start','#424242',13,14)
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
     ar(515,49,537,49),bx(537,30,105,'Van tổng Ø34','đoạn 5m'),ar(642,49,662,49),bx(662,30,110,'Bơm tăng áp','chỉ nếu máy giặt cần','#eceff1','#90a4ae',True),
     ar(772,49,790,49),bx(790,30,100,'Ống chính Ø27','ngầm + nổi ~23m')]
x=60
for t1,t2,d in [('Máy giặt','van 1,0m',False),('Lavabo','van góc',False),('Bồn cầu','van + vòi xịt',False),('Máy nước nóng','trực tiếp có bơm · 1 van khoá',False),('Chậu rửa chén','van, chừa tê RO',False),('Vòi trước nhà','rửa tay chân',False)]:
    g.append(bx(x,110,128,t1,t2,'#eceff1' if d else '#e3f2fd','#90a4ae' if d else '#1e88e5',d)); g.append(ar(840,68,x+64,110,'#90a4ae' if d else '#1e88e5',d)); x+=138
g.append('<text x="10" y="190" font-weight="bold" fill="#424242">THOÁT NƯỚC THẢI (không xả ra ao, không xả ra sông)</text>')
G2='#757575'
g+= [bx(10,200,150,'Chậu bếp','bẫy mỡ inox dưới chậu','#f5f5f5',G2),bx(10,243,150,'Máy giặt + lavabo','ống đứng 0,8m, siphon','#f5f5f5',G2),bx(10,286,150,'Sàn tắm WC','phễu thu có bẫy mùi','#f5f5f5',G2),bx(10,329,150,'Bệ rửa chân cao 0,3m','rửa xe không vào bể','#f5f5f5',G2),
     ar(160,219,215,262,G2),ar(160,262,215,264,G2),ar(160,305,215,266,G2),ar(160,348,215,268,G2),bx(215,245,120,'Nhánh Ø60','dốc ≥2,5%, chếch Y','#f5f5f5',G2),ar(335,264,375,330,G2),
     bx(10,400,150,'Bồn cầu','ống Ø90 dán keo kín','#eeeeee','#424242'),ar(160,419,375,354,'#424242'),
     bx(375,323,120,'Ống chính Ø90','dốc 1,5%, co lơi 45°','#eeeeee','#424242'),ar(495,342,520,342,'#424242'),
     bx(520,315,150,'Bể tự hoại 2.000L','có ngăn lọc vi sinh','#cfd8dc','#263238'),ar(595,353,595,380,'#424242'),
     bx(530,380,130,'Tê kiểm tra','đầu ra bể ≈ 0,0','#eeeeee','#212121'),ar(595,418,595,440,'#424242'),
     bx(510,440,170,'Bãi thấm dự kiến ~10m²','chốt sau khi thử thấm','#e8e4d4','#8d8a7a'),
     bx(700,200,180,'Nước mưa mái, sân','ra ao riêng (sạch)','#eceff1','#b0bec5',True),
     '<text x="700" y="330" font-size="10" fill="#455a64">Bể ở sân trước bếp,</text><text x="700" y="344" font-size="10" fill="#455a64">cách giếng ≥15,3m; đầu ra cao hơn</text><text x="700" y="358" font-size="10" fill="#455a64">triều cao nhất ~0,3m; hút bùn</text><text x="700" y="372" font-size="10" fill="#455a64">2–3 năm, lúc triều ròng.</text>']
g.append('</svg>')
one='\n'.join(g)
b9,t9=bom_table(['9. Nước cấp + thoát']); b2,t2=bom_table(['2. Bể tự hoại + ống thoát'])
page=f'''<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sơ đồ nước chi tiết – nhà Duyên Hải</title>{STYLE}</head><body>
{nav('nuoc.html')}
<h1>Sơ đồ cấp – thoát nước chi tiết (phương án vừa đủ dọn vào ở)</h1>
<p style="font-size:14px">Cùng toạ độ với lớp <b>Nước</b> trong mô hình 3D. Nét liền: cấp nước; nét đứt đậm: ống thoát chôn ngầm; <span class="d2">nét đứt xám: đợt 2</span>.</p>
<div class="lg"><span><i style="background:{BLU}"></i>Nước lạnh</span><span><i style="background:{HOT}"></i>Nước nóng</span><span><i style="background:{GRY}"></i>Thoát nước xám Ø60</span><span><i style="background:{BRN}"></i>Ống chính Ø90 ra bể</span><span><i style="background:#b0bec5"></i>Nước mưa (đợt 2)</span><span><i style="background:#212121;width:8px;height:8px"></i>Van khoá</span></div>
<h2>1. Phản biện trước khi vẽ (bản 17/11: ưu tiên dọn vào ở)</h2>
<ul>
<li><b>Cao độ quyết định:</b> so với nền nhà, sàn WC +0,5; sân −0,1; triều cao nhất −0,3. Bản cũ để bể trước hiên nhà chính, ống chính dài ~25m nên đầu ra bể ở −0,5m, <b>thấp hơn triều</b>; rãnh thấm sâu tới −0,95m nằm dưới cổng phụ.</li>
<li><b>Bản này:</b> dời bể về <b>sân trước bếp</b> (cách giếng ≥15,3m), ống chính Ø90 còn ~19m, dốc 1,5% (TCVN 4474 cho phép Ø90–100 từ 1,2%), đi nổi chân tường. Đầu ra bể ≈ 0,0: <b>cao hơn triều cao nhất ~0,3m</b>, bỏ nắp lật.</li>
<li>Chỉ thiết bị xả từ cao ≥ +0,3 mới chảy về bể được: bồn cầu, sàn tắm WC (+0,5), lavabo, máy giặt (ống đứng), chậu bếp, bệ rửa chân nâng cao 0,3m. <b>Khu giặt bỏ phễu sàn</b>, dùng khay hứng dưới máy. <b>Rửa xe</b> làm trên nền đá mi sân xe, không vào bể.</li>
<li><b>Bãi thấm: chốt sau khi đo.</b> Chỗ duy nhất phía trước vừa cách giếng ≥15m vừa cách ao ≥15m là dải dọc rào trái (~10m²). Ngày thuê máy đào làm hố thử trước: đất cát cần ~12–20m², đất sét ~30–50m². Nếu cần quá 10m² thì chọn phương án bổ sung theo kết quả.</li>
<li><b>Ống cấp</b> Ø27 không còn chôn song song dưới ống thoát: chôn đoạn sau nhà, lên đi nổi trên tường hông trái cao 0,7m. Ống thoát gần giếng nhất 1,75m là đoạn đi nổi trong khu giặt (dán keo kín, rò là thấy ngay); không có ống thoát chôn gần giếng. Mọi chỗ rẽ dùng co lơi 45°, nhập nhánh bằng chếch Y.</li>
<li><b>Máy nước nóng</b>: Panasonic DH-4VP1VW trực tiếp 4500W có bơm, đồ cũ có sẵn sen. Máy chạy từ áp ~0,05 bar nên bồn 2,5m là dư; chỉ cần 1 van khoá. Bỏ van an toàn, van 1 chiều, van trộn, sen mua mới.</li>
<li><b>Bồn nước</b> giữ góc phải phía sau trên chân 2,5m: gần khu giặt (~4m ống), xa bếp. Máy giặt được ~0,15–0,25 bar; nếu model cần cao hơn thì lắp bơm tăng áp 125W (đợt 2).</li>
<li>Vẫn để đợt 2: vòi sân sau, thoát sân Ø114, bồn nước mưa, cột lọc (chỉ khi nước phèn).</li>
</ul>
<h2>2. Mặt bằng cấp – thoát</h2>
{plan}
<h2>3. Sơ đồ nguyên lý</h2>
{one}
<h2>3b. Trắc dọc ống chính (cao độ đáy ống so với nền nhà)</h2>
<table><tr><th>Điểm</th><th>Vị trí</th><th>Đáy ống</th><th>Ghi chú</th></tr>
<tr><td>Đầu tuyến</td><td>Khu giặt (lavabo, máy giặt)</td><td>+0,36</td><td>đi nổi sát chân tường sau</td></tr>
<tr><td>Bồn cầu</td><td>Dưới sàn WC (+0,5)</td><td>+0,30</td><td>chếch Y; phễu sàn tắm vào ở +0,30</td></tr>
<tr><td>Góc WC</td><td>Ra hông trái nhà phụ</td><td>+0,27</td><td>2 co lơi, nắp kiểm tra, ống thông hơi Ø60</td></tr>
<tr><td>Chậu bếp</td><td>Hông trái, ngang bếp</td><td>+0,19</td><td>nhánh Ø60 từ bẫy mỡ (+0,24)</td></tr>
<tr><td>Góc trước nhà phụ</td><td>Chân tường</td><td>+0,11</td><td>nắp kiểm tra; bệ rửa chân vào ở +0,11</td></tr>
<tr><td>Vào bể</td><td>Sân trước bếp</td><td>+0,07</td><td>đoạn qua sân chôn/đắp đất phủ</td></tr>
<tr><td>Ra bể</td><td>Tê kiểm tra</td><td>≈ 0,0</td><td>cao hơn triều cao nhất (−0,3) ~0,3m</td></tr>
<tr><td>Bãi thấm</td><td>Dải rào trái</td><td>ống −0,1; đáy đá −0,3</td><td>dự kiến, chốt sau khi thử thấm</td></tr></table>
<p style="font-size:13px">Cao độ giả định đáy ống bồn cầu +0,30; đo thực tế rồi chỉnh. Ống đi nổi ngoài trời sơn chống nắng; đoạn trên mặt sân đắp đất/đá mi phủ ≥0,2m, đợt 2 nâng sân +0,5 sẽ chôn hẳn.</p>
<h2>4. Vật tư đợt 1</h2>
<p><b>Mục 9 – Cấp + thoát nước</b></p>{b9}
<p><b>Mục 2 – Bể tự hoại có ngăn lọc + ống chính + bãi thấm</b></p>{b2}
<p style="font-size:13px">Cộng 2 mục ≈ <b>{(t9+t2)/1000:.1f}tr</b> chưa VAT, dự phòng; phần bãi thấm là dự kiến. Đợt 2 (bơm tăng áp nếu cần, thoát nước mưa sân Ø114, vòi sân sau, bồn nước mưa) xem bảng dự toán.</p>
<h2>5. Quy cách thi công</h2>
<ul>
<li>Ống uPVC dán keo. <b>Mọi chỗ rẽ: 2 co lơi 45° hoặc co cong</b>, không dùng co, tê 90° vuông; ống thoát nhập nhánh bằng chếch Y 45°.</li>
<li>Ống cấp chôn ≥0,3m đoạn sau nhà; đoạn trên tường kẹp chắc, sơn chống nắng, nằm trên ống thoát và cách ≥0,4m. Thử áp: bịt đầu, mở bồn, để 24 giờ không rò mới lấp. Mỗi nhánh có van khoá riêng.</li>
<li>Máy nước nóng: 1 van khoá đầu vào, treo đáy cao ~1,4m so sàn WC, ngoài tia nước; điện xem trang Điện (dây 4mm², MCB 32A).</li>
<li>Ống thoát: chính Ø90 dốc 1,5%, nhánh Ø60 dốc ≥2,5%; mỗi thiết bị có siphon/bẫy mùi; nước bếp qua bẫy mỡ.</li>
<li>Bể: đào lúc triều ròng; đáy bê tông lót 10cm + 2 đai neo chống nổi; thử nước kín mối nối trước khi lấp; nắp nhô ~0,35m đắp đất phủ, không cho xe lên; hút bùn 2–3 năm/lần lúc triều ròng rồi châm nước lại ngay.</li>
<li>Hố thử thấm (làm trước): hố 0,3×0,3×0,6m ở dải rào trái, đổ nước ngâm 4 giờ, đổ đầy lại rồi đo mực rút trong 30 phút; ghi mực nước ngầm.</li>
<li>Bãi thấm: ống Ø90 khoan lỗ đặt ở −0,1, lớp đá/gạch vỡ từ −0,3 đến −0,05 bọc vải địa, phủ đất thành ụ thấp; không để nước mưa mái đổ vào; chỉ đi bộ, không cho xe lên.</li>
<li>Bồn cũ: kiểm tra mối hàn, súc rửa bằng nước + chlorine; neo chân bồn xuống đế bê tông.</li>
</ul></body></html>'''
open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'nuoc.html'),'w').write(page); print('nuoc ok',round(t9),round(t2))
