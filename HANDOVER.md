# Bàn giao – Nhà Duyên Hải (cải tạo để dọn vào ở)

Tài liệu này giúp người khác hoặc một tài khoản Claude khác tiếp tục làm mà không cần đọc lại lịch sử chat.

## 1. Mục tiêu
- Chủ nhà là Tiến. Hai vợ chồng dọn vào ở sớm; **vợ đang mang thai**.
- Ngân sách đợt 1 khoảng **100–115tr**. Dự toán chi tiết (bóc tách 152 dòng, đơn giá Thông báo 561/TB-SXD Vĩnh Long PL II KV10 + PL IV, kỳ 01–15/9/2026) = **~145,6tr** gồm VAT + 10% dự phòng (bản 17/11), vượt mốc 100tr ~45tr: chủ nhà cần chọn hạng mục để dời sang đợt 2. Nguồn số liệu: `tools/dutoan.py` → `tools/out/dutoan.json`; bảng tính Sheets https://claude.ai/artifact/B8LPuDUHWvyX6ktExjic4L. Đã bỏ ổ sạc xe điện và mua bình nóng lạnh (chủ nhà không có xe điện, đã có bình). Máy nước nóng là Panasonic DH-4VP1VW trực tiếp 4500W có bơm (đồ cũ, có sen) nên vòi sen không cần bơm tăng áp; bơm tăng áp chỉ lắp nếu máy giặt thiếu áp (đợt 2). Đợt 2: 30–46tr thiết bị + nhà xe + san lấp ao 50–80tr + tường mặt tiền 70–110tr.
- Mọi việc làm ở đợt 1 phải dùng tiếp được khi nâng cấp về sau, không phải đập bỏ.
- Thửa 320, tờ 51 (số cũ 595), 2.064,2m² theo GCN, cạnh 53,45 / 44,91 / 44,07 / 41,65m. Phía sau giáp sông lớn; phần đất sát sông (~1.200m²) chưa được cấp GCN.

## 2. Nguyên tắc đợt 1
1. Vào ở sớm và an toàn. Hạng mục không phục vụ việc vào ở thì để sang đợt 2.
2. Tận dụng đồ có sẵn: tủ lạnh, máy giặt, máy sấy, **1** máy lạnh 1,5HP (không mua thêm), tôn, cột gỗ, cửa sắt cũ.
3. Không phải làm lại về sau:
   - ổ cắm cao ≥1m, vì nền nhà sẽ nâng +0,45m và sân +0,5m;
   - sàn WC +0,5m;
   - hộp công tắc có dây N để lắp Zigbee;
   - ống chờ cho mạng, camera và đường lên mái;
   - tủ điện 24 module, chừa module dự phòng cho máy lạnh thứ hai, bơm tăng áp, nhà xe.
4. An toàn trước, thẩm mỹ sau:
   - điện: RCBO, nối đất, chống sét lan truyền;
   - bể tự hoại cách giếng ≥15m (hiện ~15,9m);
   - chữa cháy: báo khói, báo rò gas, 2 bình chữa cháy 4kg, ô cửa sổ thoát hiểm;
   - thai phụ: lưới chống muỗi, gạch chống trơn, tay vịn, đèn cảm biến đêm.
5. Phần âm (điện, nước, mạng, chống thấm, bể tự hoại) làm đúng một lần. Phần hoàn thiện làm dần.
6. Không còn bụi hay hoá chất khi vợ đã vào ở: làm xong phần bụi và phần sơn/keo, thông gió ≥2 tuần rồi mới dọn vào.
7. Công năng theo cách dùng thật:
   - cửa WC không nhìn ra bàn ăn;
   - khu tắm sát máy giặt + sấy, **không làm phòng giặt riêng**;
   - đường đi đêm từ phòng ngủ đến WC ngắn và có đèn.
8. Hạng mục phụ (nhà xe, mái che) ưu tiên vật liệu rẻ, khung gỗ bắt bulông, để sau này sửa hoặc dời dễ.
9. Ống đi nổi, dễ kiểm tra. Thử áp ống nước và đo cách điện trước khi che lại.
10. Làm đúng ranh GCN và đúng thủ tục: xả thải, san lấp ao, sửa nhà.
11. Số liệu là ước tính, phải hỏi giá thợ địa phương. PA A và PA B cần kỹ sư kiểm tra kết cấu.

## 3. Quyết định đã chốt (đừng đổi lại nếu chủ nhà chưa đồng ý)
- **Bếp:** bếp từ đôi (mạch R1, RCBO 32A, dây 4mm², đợt 2) cộng bếp gas đơn dự phòng; bình gas đặt trong lồng ngoài vách. Thứ tự trên bàn: tủ lạnh → chậu → sơ chế 90cm → bếp. Ổ cắm mặt bếp cách chậu ≥0,6m.
- **WC:**
  - xây tại chỗ WC cũ, sàn +0,5m;
  - **cửa lùa** quay vào khu giặt;
  - lên WC: chiếu nghỉ 0,5m, rồi 2 bậc ~17cm, có tay vịn;
  - quạt hút thổi ra vách ngoài;
  - máy giặt + sấy đặt chồng cạnh WC; lavabo ngoài; cửa sau ra dây phơi.
