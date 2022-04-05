import os
from invoke import task

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def robot(ctx):
    os.environ["ENV"] = "test"
    ctx.run("robot src/tests", pty=True)
    del os.environ["ENV"]

@task(coverage_report, robot)
def tests(ctx):
    ctx.run("pylint src", pty=True)
