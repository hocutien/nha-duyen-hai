import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"out");os.makedirs(OUT,exist_ok=True)
P1=[
("A","Nhà chính","Trát chống thấm chân tường cao 1,2m (phòng ở + hành lang)","Mới",5,8),
("B","Nền nhà tạm","Mua thêm xà gồ, vít, ke chống bão, úp nóc, máng xối","Khung gỗ + tôn cũ",6,10),
("B","","Vách tôn + cửa sắt lắp lại","Cũ",1,2),
("B","","Sửa, láng nền gạch cũ","Mới",3,5),
("C","WC + vệ sinh","Xây WC, nâng nền +0,5m, chống thấm, lát gạch","Mới",10,14),
("C","","Bồn cầu, lavabo, sen, quạt hút","Mới",4,6),
("C","","Bể tự hoại 3 ngăn 1.500–2.000L (Đại Thành ~4–6,8tr, META) + ống Ø90 ~16m + lót BT + lắp","Mới",7,10),
("C","","Lấp hầm cũ + sân bê tông miệng giếng","Mới",1,2),
("D","Bếp","Tủ/kệ bếp cũ + mặt bếp 3,4m","Cũ + mặt mới",4,7),
("D","","Chậu đôi + vòi","Mới",1,1.5),
("D","","Bếp từ đôi","Mới",3,4.5),
("D","","Bếp gas đơn + van + dây","Mới",0.6,1),
("D","","Máy hút mùi","Cũ được",0.5,1.5),
("D","","Bàn ăn + 4 ghế","Cũ",1,1.5),
("E","Điện","Tủ điện, CB tổng 63A, RCBO, MCB, chống sét lan truyền, cọc tiếp địa","Mới",5,7),
("E","","Dây mới cho mạch bếp từ, giặt sấy, ngoài trời + ống + ổ IP55","Mới",4,6),
("E","","Đo cách điện, thay ổ/công tắc, giữ dây cũ chiếu sáng + ổ cắm","Dây cũ",1.5,3),
("E","","Đèn LED, quạt","Cũ được",1.5,2.5),
("E","","Nhân công điện","",3,5),
("E","","Mạng: CAT6 ~75m + ống + ổ mạng, kéo sẵn cả đường camera và ống chờ lên mái","Mới",1.5,2.5),
("F","Nước","Bơm giếng 1HP","Cũ được",1,2.5),
("F","","Bồn inox 1.000L (3,5–4tr, ĐMX) + chân sắt 2,5m","Mới",4,6),
("F","","Ống PPR/uPVC + phụ kiện cấp, thoát","Mới",3,5),
("F","","Bình nóng lạnh 30L","Mới",2,3),
("F","","Xét nghiệm nước giếng (lọc tính sau theo kết quả)","Mới",0.5,1),
("F","","Nhân công nước","",2,4),
("I","Máy lạnh","Tháo lắp, di dời máy lạnh 1,5HP có sẵn + ống đồng + châm gas","Có sẵn",1,1.5),
("G","Thai phụ","Lưới chống muỗi cửa sổ + cửa đi, đèn cảm biến đêm, gạch chống trơn + tay vịn WC","Mới",2,3.5),
("G","An toàn cháy","2 bình chữa cháy 4kg, chăn chữa cháy, 4 đầu báo khói/nhiệt, báo rò gas, ổ sạc xe điện ngoài trời","Mới",2,3),
("H","Sân, rào","Rào mặt tiền ~40m: trụ + kẽm gai (kẽm gai quanh đất làm đợt 2)","Mới",1.5,3),
("H","Nhà xe","Mái che 5,8×7,3m: 4 cột + đà sắt hộp mạ kẽm, xà gồ, lợp tôn cũ, máng xối; thợ hàn 2 người × 3 ngày","Tôn cũ",5,8),
("H","Cây xanh","7 cây che nắng (bàng Đài Loan ×3 bên phải, mù u ×4 phía sau) cao 2–2,5m + 10 phi lao chắn gió + ~70 gốc bông giấy rào mặt tiền + đất, phân","Mới",3,6),
("H","","Lắp lại cổng sắt cũ + trụ","Cũ",1,2),
]
P2=[("Sơn lại phòng ở + mặt tiền (tự sơn)","Mới",2,4),
("Đục cửa sau hành lang + ô văng","Cửa sắt cũ",3,5),
("Kệ V lỗ phòng kho + đá mi sân xe","Cũ/mới",2,4),
("Cột lọc nước (nếu xét nghiệm có phèn)","Mới",1.5,3),
("3 camera PoE + switch PoE (dây đã kéo sẵn ở đợt 1)","Mới",2.5,4),
("Cảm biến Zigbee: khói, rò nước, cửa (báo về điện thoại qua Home Assistant)","Mới",1,2),
("Bồn nước mưa 2.000L nhựa (4,29tr, ĐMX) + máng","Mới",4.5,5.5),
("Máy rửa xe áp lực","Mới",1.5,2.5),
("Bơm tăng áp tự động","Mới",1,1.5),
("Kẽm gai quanh đất + đá mi lối đi","Mới",5,9),
("San lấp ao, đắp sân bằng mặt lộ, nâng nền +0,45m","",50,80)]
lo=sum(r[4] for r in P1);hi=sum(r[5] for r in P1)
f=lambda x:(f"{x:.1f}".rstrip('0').rstrip('.')).replace('.',',')
rows=""
for r in P1: rows+=f"<tr><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{f(r[4])}–{f(r[5])}</td></tr>\n"
rows+=f"<tr><th colspan=3>Cộng</th><th>{f(lo)}–{f(hi)}</th></tr>\n<tr><th colspan=3>Dự phòng 10%</th><th>{f(lo*0.1)}–{f(hi*0.1)}</th></tr>\n<tr><th colspan=3>Tổng đợt 1 (vào ở)</th><th>{f(lo*1.1)}–{f(hi*1.1)}</th></tr>"
r2="".join(f"<tr><td>{a}</td><td>{b}</td><td>{f(c)}–{f(d)}</td></tr>\n" for a,b,c,d in P2)
lo2=sum(x[2] for x in P2[:-1]);hi2=sum(x[3] for x in P2[:-1])
print(lo,hi,lo*1.1,hi*1.1,lo2,hi2)
open(OUT+'/b1.html','w').write(rows);open(OUT+'/b2.html','w').write(r2+f"<tr><th>Cộng phần thiết bị (chưa tính san lấp)</th><th></th><th>{f(lo2)}–{f(hi2)}</th></tr>")