- **Thoát nước (chốt 17/11):** bể tự hoại nhựa 2.000L nằm ngang có ngăn lọc, ở sân trước bếp, trục dọc vào trong (a 8,4–9,6; b 2,3–4,6), cách giếng ≥15,3m, nắp nhô ~0,35m đắp đất, không cho xe lên. Ống chính Ø90 dốc 1,5% từ khu giặt → dưới sàn WC → đi nổi chân tường hông trái → bể; đầu ra bể ≈ 0,0 (cao hơn triều cao nhất −0,3). Co lơi 45° mọi chỗ rẽ, chếch Y nhập nhánh, thông hơi Ø60 ở đầu tuyến sau WC. Khu giặt không phễu sàn; bệ rửa chân cao 0,3m; rửa xe không vào bể. Bãi thấm dự kiến ~10m² dọc rào trái, **chốt kích thước sau khi thử thấm**. Hầm cũ hút sạch, rắc vôi, lấp cát, đậy bê tông.
- **Điện:** CB tổng 63A, cáp CVV 2×25 chôn trong HDPE Ø50 (cần công tơ ≥63A), 1 cọc tiếp địa, 9 mạch C1–C4, R1–R5. Chống giật mọi mạch: RCCB 63A #1 cho C1–C3; RCBO riêng C4 tủ mạng, R2 bếp, R4 máy nước nóng 4500W (25A, dây 4mm² ống riêng); RCCB 63A #2 cho R3, R5. R5 ngoài trời CVV 3×2,5 có PE. Tủ 24 module. Chi tiết trang dien.html.
- **Mạng:**
  - cáp quang từ cột vào tủ mạng ở phòng khách cạnh bàn làm việc, gồm ONT, MikroTik hEX (RB750), switch thường có sẵn, NAS DS220j + WD, UPS; PC i7-6700 ở bàn làm việc cắm thẳng switch; không dùng Lenovo M720q, không mua switch PoE (camera dùng nguồn PoE rời);
  - **không dùng Aruba**: wifi bằng 2 Xiaomi BE6500 chế độ AP nối dây (phòng khách cạnh TV, kệ cao ở bếp);
  - ~80m CAT6 có sẵn, có ống chờ cho camera.
- **Nhà xe:** góc trước bên trái, 5,7×7,1m, xe vào bằng cổng phụ 4,5m.
  - Kết cấu: 4 cột gỗ 12×12 trên đế bê tông rời (chân sắt U bắt bulông), đà và xà gồ gỗ nối bulông và ke, tôn cũ, nền đá mi. Tháo và dời được, không đổ bê tông.
  - Sedan ≤4,7×1,8m lùi vào, đầu xe ra cổng. 4 xe máy xếp so le sát rào trái, cách nhau 0,55m.
  - Sân trước bếp để trống làm lối đi và chỗ xe khách.
- **Cây (chủ nhà thích kiểu rừng nhiệt đới, cây to):** 3 tầng.
  - Tầng trên: mù u ×3, còng ×2, trên ụ đất cao +0,5m. Còng cách nhà ≥12m.
  - Tầng giữa: cau ×4 hông phải, chuối ×4 bụi phía sau cạnh hố ga nước xám.
  - Tầng dưới: môn, ráy.
  - Thêm phi lao bờ sông, bông giấy rào mặt tiền. Không trồng trúc đào.
- **Mặt tiền (chốt 15/11):** không trồng cây giáp lộ (chủ nhà không thích rào bông giấy). Đợt 1: nâng nền mí lộ + rào kẽm gai tạm. Đợt sau: tường xây kín 2,6m, 5 ô bông gió, cổng gỗ kín (nhóm `fut`).
- **Nhà phụ:** vách kín lên mái, dải bông gió 0,5m (vách trước + trái; vách sau Tây Nam kín), cách nhiệt dưới tôn, 2 quạt trần (bàn ăn; khu bếp gần cửa, cách bếp gas >3m).
- **Gió:** mặt tiền hướng Đông Bắc, phía sông Tây Nam. Gió mùa mưa Tây Nam thổi qua vườn sau vào nhà; cửa sau nhà chính làm đợt 1, mái hắt 1,2m cho cả 2 cửa sau. Không làm giàn leo.
- **Thẩm mỹ:** tường trắng ngà, gỗ nâu (nhà xe, lam gỗ mặt bếp), mái xám đậm, cổng song sắt nâu.
- **Ban công trên cao:** hai phương án, chưa chọn.
  - PA A: sân thượng trên mái nhà chính, 32–53tr.
  - PA B: lầu gỗ kiểu Hà Giang trên nhà tạm, 50–80tr (bản đầy đủ 130–220tr).

