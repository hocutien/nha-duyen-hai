"""Kiểm tra nhanh index.html: không lỗi JS, chụp ảnh các góc nhìn vào tools/out/.

    cd tools && npm i three@0.128.0 && pip install playwright
    python3 check_render.py
"""
import os, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, 'tools'); OUT = os.path.join(TOOLS, 'out'); os.makedirs(OUT, exist_ok=True)
CHROME = os.environ.get('CHROME', '/usr/bin/google-chrome')
VIEWS = os.environ.get('VIEWS','tong,trong,dn,song,pa,pb').split(',')   # id các nút trên thanh công cụ

html = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
if os.path.isdir(os.path.join(TOOLS, 'node_modules', 'three')):
    html = html.replace('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js', 'node_modules/three/build/three.min.js')
    html = html.replace('https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js', 'node_modules/three/examples/js/controls/OrbitControls.js')
page = os.path.join(TOOLS, '_page.html'); open(page, 'w', encoding='utf-8').write(html)
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME if os.path.exists(CHROME) else None,
                          args=['--no-sandbox', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    pg = b.new_page(viewport={'width': 1280, 'height': 800})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: m.type == 'error' and errs.append(m.text))
    pg.goto('file://' + page); pg.wait_for_timeout(int(os.environ.get('WAIT0','3000')))
    print('frame ms', pg.evaluate('''()=>{const t=performance.now();renderer.render(scene,camera);return Math.round(performance.now()-t)}'''), 'meshes', pg.evaluate('''()=>{let n=0;scene.traverse(o=>{if(o.isMesh)n++});return n}'''))
    if os.environ.get('CAM'):
        pg.evaluate('c=>{lblOn=false;syncLbl();setRoof(!'+('true' if os.environ.get('NOROOF') else 'false')+');const v=c.split(",").map(Number);camera.position.copy(S(v[0],v[1],v[2]));controls.target.copy(S(v[3],v[4],v[5]));controls.update();}', os.environ['CAM']); pg.wait_for_timeout(800); pg.screenshot(path=os.path.join(OUT,'cam.png'), timeout=120000)
    for v in VIEWS:
        btn = pg.query_selector(f'#{v}') or pg.query_selector(f'[data-v="{v}"]')
        if not btn: errs.append('thiếu nút #' + v); continue
        pg.evaluate('''el=>el.click()''', btn); pg.wait_for_timeout(int(os.environ.get('WAIT','1200')))
        pg.screenshot(path=os.path.join(OUT, v + '.png'), timeout=120000)
        pg.evaluate('''el=>el.click()''', btn) if v in ('dn', 'pa', 'pb') else None
    b.close()
os.remove(page)
print('Ảnh ->', OUT); print('LỖI:' if errs else 'Không lỗi JS', *errs, sep='\n')
sys.exit(1 if errs else 0)
