"""Browser flows against a running local server.

Normal: python scripts/browser_smoke.py --url http://127.0.0.1:8765
Restricted harness: add --bridge. This substitutes an HTTP bridge and in-memory
localStorage for browser networking/storage; it is NOT a native-origin smoke test.
"""
import argparse
import json
import os
from pathlib import Path
import httpx
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--url',default='http://127.0.0.1:8765')
    parser.add_argument('--browser',default=os.environ.get('CHROMIUM_PATH'))
    parser.add_argument('--bridge',action='store_true')
    parser.add_argument('--screenshots',type=Path,default=ROOT/'artifacts')
    args=parser.parse_args();args.screenshots.mkdir(exist_ok=True,parents=True)
    with sync_playwright() as p:
        options={'headless':True}
        if args.browser:options['executable_path']=args.browser
        browser=p.chromium.launch(**options)
        page=browser.new_page(viewport={'width':1500,'height':1100})
        errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        if args.bridge:
            def bridge(path,options):
                result=httpx.request(options.get('method','GET'),args.url+path,headers=options.get('headers',{}),content=options.get('body'),timeout=90)
                return {'ok':result.is_success,'status':result.status_code,'body':result.json()}
            page.expose_function('_localHTTP',bridge)
            page.set_content('<!doctype html><html><head><style>'+(ROOT/'web/style.css').read_text()+'</style></head><body><div id="app"></div></body></html>')
            page.add_script_tag(content="""window.fetch=async (path,options={})=>{const r=await window._localHTTP(path,options);return {ok:r.ok,status:r.status,json:async()=>r.body};};const store=new Map();Object.defineProperty(window,'localStorage',{value:{getItem:k=>store.get(k)||null,setItem:(k,v)=>store.set(k,v)}});""")
            page.add_script_tag(content=(ROOT/'web/charts.js').read_text().replace('export ','')+'\n'+(ROOT/'web/app.js').read_text().split('\n',1)[1])
        else:
            page.goto(args.url)
        def ready(module):
            page.wait_for_function(f'window.observatory?.scene().result_id && window.observatory.scene().displayed_request.module==="{module}"',timeout=70000)
            assert not page.locator('#error').is_visible(),page.locator('#error').inner_text()
        ready('geometry')
        first=page.evaluate('window.observatory.scene().result_id')
        assert page.locator('#workspace').get_attribute('data-scene-id')==first
        page.locator('#field canvas').click(position={'x':160,'y':100})
        assert page.evaluate('window.observatory.scene().selection.kind')=='sampled grid cell'
        page.locator('#primary').get_by_role('button',name='Zoom in',exact=True).click()
        page.locator('#primary canvas').click(position={'x':170,'y':120})
        original=page.evaluate('window.observatory.exportExperiment()')
        page.locator('#experiment-name').fill('Browser smoke observation')
        page.locator('#notes').fill('Check persistence, precision, and selected viewport.')
        page.get_by_role('button',name='Save locally',exact=True).click()
        assert page.locator('#shelf').inner_text().startswith('Browser smoke observation')
        page.screenshot(path=str(args.screenshots/'desktop.png'),full_page=True)
        for module in ['primes','euler','mobius','zeros','height']:
            page.locator(f'[data-module="{module}"]').click();ready(module)
            print(module,page.locator('#run-status').inner_text(),flush=True)
            assert page.locator('canvas').count()>0
            if module=='height':
                assert '763173730199776587433631628769.931797' in page.locator('#inspector').inner_text()
            if module=='mobius':page.screenshot(path=str(args.screenshots/'cancellation.png'),full_page=True)
        print('replay start',flush=True);page.evaluate('(x)=>window.observatory.replay(x)',original);ready('geometry');print('replay done',flush=True)
        replayed=page.evaluate('window.observatory.exportExperiment()')
        assert replayed['result_id']==original['result_id']
        assert replayed['viewports']==original['viewports']
        assert replayed['selection']==original['selection']
        print('baseline start',flush=True);page.get_by_role('button',name='Pin baseline',exact=True).click()
        page.get_by_role('spinbutton',name='Slice σ',exact=True).fill('0.6')
        page.get_by_role('spinbutton',name='Slice σ',exact=True).press('Tab')
        assert page.evaluate('window.observatory.scene().uncomputed_controls.sigma')==.6
        page.get_by_role('button',name='Run experiment',exact=False).click()
        page.wait_for_function('window.observatory.scene().displayed_request.sigma===0.6',timeout=70000)
        assert page.evaluate('window.observatory.scene().baseline.result_id')==first;print('baseline done',flush=True)
        page.evaluate("void window.observatory.run({module:'geometry',grid:80,samples:2048,dps:70})")
        page.wait_for_function('!document.getElementById("cancel").disabled')
        page.get_by_role('button',name='Cancel',exact=True).click()
        page.wait_for_function('document.getElementById("cancel").disabled');print('cancel done',flush=True)
        page.evaluate("window.observatory.run({module:'height'})");ready('height')
        page.set_viewport_size({'width':390,'height':844})
        assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
        page.screenshot(path=str(args.screenshots/'mobile.png'),full_page=True)
        assert not errors,errors
        print(json.dumps({'browser_mode':'bridge' if args.bridge else 'native-origin','modules':6,'page_errors':errors,'replay_hash_matches':True,'viewport_and_selection_restored':True,'mobile_overflow':False}),flush=True)
        browser.close()

if __name__=='__main__':main()
