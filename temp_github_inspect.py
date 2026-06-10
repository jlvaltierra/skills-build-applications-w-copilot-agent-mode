import json, urllib.request
url = 'https://api.github.com/repos/jlvaltierra/skills-build-applications-w-copilot-agent-mode/actions/runs/27249278440/jobs'
req = urllib.request.Request(url, headers={'User-Agent':'GitHub-API-Client'})
with urllib.request.urlopen(req) as r:
    data = json.load(r)
job = next(j for j in data['jobs'] if j['name'] == 'Check step work')
print(json.dumps({'id': job['id'],'name': job['name'],'status': job['status'],'conclusion': job['conclusion'],'steps': [{'name': s['name'], 'number': s.get('number'), 'status': s['status'], 'conclusion': s.get('conclusion'), 'outcome': s.get('outcome')} for s in job['steps']]}, indent=2))
