"""Run native browser acceptance, or a clearly labeled restricted-harness bridge.

Bridge mode uses the actual HTTP server through Python, IIFE-wrapped JS modules,
and Map-backed localStorage. It cannot validate native origin/CSP or real storage.
"""
import argparse
import json
import os
import re
from pathlib import Path
import httpx
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]


def bridge_bundle():
    # Each file keeps its own lexical scope, just as an ES module does. This is
    # only a test harness, not a shipped bundler or a native-origin substitution.
    exports={'charts.js':['Curve','Field','legend','fmt','colors'],
             'labs.js':['labModules','labFields','labMarkup','mountLab'],
             'datasets.js':['storedDesk'],'app.js':[]}
    pieces=['window.__testModules={};']
    for filename,names in exports.items():
        code=(ROOT/'web'/filename).read_text()
        code=re.sub(r"import\s*\{([^}]+)\}\s*from\s*'\./([^']+)';",lambda m:'const {'+m[1]+'}=window.__testModules['+json.dumps(m[2])+'];',code)
        code=code.replace('export ','')
        pieces.append('(()=>{'+code+'\nwindow.__testModules['+json.dumps(filename)+']={'+','.join(names)+'};})();')
    return '\n'.join(pieces)


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
        context=browser.new_context(viewport={'width':1500,'height':1100},accept_downloads=True)
        page=context.new_page();errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        if args.bridge:
            http = httpx.Client(base_url=args.url, timeout=90)
            def bridge(path,options):
                result=http.request(options.get('method','GET'),path,headers=options.get('headers',{}),content=options.get('body'))
                return {'ok':result.is_success,'status':result.status_code,'body':result.json()}
            page.expose_function('_localHTTP',bridge)
            page.set_content('<!doctype html><html><head><style>'+(ROOT/'web/style.css').read_text()+'</style></head><body><div id="app"></div></body></html>')
            page.add_script_tag(content="""window.fetch=async(path,options={})=>{const r=await window._localHTTP(path,options);return {ok:r.ok,status:r.status,json:async()=>r.body};};const store=new Map();Object.defineProperty(window,'localStorage',{value:{getItem:k=>store.get(k)||null,setItem:(k,v)=>store.set(k,v)}});""")
            page.add_script_tag(content=bridge_bundle())
        else:
            page.goto(args.url)
        def ready(module):
            page.wait_for_function('(m)=>window.observatory?.scene().result_id && window.observatory.scene().displayed_request.module===m && document.getElementById("cancel").disabled',arg=module,timeout=70000)
            assert not page.locator('#error').is_visible(),page.locator('#error').inner_text()
            assert not errors,errors
        ready('cancellation')
        page.locator('#difference canvas').click(position={'x':160,'y':110})
        assert page.evaluate('window.observatory.scene().selection.kind')=='cancellation trace'
        assert page.locator('#trace tbody tr').count()==64
        page.locator('#mode-select').select_option('61')
        assert page.evaluate('window.observatory.scene().selection.mode')==61
        page.locator('#prefix').get_by_role('button',name='Zoom in',exact=True).click()
        page.locator('#pin').click()
        page.get_by_role('spinbutton',name='Log-kernel width h',exact=True).fill('0.8')
        page.get_by_role('spinbutton',name='Log-kernel width h',exact=True).press('Tab')
        assert page.evaluate('window.observatory.scene().uncomputed_controls.width')==.8
        page.locator('#run').click()
        page.wait_for_function('window.observatory.scene().displayed_request.width===0.8');ready('cancellation')
        assert page.locator('#compare-left canvas').count()==1
        page.locator('#difference canvas').click(position={'x':200,'y':110})
        page.locator('#experiment-name').fill('Browser linked investigation')
        page.locator('#notes').fill('Both matrices and all signed cross terms retained.')
        original=page.evaluate('window.observatory.exportExperiment()')
        receipt=page.evaluate('window.observatory.save()')
        page.evaluate('(key)=>window.observatory.openInvestigation(key)',receipt['investigation_id'])
        ready('cancellation')
        reopened=page.evaluate('window.observatory.exportExperiment()')
        assert reopened['result']==original['result'] and reopened['comparison']==original['comparison']
        assert reopened['selection']==original['selection']
        assert reopened['viewports']==original['viewports']
        assert page.locator('#artifact-notice').is_visible()
        # Real browser JSON round-trip, server integrity validation, inspection.
        page.evaluate('(x)=>window.observatory.inspectArtifact(JSON.parse(JSON.stringify(x)))',original)
        ready('cancellation')
        capture=page.evaluate('window.observatory.capture()')
        assert capture['images'] and all(im['png_data_url'].startswith('data:image/png;base64,') for im in capture['images'])
        assert capture['scene']['result_id']==original['result']['result_id']
        page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(args.screenshots/'cancellation.png'),full_page=True)
        page.evaluate('(x)=>window.observatory.replay(x)',original);ready('cancellation')
        replayed=page.evaluate('window.observatory.exportExperiment()')
        assert replayed['result']['result_id']==original['result']['result_id']
        assert replayed['comparison']['result_id']==original['comparison']['result_id']
        assert replayed['selection']==original['selection']
        print('cancellation: trace, mode, two artifacts, disk reopen, replay and capture PASS',flush=True)
        for module in ['explicit','sweep','family','hierarchy','refine','geometry','primes','euler','mobius','zeros','height']:
            page.locator(f'[data-module="{module}"]').click();ready(module)
            print(module,'PASS',flush=True)
            if module=='explicit':
                assert page.locator('body').inner_text().count('UNKNOWN — no bound supplied')==5
                page.locator('#explicit-sides canvas').click(position={'x':280,'y':120})
                focused=page.evaluate('window.observatory.scene().selection.b')
                page.locator('#focus-explicit').click()
                page.wait_for_function('(b)=>window.observatory.scene().displayed_request?.focus_b===b',arg=focused);ready(module)
                page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(args.screenshots/'explicit.png'),full_page=True)
            if module=='sweep':
                page.locator('[data-trial="0"]').click()
                assert page.evaluate('window.observatory.scene().selection.index')==0
                page.locator('#open-holdout').click();ready('cancellation')
                assert page.evaluate('window.observatory.scene().displayed_request.start')==1001
            if module=='geometry':
                page.locator('#field canvas').click(position={'x':200,'y':120})
                selected=page.evaluate('window.observatory.scene().selection')
                assert selected['kind']=='sampled grid cell'
                parent=page.evaluate('window.observatory.scene().result_id')
                page.locator('#refine-selected').click()
                page.wait_for_function('window.observatory.scene().refinement_ids.length===1 && document.getElementById("cancel").disabled',timeout=70000)
                assert page.evaluate('window.observatory.scene().result_id')==parent
                assert page.locator('#refinements details').count()==1
                assert not page.locator('#error').is_visible(),page.locator('#error').inner_text()
        page.locator('[data-module="datasets"]').click()
        page.locator('#dataset-demo').click()
        page.wait_for_function('window.observatory.scene().dataset?.event_count===2',timeout=30000)
        page.locator('#stored-events button').first.click()
        page.wait_for_function('window.observatory.scene().dataset?.selection?.exact_decimal')
        assert page.evaluate('window.observatory.scene().dataset.selection.anchor')=='763173730199776587433631628770'
        page.locator('#stored-curve').get_by_role('button',name='Zoom in',exact=True).click()
        page.wait_for_function('window.observatory.scene().dataset.start>0')
        page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(args.screenshots/'stored-data.png'),full_page=True)
        print('stored data: ingestion, exact selection, indexed zoom PASS',flush=True)
        page.evaluate("void window.observatory.run({module:'geometry',grid:80,samples:2048,dps:70})")
        page.wait_for_function('!document.getElementById("cancel").disabled')
        page.locator('#cancel').click();page.wait_for_function('document.getElementById("cancel").disabled')
        page.evaluate("window.observatory.run({module:'cancellation',n:32,split:16})");ready('cancellation')
        page.set_viewport_size({'width':390,'height':844})
        assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),page.evaluate('[document.documentElement.scrollWidth,innerWidth]')
        page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(args.screenshots/'mobile.png'),full_page=True)
        if not args.bridge:
            # Downloads and localStorage are accepted only in native-origin mode.
            with page.expect_download() as event: page.locator('#export').click()
            event.value.save_as(args.screenshots/'native-export.json')
            assert json.loads((args.screenshots/'native-export.json').read_text())['result']['result_id']
            page.evaluate("localStorage.setItem('observatory-smoke-durable','yes')")
            page.reload();ready('cancellation')
            assert page.evaluate("localStorage.getItem('observatory-smoke-durable')")=='yes'
        assert not errors,errors
        report={'browser_mode':'bridge' if args.bridge else 'native-origin','numerical_modules':12,'stored_data_desk':True,'page_errors':errors,'two_result_replay':True,'disk_reopen':True,'viewport_and_selection_restore':True,'native_download_storage_acceptance':not args.bridge}
        (args.screenshots/'report.json').write_text(json.dumps(report,indent=2))
        print(json.dumps(report),flush=True);browser.close()

if __name__=='__main__':main()
