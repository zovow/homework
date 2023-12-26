import requests
import json

# 在这里填入你的 GitHub 用户名和令牌
username = 'zovow'
token = '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'

# 设置 GitHub API 的基本 URL
base_url = 'https://api.github.com'

# 获取关注者列表
followers_url = f'{base_url}/users/{username}/followers'
followers_response = requests.get(followers_url, auth=(username, token))
followers = followers_response.json()

# 遍历每个关注者，获取其仓库信息
for follower in followers:
    follower_repos_url = f'{base_url}/users/{follower["login"]}/repos'
    repos_response = requests.get(follower_repos_url, auth=(username, token))
    repos = repos_response.json()

    # 将仓库信息存储到本地文件
    with open(f'{follower["login"]}_repos.json', 'w') as f:
        json.dump(repos, f, indent=2)

print("数据已存储到本地文件中。")
