from __future__ import annotations
import difflib, hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'source_snapshot'; V1=ROOT/'v0.1'; V2=ROOT/'v0.2'
EXPECTED=[1,*range(4,31)]
CRE=re.compile(r'^Chapter (\d+)\s+[–-]\s+(.+)$')
LINK=re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')

def chapters(d):
    found=[]
    for p in d.glob('Chapter *.md'):
        m=CRE.match(p.stem)
        if m: found.append((int(m.group(1)),p))
    found.sort()
    if [n for n,_ in found]!=EXPECTED: raise ValueError(f'Bad sequence in {d}')
    return [p for _,p in found]

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def visible(s): return LINK.sub(lambda m:m.group(2) or m.group(1).split('#',1)[0],s)
def assemble(title, files):
    z=[f'# {title}']
    for p in files:
        m=CRE.match(p.stem); z.extend((f'## {m.group(2)}',visible(p.read_text(encoding='utf-8').strip())))
    return '\n\n'.join(z)+'\n'
def write(p,s): p.write_text(s,encoding='utf-8',newline='')

def validate():
    b=chapters(BASE); v=chapters(V1)
    expected={}
    for line in (ROOT/'source_snapshot.sha256').read_text(encoding='utf-8').splitlines():
        h,n=line.split('  ',1); expected[n]=h.upper()
    if len(expected)!=28 or any(expected.get(p.name)!=digest(p) for p in b): raise ValueError('Source snapshot hash mismatch')
    if [p.name for p in b]!=[p.name for p in v]: raise ValueError('v0.1 parent order mismatch')
    parent={line.split('  ',1)[1]:line.split('  ',1)[0].upper() for line in (ROOT/'v0.1_parent.sha256').read_text(encoding='utf-8').splitlines()}
    if len(parent)!=28 or any(parent.get(p.name)!=digest(p) for p in v): raise ValueError('v0.1 parent hash mismatch')
    if 'recorded before v0.2 manuscript revision' not in (ROOT/'feedback_before_revision.md').read_text(encoding='utf-8'): raise ValueError('Pre-revision feedback record missing')
    guide2=(ROOT/'style_guide_v0.2.sha256').read_text().split()[0].upper()
    if digest(ROOT/'style_guide_v0.2.md')!=guide2: raise ValueError('Frozen v0.2 guide hash mismatch')
    gh=(ROOT/'style_guide_v0.1.sha256').read_text().split()[0].upper()
    if hashlib.sha256((ROOT/'style_guide_v0.1.md').read_bytes()).hexdigest().upper()!=gh: raise ValueError('Frozen v0.1 guide changed')
    ch16=next(p for p in b if CRE.match(p.stem).group(1)=='16')
    if ch16.read_bytes()!=(V1/ch16.name).read_bytes(): raise ValueError('Chapter 16 control altered')
    return b,v

def diff(files,a,b,al,bl):
    out=[]
    for p in files:
        x=(a/p.name).read_text(encoding='utf-8').splitlines(True); y=(b/p.name).read_text(encoding='utf-8').splitlines(True)
        out.extend(difflib.unified_diff(x,y,fromfile=f'{al}/{p.name}',tofile=f'{bl}/{p.name}'))
    return ''.join(out)

