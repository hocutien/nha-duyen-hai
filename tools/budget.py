# Sinh bang du toan cho panel thuyet minh tu out/dutoan.json (chay dutoan.py truoc)
import json, os
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, "out")
R = [x for x in json.load(open(os.path.join(OUT, "dutoan.json"))) if not x[0].startswith("Đợt 2")]
f = lambda x: f"{x:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")
grp = {}
for x in R:
    g = grp.setdefault(x[0], {"Vật tư": 0, "Thiết bị": 0, "Nhân công": 0, "Khác": 0, "Đồ cũ": 0, "Tự làm": 0})
    g[x[5]] += x[8]
tot = sum(x[8] for x in R)
vat = sum(x[8] for x in R if x[6].startswith("PL") and x[5] != "Nhân công") * 0.1
dp = (tot + vat) * 0.1
rows = "".join(f"<tr><td>{k}</td><td>{f((v['Vật tư']+v['Thiết bị'])/1000)}</td><td>{f(v['Nhân công']/1000)}</td><td>{f(v['Khác']/1000)}</td><td>{f(sum(v.values())/1000)}</td></tr>\n" for k, v in grp.items())
html = ("<table><tr><th>Hạng mục</th><th>Vật tư + TB</th><th>Nhân công</th><th>Khác</th><th>Cộng</th></tr>\n" + rows +
        f"<tr><th colspan=4>Cộng trước thuế</th><th>{f(tot/1000)}</th></tr>\n"
        f"<tr><th colspan=4>VAT 10% phần vật tư lấy giá công bố (chưa VAT)</th><th>{f(vat/1000)}</th></tr>\n"
        f"<tr><th colspan=4>Dự phòng 10%</th><th>{f(dp/1000)}</th></tr>\n"
        f"<tr><th colspan=4>Tổng đợt 1 (vào ở)</th><th>{f((tot+vat+dp)/1000)}</th></tr></table>")
open(os.path.join(OUT, "b1.html"), "w").write(html)
print(round(tot), round(vat), round(tot + vat + dp))
