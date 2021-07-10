import requests
import json
username = 'Os1991'
token = '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'
r = requests.get('https://api.github.com/user/repos', auth=(username, token))
#r = r.json()
#print('reposJSON: \n', r)

for repo in r.json():
    if not repo['private']:
        print(repo['html_url'])

r = r.json()
with open('C:\\Users\\s.okruzhnov\\PycharmProjects\\pythonProject\\githubAPI.json', 'w') as f:
    json.dump(r, f, ensure_ascii=False)