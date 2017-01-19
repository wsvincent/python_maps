from fabric.api import local, task, cd, run


@task
def deploy():
    local('git push origin master')