## 4. Tệp trong repo
| Tệp | Nội dung |
|---|---|
| `index.html` | Trang 3D (three.js r128, một tệp duy nhất). Là nguồn chính của mọi thứ. Panel Thuyết minh nằm trong `<div id="tmp">`. |
| `map.html` | Bản đồ thực địa (Leaflet), có `ORIGIN`, `BRG0`, danh sách khối `F` và điểm `P`. Hàm `toLL(a,b)` đổi toạ độ công trình sang kinh/vĩ độ. |
| `phuong-an.kml` | Lớp 2D; repo Tracuu nạp tệp này qua nút “🏠 Lớp nhà Duyên Hải”. |
| `nha-duyen-hai-3d.kmz` | Mô hình 3D chi tiết cho Google Earth (~14.000 tam giác, gồm thư mục Đợt 1, PA A, PA B). |
| `tools/genkml.js` | `map.html` → `phuong-an.kml` |
| `tools/export_kmz.py` | `index.html` + `map.html` → `nha-duyen-hai-3d.kmz` |
| `tools/budget.py` | Danh sách hạng mục đợt 1 và đợt 2 → bảng HTML trong `tools/out/b1.html`, `b2.html`, dán vào Thuyết minh mục 11. |
| `tools/dutoan.py` | Dự toán chi tiết (nguồn số liệu tiền) → `tools/out/dutoan.json`. |
| `tools/sodo_dien.py`, `sodo_nuoc.py`, `sodo_mang.py` (+ `plan_common.py`) | Đọc `index.html` + `out/dutoan.json`, sinh lại `dien.html`, `nuoc.html`, `mang.html`. |
| `tools/check_render.py` | Mở trang ở chế độ ẩn, báo lỗi JS, chụp ảnh các góc nhìn vào `tools/out/`. |

Cách vẽ chân thật trong `index.html`:
- `mat(màu)` tra bảng `MT` theo mã màu để gán vân (`TEX`: plaster, brick, wood, ton, gravel, grass, asphalt, concrete, tile), độ nhám và độ kim loại. Muốn thêm vật liệu mới thì thêm dòng `mt([...],{...})`.
- Cuối trang có một bước tính UV theo mét và bật bóng đổ cho mọi khối gần nhà.
- Mặt trời đặt ở hướng 245°, cao 42° (khoảng 15h).
- Hàm vẽ cây: `bigTree(a,b,tỉ_lệ,'cong'|'muu')`, `cau`, `chuoi`, `ray`, `phiLao`, `mound` (ụ đất). Hàng rào cây: `hedge`. Cổng song: `gate`.

Hệ toạ độ trong `index.html`:
- `a` chạy dọc mặt lộ, `b` chạy từ lộ vào trong (về phía sông), `z` là cao độ (m).
- Nhóm `site` được xoay theo góc PHI; điểm (a, b, z) nằm ở vị trí mesh (a, z, −b).
- Hàm tiện ích: `box`, `wall`, `pipe`, `label(text,a,b,z,parent)`.
- Các nhóm: `mep` (điện nước), `fut` (cao độ tương lai), `optA`, `optB`, `treeObjs`.

## 5. Sửa và xuất lại
```bash
cd tools && npm i three@0.128.0 && pip install playwright   # chỉ làm lần đầu
python3 check_render.py           # phải in "Không lỗi JS"
node genkml.js                    # khi sửa map.html
python3 export_kmz.py             # khi sửa khối nhà trong index.html
python3 dutoan.py && python3 budget.py   # khi sửa giá; dán out/b1.html vào index.html mục 11
python3 sodo_dien.py && python3 sodo_nuoc.py && python3 sodo_mang.py   # sinh lại 3 trang chi tiết
```
- Nếu Chrome không nằm ở `/usr/bin/google-chrome`, đặt biến môi trường `CHROME=<đường dẫn>`.
- Đăng web: push lên nhánh `main`, GitHub Pages tự cập nhật trang https://hocutien.github.io/nha-duyen-hai/.
- Có một bản artifact trên claude.ai (slug `f920515a-088f-4da2-9912-090238ba537a`) chỉ tài khoản gốc sửa được. Tài khoản khác dùng GitHub Pages.

## 6. Việc còn dở / có thể làm tiếp
- [ ] Đo tại chỗ (Thuyết minh mục 14):
  - cao độ nền so với mặt lộ;
  - trần thả;
  - vị trí giếng và hầm cũ;
  - khoảng cách đến cột điện;
  - công tơ điện (≥80A?);
  - kiểm tra nước giếng (nitrat, asen, vi sinh).
