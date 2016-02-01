from django.shortcuts import render
import requests
import json

def index(request):
    data={}
    if request.method=='POST':
        user_repo1 = request.POST.get('user_repo1')
        user_repo2 = request.POST.get('user_repo2')
        req1 = requests.get('https://api.github.com/repos/'+ user_repo1)
        req2 = requests.get('https://api.github.com/repos/'+ user_repo2)
        r1 = json.loads(req1.content)
        r2 = json.loads(req2.content)

        data['username1'] = r1['owner']['login']
        data['repo1'] = r1['name']
        data['avatar1'] = r1['owner']['avatar_url']
        data['star_count1'] = r1['stargazers_count']
        # this is not the source fork count
        data['forks1'] = r1['forks_count']
        data['watch_count1'] = r1['subscribers_count']
        data['total1'] = r1['stargazers_count']+r1['forks_count']+r1['subscribers_count']

        data['username2'] = r2['owner']['login']
        data['repo2'] = r2['name']
        data['avatar2'] = r2['owner']['avatar_url']
        data['star_count2'] = r2['stargazers_count']
        # this is not the source fork count
        data['forks2'] = r2['forks_count']
        data['watch_count2'] = r2['subscribers_count']
        data['total2'] = r2['stargazers_count']+r2['forks_count']+r2['subscribers_count']

    return render(request, 'app/index.html',{'data':data})
