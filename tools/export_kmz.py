"""Xuất mô hình 3D (index.html) thành KMZ chi tiết cho Google Earth.

Cách chạy (cần Python + playwright + Chrome/Chromium, và three.js r128 cài cục bộ):
    cd tools && npm i three@0.128.0 && pip install playwright
    python3 export_kmz.py            # tạo ../nha-duyen-hai-3d.kmz

Cách làm: mở index.html trong trình duyệt ẩn, lấy toàn bộ tam giác của các khối
quanh nhà (bỏ cây, chữ, điện nước), quy đổi toạ độ công trình (a,b,z) sang kinh/vĩ độ
theo ORIGIN/BRG0 trong map.html, ghi thành các Polygon có cao độ (relativeToGround).
"""
import json, math, os, re, zipfile
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, 'tools')
THREE = os.path.join(TOOLS, 'node_modules', 'three')
CHROME = os.environ.get('CHROME', '/usr/bin/google-chrome')

JS = r"""
() => {
 site.updateMatrixWorld(true);
 const inv=new THREE.Matrix4().copy(site.matrixWorld).invert(), out={}, v=new THREE.Vector3(), trees=new Set(treeObjs);
 function folderOf(o){let p=o;while(p&&p!==site){if(trees.has(p))return null;if(p===optA)return 'A';if(p===optB)return 'B';if(p===mep||p===fut)return null;p=p.parent;}return 'D';}
 site.traverse(o=>{
  if(!o.isMesh||o.isInstancedMesh)return; const f=folderOf(o); if(!f)return;
  const g=o.geometry; if(!g||!g.attributes.position)return;
  const M=new THREE.Matrix4().multiplyMatrices(inv,o.matrixWorld); g.computeBoundingBox(); const bb=g.boundingBox.clone().applyMatrix4(M);
  if(f==='D'){ if(bb.min.x<-3||bb.max.x>26||-bb.max.z<-9||-bb.min.z>26) return; if(bb.max.x-bb.min.x>25||bb.max.z-bb.min.z>25) return; }
  const key=f+'|'+o.material.color.clone().convertLinearToSRGB().getHexString()+'|'+(o.material.opacity??1).toFixed(2), arr=out[key]||(out[key]=[]);
  const pos=g.attributes.position, idx=g.index, n=idx?idx.count:pos.count;
  for(let i=0;i<n;i+=3){const t=[];for(let k=0;k<3;k++){const j=idx?idx.getX(i+k):i+k;v.fromBufferAttribute(pos,j).applyMatrix4(M);t.push([+v.x.toFixed(3),+(-v.z).toFixed(3),+v.y.toFixed(3)]);}arr.push(t);}
 });
 return out;}
"""

def local_page():
    html = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    if os.path.isdir(THREE):
        html = html.replace('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js', 'node_modules/three/build/three.min.js')
        html = html.replace('https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js', 'node_modules/three/examples/js/controls/OrbitControls.js')
    p = os.path.join(TOOLS, '_page.html'); open(p, 'w', encoding='utf-8').write(html); return p

def main():
    page = local_page()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME if os.path.exists(CHROME) else None,
                              args=['--no-sandbox', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
        pg = b.new_page(); pg.goto('file://' + page); pg.wait_for_timeout(3000)
        T = pg.evaluate(JS); b.close()
    os.remove(page)
    m = open(os.path.join(ROOT, 'map.html'), encoding='utf-8').read()
    o = re.search(r"ORIGIN=\{lat:([\d.]+),lon:([\d.]+)\}", m); LAT0, LON0 = float(o.group(1)), float(o.group(2))
    BRG0 = float(re.search(r"const BRG0=([\d.]+)", m).group(1))
    ML = 110600; MO = 111320 * math.cos(math.radians(LAT0))
    R = math.radians(BRG0); RI = R - math.pi / 2
    def ll(a, b, z):
        e = a * math.sin(R) + b * math.sin(RI); n = a * math.cos(R) + b * math.cos(RI)
        return f"{LON0 + e / MO:.8f},{LAT0 + n / ML:.8f},{max(z, 0) + 0.05:.2f}"
    names = {'D': 'Nhà chính + nhà tạm + sân (đợt 1)', 'A': 'PA A – Sân thượng mái nhà chính', 'B': 'PA B – Lầu gỗ trên nhà tạm'}
    styles, folders = [], {'D': [], 'A': [], 'B': []}
    for i, (k, tris) in enumerate(T.items()):
        if not tris: continue
        f, c, op = k.split('|'); op = float(op)
        styles.append(f'<Style id="c{i}"><LineStyle><width>0</width></LineStyle><PolyStyle><color>{int(round(op*255)):02x}{c[4:6]}{c[2:4]}{c[0:2]}</color><outline>0</outline></PolyStyle></Style>')
        polys = ''.join('<Polygon><altitudeMode>relativeToGround</altitudeMode><outerBoundaryIs><LinearRing><coordinates>'
                        + ' '.join(ll(*q) for q in t + [t[0]]) + '</coordinates></LinearRing></outerBoundaryIs></Polygon>' for t in tris)
        vis = 0 if f == 'B' else 1
        folders[f].append(f'<Placemark><visibility>{vis}</visibility><styleUrl>#c{i}</styleUrl><MultiGeometry>{polys}</MultiGeometry></Placemark>')
    ranh = open(os.path.join(ROOT, 'phuong-an.kml'), encoding='utf-8').read()
    rb = re.search(r'<Document><name>[^<]*</name>(.*)</Document>', ranh, re.S).group(1)
    k = ('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>Nhà Duyên Hải – mô hình 3D chi tiết</name>'
         + ''.join(styles) + '<Folder><name>Ranh đất + mặt bằng</name>' + rb + '</Folder>'
         + ''.join(f'<Folder><name>{names[f]}</name><visibility>{0 if f == "B" else 1}</visibility>' + ''.join(folders[f]) + '</Folder>' for f in 'DAB')
         + '</Document></kml>')
    out = os.path.join(ROOT, 'nha-duyen-hai-3d.kmz')
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z: z.writestr('doc.kml', k)
    print(sum(len(v) for v in T.values()), 'tam giác ->', out, os.path.getsize(out) // 1024, 'KB')

if __name__ == '__main__':
    main()