- [ ] Hỏi giá 2–3 thợ địa phương để thay giá ước tính trong `tools/budget.py`.
- [ ] Tải Phụ lục II của Thông báo 573/TB-SXD (Sở Xây dựng Vĩnh Long, giá vật liệu khu vực Trà Vinh cũ) rồi thay giá vật liệu trong `tools/budget.py`.
- [ ] Hỏi giá cây bàng Đài Loan, mù u, phi lao, bông giấy ở vựa Chợ Lách hoặc Trà Vinh.
- [ ] Chọn PA A hay PA B, rồi nhờ kỹ sư kiểm tra kết cấu (dầm mái nhà chính, hoặc cột nhà tạm).
- [ ] Danh sách kiểm tra in cho thợ: thử áp, đo cách điện, chụp ảnh đường ống trước khi che.
- [ ] Đợt 2: kệ V lỗ phòng kho; đục cửa sau hành lang; sơn; san lấp ao; nâng nền +0,45m và sân +0,5m; switch PoE và camera; cảm biến rò nước.
- [ ] Nếu sửa vị trí khối nhà: chạy lại `export_kmz.py`, và cập nhật `F`/`P` trong `map.html` rồi chạy `genkml.js`.

## 7. Repo liên quan
- `hocutien/Tracuu`: ứng dụng tra cứu thửa đất. Nút `bnha` gọi hàm `napNha()`, hàm này nạp `phuong-an.kml` từ GitHub Pages.
- `hocutien/quyhoach`: **không** nhúng nhà vào repo này (đã từng làm nhầm và đã revert).

## 8. Lịch sử audit (đợt tự kiểm tra 15/11/2026)
Đã sửa:
- Ổ cắm bếp đặt quá sát chậu (0,35m) → dời ra ≥0,6m.
- Cửa WC mở ra ngoài quét ngang bậc, dễ té → đổi sang cửa lùa, thêm chiếu nghỉ 0,5m.
- Kệ khăn chắn đường cửa → dời sang vách ngăn.
- Cây che mất nắng dây phơi → dời cây ra xa.
- Các hạng mục đợt 2 còn ghi như đợt 1 → ghi rõ “đợt 2”.
- Thiếu hạng mục cho thai phụ (lưới chống muỗi, đèn cảm biến đêm, chống trơn) → đã thêm vào dự toán và vào mô hình.
- README ghi giá cũ → đã cập nhật.
- Tệp `phuong-an-3d.kml` dạng khối lỗi thời → đã xoá.
- Các script nằm ngoài repo → đã chuyển vào `tools/`.

- 15/11 tối: nhà xe chuyển vào lớp `fut` (đợt 2, bật nút Tương lai). Ống thông hơi bể tự hoại dời từ giữa cửa nhà phụ (10,9; 7,68) lên góc trái nhà chính (13,88; 6,0), cao 5,3m. Ống âm (đáy dưới +0,45m) trong nhóm `mep` dùng depthTest=false để hiện xuyên nền; thêm 2 hố thu + ống Ø114 ra ao, hố ga góc rẽ ống xí, bơm tăng áp.
- 15/11 khuya: gói vào ở. Nhà phụ: vách gạch ống 10cm trát (vách trái b7,85–15,3; vách sau a11,35–14; mặt trước) trên đà kiềng, dải bông gió xi măng tháo từ nhà 914 (màu xám, `bong(...,col)`), 1 quạt trần (17/11: bỏ 2 quả cầu hút nhiệt). Mí lộ + rào tạm chuyển vào lớp `fut`. Máy giặt–sấy trên giá chồng, ống thoát hơi Ø100. Bàn làm việc ở phòng khách, kệ sắt + tủ mạng ở phòng kho. Dự toán: loại `Tự làm` (0đ, ghi tiết kiệm), `Đồ cũ` (0đ); nhóm `Đợt 2 – ...` không cộng vào đợt 1.
- 17/11: rà soát độc lập 2 lượt (Docs "Rà soát thiết kế điện – nước – mạng"). Đã sửa: bỏ Aruba; dời bể về sân trước bếp, ống chính 19m dốc 1,5% đi nổi, bỏ nắp lật/hố ga/phễu sàn khu giặt, ống cấp lên trên ống thoát, máy nước nóng trực tiếp 4500W; điện thêm RCCB #2 cho C1–C3, RCBO C4, R4 4mm² + 32A, R5 3×2,5, tủ 24 module. Script sodo_* đổi sang đường dẫn tương đối. Còn chờ: thử thấm (chốt bãi thấm), công tơ (chốt cáp nguồn), model máy giặt, cao độ ống bồn cầu; bảng nhánh công tắc C1 (dây đảo chiều, công tắc đầu giường) chưa sửa.
