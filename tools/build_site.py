"""Build the public, read-only site (index.html) from the codex page and a data export.

Usage: python3 build_site.py <data_dir> <out_file> [<assets_dir>]
<data_dir> holds characters/*.json and skills/*.json as saved by an ArtifactData list.
<assets_dir> holds skill icon files saved by Artifact read, named <asset id>.<ext>.
Icons are copied next to <out_file> as img/<skill id>.webp.
"""
import glob, json, os, re, shutil, sys

data_dir, out = sys.argv[1], sys.argv[2]
assets_dir = sys.argv[3] if len(sys.argv) > 3 else None
HERE = os.path.dirname(os.path.abspath(__file__))


def body(path):
    d = json.load(open(path, encoding='utf-8'))
    return d['data'] if isinstance(d.get('data'), dict) else d


chars = [dict(body(p), id=os.path.basename(p)[:-5]) for p in sorted(glob.glob(data_dir + '/characters/*.json'))]
skills = [dict(body(p), id=os.path.basename(p)[:-5]) for p in sorted(glob.glob(data_dir + '/skills/*.json'))]

img_dir = os.path.join(os.path.dirname(os.path.abspath(out)), 'img')
icons = 0
for sk in skills:
    sk.pop('iconPrompt', None)
    aid = sk.pop('icon', '') or ''
    sk.pop('iconUrl', None)
    if not aid:
        continue
    found = glob.glob(os.path.join(assets_dir, aid + '.*')) if assets_dir else []
    target = os.path.join(img_dir, sk['id'] + '.webp')
    if found:
        os.makedirs(img_dir, exist_ok=True)
        shutil.copyfile(found[0], target)
    if os.path.exists(target):
        sk['iconUrl'] = 'img/' + sk['id'] + '.webp'
        icons += 1
    else:
        print('warning: icon file missing for', sk['id'], aid)

page = open(os.path.join(HERE, 'codex.html'), encoding='utf-8').read()
m = re.search(r'<title>(.*?)</title>', page)
title = m.group(1) if m else '아르카나 인물 도감'
page = page.replace(m.group(0), '', 1) if m else page

desc = '왓더퍽을 비롯한 판타지 등장인물의 능력, 고유 스킬, 전투 기믹, 잠재 해방을 단계별로 열어보는 설정 도감.'
data = json.dumps({'characters': chars, 'skills': skills}, ensure_ascii=False).replace('</', '<\\/')

html = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        f'<title>{title}</title>'
        f'<meta name="description" content="{desc}">'
        f'<meta property="og:title" content="{title}">'
        f'<meta property="og:description" content="{desc}">'
        '<meta property="og:type" content="website">'
        '<meta name="theme-color" content="#0d0b15">'
        '<style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}'
        'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>'
        '</head><body>'
        f'<script>window.__PUBLIC_DATA__={data};</script>'
        + page + '</body></html>')
open(out, 'w', encoding='utf-8').write(html)
print(f'{out}: {len(chars)} characters, {len(skills)} skills, {icons} icons, {len(html)} bytes')
