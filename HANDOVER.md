# Bàn giao – Nhà Duyên Hải (cải tạo để dọn vào ở)

Tài liệu này giúp người khác hoặc một tài khoản Claude khác tiếp tục làm mà không cần đọc lại lịch sử chat.

## 1. Mục tiêu
- Chủ nhà là Tiến. Hai vợ chồng dọn vào ở sớm; **vợ đang mang thai**.
- Ngân sách đợt 1 khoảng **100–115tr**. Dự toán hiện tại 91–149tr, đã cộng 10% dự phòng. Đợt 2 khoảng 22–39tr.
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
   - mạch C8 dự phòng cho máy lạnh thứ hai.
4. An toàn trước, thẩm mỹ sau:
   - điện: RCBO, nối đất, chống sét lan truyền;
   - bể tự hoại cách giếng ≥15m (hiện ~16m);
   - chữa cháy: báo khói, báo rò gas, 2 bình chữa cháy 4kg, ô cửa sổ thoát hiểm;
   - thai phụ: lưới chống muỗi, gạch chống trơn, tay vịn, đèn cảm biến đêm.
5. Phần âm (điện, nước, mạng, chống thấm, bể tự hoại) làm đúng một lần. Phần hoàn thiện làm dần.
6. Không còn bụi hay hoá chất khi vợ đã vào ở: làm xong phần bụi và phần sơn/keo, thông gió ≥2 tuần rồi mới dọn vào.
7. Công năng theo cách dùng thật:
   - cửa WC không nhìn ra bàn ăn;
   - khu tắm sát máy giặt + sấy, **không làm phòng giặt riêng**;
   - đường đi đêm từ phòng ngủ đến WC ngắn và có đèn.
8. Ống đi nổi, dễ kiểm tra. Thử áp ống nước và đo cách điện trước khi che lại.
9. Làm đúng ranh GCN và đúng thủ tục: xả thải, san lấp ao, sửa nhà.
10. Số liệu là ước tính, phải hỏi giá thợ địa phương. PA A và PA B cần kỹ sư kiểm tra kết cấu.

## 3. Quyết định đã chốt (đừng đổi lại nếu chủ nhà chưa đồng ý)
- **Bếp:** bếp từ đôi (mạch C4, RCBO 32A, dây 4mm²) cộng bếp gas đơn dự phòng; bình gas đặt trong lồng ngoài vách. Thứ tự trên bàn: tủ lạnh → chậu → sơ chế 90cm → bếp. Ổ cắm mặt bếp cách chậu ≥0,6m.
- **WC:**
  - xây tại chỗ WC cũ, sàn +0,5m;
  - **cửa lùa** quay vào khu giặt;
  - lên WC: chiếu nghỉ 0,5m, rồi 2 bậc ~17cm, có tay vịn;
  - quạt hút thổi ra vách ngoài;
  - máy giặt + sấy đặt chồng cạnh WC; lavabo ngoài; cửa sau ra dây phơi.
- **Thoát nước:** bể tự hoại composite 3 ngăn ~2m³ mới, đặt dưới lối đi. Hầm cũ hút sạch, rắc vôi, lấp cát, đậy bê tông.
- **Điện:** CB tổng 63A, dây Cu 2×16mm², 11 mạch C1–C11 (bảng chi tiết trong Thuyết minh mục 3). Máy nước nóng có ELCB và nối đất; máy bơm có rơ-le chống chạy khô.
- **Mạng:**
  - cáp quang từ cột vào tủ mạng trong phòng kho, gồm ONT, MikroTik hEX, Lenovo M720q, NAS, UPS; switch PoE lắp ở đợt 2;
  - AP1 trên trần hành lang, AP2 trên trần bếp;
  - ~75m CAT6, có ống chờ cho 3 camera.
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
| `tools/check_render.py` | Mở trang ở chế độ ẩn, báo lỗi JS, chụp ảnh các góc nhìn vào `tools/out/`. |

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
python3 budget.py                 # khi sửa giá; dán out/b1.html, out/b2.html vào index.html mục 11
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