def stat(s):
    paras=[p for p in re.split(r'\n\s*\n',s.strip()) if p.strip()]
    toks=re.findall(r"\b[\w’'-]+\b",s,flags=re.UNICODE)
    sents=re.findall(r'[^.!?]+(?:[.!?]+[\"\'”’)]*)|[^.!?]+$',s)
    lens=[len(re.findall(r"\b[\w’'-]+\b",x)) for x in sents if x.strip()]
    return {'words':len(toks),'paragraphs':len(paras),'sentences_approx':len(lens),'mean_sentence_words':round(sum(lens)/len(lens),2) if lens else 0,'median_sentence_words':sorted(lens)[len(lens)//2] if lens else 0,'sentences_le_6_words':sum(n<=6 for n in lens),'sentence_length_contour':lens}

MODES={1:['recollection/recovery','immediate action'],4:['contested exchange','recollection/recovery'],5:['contested exchange','sustained observation'],6:['recollection/recovery','contested exchange'],7:['immediate action','signal/countdown'],8:['immediate action','recollection/recovery'],9:['recollection/recovery','sustained observation'],10:['contested exchange','signal/countdown'],11:['signal/countdown','contested exchange'],12:['sustained observation'],13:['immediate action','sustained observation'],14:['sustained observation','recollection/recovery'],15:['recollection/recovery','immediate action'],16:['sustained observation','signal/countdown'],17:['sustained observation','contested exchange','signal/countdown'],18:['signal/countdown','immediate action'],19:['sustained observation'],20:['sustained observation','contested exchange'],21:['contested exchange','sustained observation'],22:['sustained observation','immediate action'],23:['immediate action','contested exchange'],24:['sustained observation','contested exchange'],25:['immediate action','signal/countdown'],26:['signal/countdown','recollection/recovery'],27:['contested exchange'],28:['immediate action','contested exchange'],29:['recollection/recovery','signal/countdown'],30:['sustained observation','recollection/recovery']}

def main():
    b,v=validate() # hash and parent checks precede output writes
    V2.mkdir(exist_ok=True)
    for p in v: (V2/p.name).write_bytes((V1/p.name).read_bytes())
    notes={}
    # Chapter 20: restore the key civic-fiction distinction and develop it through an existing contrast.
    p20=next(p for p in v if p.name.startswith('Chapter 20 ')); x=(V2/p20.name).read_text(encoding='utf-8')
    old='After two turns, the corridor widened into a chamber hidden behind the false wall of the buried street. The architecture shifted from civic remnants to survival layered over ruins:'
    new='After two turns, the corridor widened into a chamber hidden behind the false wall of the buried street. The architecture changed immediately: not civic fiction anymore, but survival layered over ruins. The chamber held'
    if old not in x: raise ValueError('Chapter 20 passage anchor missing')
    x=x.replace(old,new,1)
    write(V2/p20.name,x)
    notes[20]='Recast the corridor transition to retain the civic-fiction distinction and connect movement to the existing architectural contrast; no new detail.'
    # Chapter 21: retain v0.1 scene/dialogue order; restore the clue's original presentation without interpretation.
    p21=next(p for p in v if p.name.startswith('Chapter 21 ')); b21=next(p for p in b if p.name==p21.name)
    x=(V2/p21.name).read_text(encoding='utf-8')
    oldclue='Fresh bright thread showed where the cut had been reopened: not random damage, but a deliberate bid for attention.'
    newclue='Fresh bright thread showed where the cut had been reopened.\n\nNot random.\n\nNot damage.\n\nAttention.'
    if oldclue not in x: raise ValueError('Chapter 21 clue passage anchor missing')
    write(V2/p21.name,x.replace(oldclue,newclue,1))
    notes[21]='Restored the clue’s original observed-detail and short-beat presentation; retained its existing scene order and the later explicit “on purpose” dialogue timing.'
    # Chapter 1: add the author's requested uncertain flashes and pain interruption.
    p1=next(p for p in v if p.name.startswith('Chapter 1 ')); x=(V2/p1.name).read_text(encoding='utf-8')
    old1='Darkness. Silence.\n\nFor one dislocated second, he could not tell whether the launch had ended or begun again.'
    new1='Darkness. Silence.\n\nAwareness. Extreme darkness. Brief, faint flashes in the distance.\n\nShould I go to it?\n\nSnap. Extreme pain.\n\nFor one dislocated second, he could not tell whether the launch had ended or begun again.\n\nThen again.'
    if old1 not in x: raise ValueError('Chapter 1 transition anchor missing')
    write(V2/p1.name,x.replace(old1,new1,1))
    notes[1]='Added the author-requested uncertain flashes, impulse, and pain interruption in the existing transition; retained the launch/awakening uncertainty.'
    for p in v:
        n=int(CRE.match(p.stem).group(1))
        if n not in notes: notes[n]='Reviewed against baseline and v0.1. Retained the passage where its attention, action cadence, dialogue, interface form, or viewpoint already served the scene; no forced lengthening.'
    notes[16]='Control. Byte-identical to baseline and v0.1.'
    (ROOT/'v0.2_parent.sha256').write_text(''.join(f'{digest(p)}  {p.name}\n' for p in chapters(V2)),encoding='utf-8',newline='')
    write(ROOT/'v0.2_reading_copy.md',assemble('Hive: Earth — Style Trial v0.2',chapters(V2)))
    write(ROOT/'comparison_v0.1-v0.2.diff',diff(b,V1,V2,'v0.1','v0.2'))
    write(ROOT/'comparison_baseline-v0.2.diff',diff(b,BASE,V2,'source_snapshot','v0.2'))
    ledger=['# v0.2 Chapter Review Ledger','','Parents: `source_snapshot.sha256`, `v0.1_parent.sha256`. Guide frozen in `style_guide_v0.2.sha256`. Chapter 16 is byte-identical across versions.','','| Ch. | Status | Editorial operation / note |','|---:|---|---|']
    for n in EXPECTED:
        status='Control' if n==16 else 'Revised' if n in notes and n in (1,20,21) else 'Retained'
        ledger.append(f'| {n} | {status} | {notes[n]} |')
    write(ROOT/'review_ledger_v0.2.md','\n'.join(ledger)+'\n')
    # Machine-readable chapter measures and anchor alignment.
    rows=[]
    for p in b:
        a=p.read_text(encoding='utf-8'); x=(V1/p.name).read_text(encoding='utf-8'); y=(V2/p.name).read_text(encoding='utf-8')
        sm1=difflib.SequenceMatcher(a=a.splitlines(),b=x.splitlines(),autojunk=False); sm2=difflib.SequenceMatcher(a=x.splitlines(),b=y.splitlines(),autojunk=False)
        def anchors(sm): return {'unchanged_line_anchors':sum(i2-i1 for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag=='equal'),'changed_runs':sum(tag!='equal' for tag,*_ in sm.get_opcodes())}
        n=int(CRE.match(p.stem).group(1))
        rows.append({'chapter':n,'title':CRE.match(p.stem).group(2),'baseline':stat(a),'v0_1':stat(x),'v0_2':stat(y),'baseline_to_v0_1_alignment':anchors(sm1),'v0_1_to_v0_2_alignment':anchors(sm2),'v0_1_patterns_retained':n not in (1,20,21),'manual_scene_mode':'see analysis examples; transitions allowed'})
    data={'method':{'tokenization':'Unicode word runs; internal apostrophes and hyphens retained; punctuation excluded.','sentence_boundaries':'Approximate .!? segmentation; abbreviations, decimals, ellipses, fragments, and dialogue complicate boundaries.','alignment':'Exact unchanged line anchors; changed runs flagged. Paragraph counts and changes are computed per chapter; join/split meaning requires manual review.','limits':'Counts describe structure; they do not establish reading speed or sophistication. Dialogue/narration/interface category is manually reviewed only in examples and ledger.'},'chapters':rows}
    (ROOT/'measurements_v0.2.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
    (ROOT/'scene_annotations_v0.2.json').write_text(json.dumps({str(n): {'modes': MODES.get(n, ['sustained observation']), 'transitions_allowed': True} for n in EXPECTED}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='')
    # Human-readable analysis with joined examples and contour data links.
    report='''# Manuscript Style Trial v0.2 — Analysis\n\n## Scope and method\n\nThis experiment compares the frozen baseline, completed v0.1, and v0.2 across Chapter 1 and Chapters 4–30 (28 files). Exact unchanged lines anchor chapter-level alignments; the JSON file records per-chapter anchor counts and sentence-length contours. Paragraph joins/splits and operation labels are manually reviewed in the ledger.\n\nTokens are Unicode word runs, retaining internal apostrophes and hyphens. Sentence boundaries are approximate at `.`, `!`, and `?`; abbreviations, decimals, ellipses, fragments, and dialogue complicate automatic segmentation. Counts describe structure, not reading speed or sophistication.\n\n## What changed between baseline and v0.1\n\nThe frozen v0.1 ledger records joins and recasts chiefly in narration: waking perception, recovery, inference chains, environmental scans, and infrastructure description. It also records purposeful retention of tactical beats, interrupted exchanges, countdowns, and interface messages. Previously suitable passages were not treated as evidence that every other passage should be expanded. v0.1’s Chapter 20 recast compressed a spatial inventory, while Chapter 21 compressed the bright-thread clue and added an interpretive phrase.\n\n## Aligned examples\n\n### Chapter 20 — spatial reveal\n\n**Baseline:** “The corridor widened after two turns into a chamber hidden behind the false wall of the buried street. The architecture changed immediately. Not civic fiction anymore. Survival, layered over ruins.”\n\n**v0.1:** The corridor description became one joined paragraph describing the architecture as shifting from civic remnants to survival, then compressed the chamber inventory into a list.\n\n**v0.2:** “After two turns, the corridor widened into a chamber hidden behind the false wall of the buried street. The architecture changed immediately: not civic fiction anymore, but survival layered over ruins. The chamber held…” The remaining list retains the v0.1 detail.\n\nThe revision reconnects movement and architecture while restoring the requested distinction and adding no setting detail.\n\n### Chapter 1 — interruption in recovery\n\n**v0.2:** “Darkness. Silence. / Awareness. Extreme darkness. Brief, faint flashes in the distance. / Should I go to it? / Snap. Extreme pain.” The uncertain perception and question break before the existing dislocated-second sentence; “Then again” adds the second interruption before the translation-device hiss.\n\n### Chapter 21 — clue, then inference\n\n**Baseline and v0.1 order:** the runner reports the deepened cut; Cassian sees the bright thread; the group discusses who should notice it; later Cassian states that the hunter left the mark usable “on purpose.” v0.1 preserved that order but compressed the bright-thread observation and added “a deliberate bid for attention.” v0.2 restores the observed detail and short beats while keeping the dialogue at its existing position.\n\n## Rhythm and development model\n\nSentence contours, approximate length distributions, and paragraph changes are recorded per chapter in `measurements_v0.2.json`. The broad v0.1 pattern is retained in chapters where connected attention was already working; short action, silence, dialogue, and signal beats remain where they carry scene function. v0.2 develops the Chapter 1 recovery interruption, restores the Chapter 20 distinction, and restores the Chapter 21 clue presentation. Chapter 16 remains byte-identical and serves as a profile of connected attention, not a target statistic.\n\nThe scene-mode labels are sustained observation, immediate action, contested exchange, recollection/recovery, and signal/countdown. They describe changing demands, not prescribed rhythms.\n\n## Editorial dimensions\n\n- **Word choice:** selective precision; no decorative synonym replacement. Chapter 20 restores a phrase with an established contrast.\n- **Sentence structure and cadence:** connected syntax for linked movement and perception; short beats retained for actual turns, interruptions, and danger.\n- **Paragraph development:** group only details belonging to a shared moment or spatial field; do not turn every detail into a continuous inventory.\n- **Operation:** Chapter 1 additive interruption; Chapter 20 recast; Chapter 21 clue-presentation restoration; all other passages reviewed and retained. Narration, dialogue, and interface forms remain distinct.\n\n## Limitations\n\nAutomatic alignment cannot infer viewpoint, scene mode, subtext, or editorial intent. Counts can mis-segment punctuation and fragments. Human review is recorded in the chapter ledger; no metric is a quality score.\n\n## Frozen v0.2 principle\n\n**Let related perceptions develop through sentences rather than compressing them into inventories.**\n\nNext action: the author reads v0.2 beside v0.1 and judges whether the prose has gained the desired development.\n'''
    agg=[]
    for key,label in [('words','Word tokens'),('paragraphs','Paragraphs'),('sentences_approx','Approx. sentences'),('sentences_le_6_words','Sentences at most 6 tokens')]:
        vals=[sum(row[ver][key] for row in rows) for ver in ('baseline','v0_1','v0_2')]
        agg.append(f'| {label} | {vals[0]} | {vals[1]} | {vals[2]} |')
    report=report.replace('## What changed between baseline and v0.1', '## Aggregate structural counts\n\n| Measure | Baseline | v0.1 | v0.2 |\n|---|---:|---:|---:|\n'+'\n'.join(agg)+'\n\n## What changed between baseline and v0.1')
    write(ROOT/'analysis_v0.2.md',report)
    print('PASS: 28 chapters; source hashes, parent order, guide hash, Chapter 16 control verified before outputs.')

if __name__=='__main__': main()
