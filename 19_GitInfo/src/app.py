from github import Github
from flask import Flask, render_template, request

# Local Import
import config

app = Flask(__name__)
app.logger.setLevel = 10
app.config.from_object('config.DevelopmentConfig')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch')
def fetch():
    flag = 1
    username = request.args.get('uname')
    g = Github()
    try:
        user = g.get_user(username)
    except Exception as err:
        app.log_exception(err)
    repos = list()
    for repo in user.get_repos():
        repos.append(repo.full_name.split('/')[1])
    app.logger.debug(f"Found Repo Names - {repos}")
    return render_template('index.html', repos=repos, flag=flag)


if __name__ == '__main__':
    app.run()
