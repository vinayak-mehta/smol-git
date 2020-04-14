# -*- coding: utf-8 -*-

import os
import time
import random
import configparser

import click

from .utils import get_log, get_status, get_commit_message_marker


@click.group("smol-git")
@click.version_option("0.1.0")
def cli(*args, **kwargs):
    """git - the stupid content tracker"""
    pass


@cli.command()
@click.argument("src")
@click.argument("dest", required=False)
def clone(src, dest):
    """Clone a repository into a new directory."""
    if dest is None:
        dest = src.split("/")[-1]
    if not os.path.exists(dest):
        os.makedirs(dest)

    click.echo(f"Cloning into '{dest}'...")
    files = list(range(0, 5))

    # https://click.palletsprojects.com/en/7.x/utils/#showing-progress-bars
    with click.progressbar(files) as bar:
        for file in bar:
            time.sleep(random.random())


@cli.command()
@click.argument("key")
@click.argument("value")
def config(key, value):
    """Get and set repository or global options."""
    # https://click.palletsprojects.com/en/7.x/utils/#finding-application-folders
    app_dir = click.get_app_dir("smol_git")

    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
    cfg = os.path.join(app_dir, "config")

    config = configparser.ConfigParser()
    config.read(cfg)
    section, key = key.split(".")
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, key, value)

    with open(cfg, "w") as configfile:
        config.write(configfile)


@cli.command()
def log(*args, **kwargs):
    """Show commit logs."""
    # https://click.palletsprojects.com/en/7.x/utils/#pager-support
    dummy_log = get_log()
    click.echo_via_pager(dummy_log)


@cli.command()
def status(*args, **kwargs):
    """Show the working tree status."""
    # https://click.palletsprojects.com/en/7.x/utils/#ansi-colors
    dummy_status = get_status()
    click.echo(dummy_status + click.style("\tnew file:   a.txt", fg="green") + "\n")


@cli.command()
@click.option("-m", "--message", help="The commit message.")
def commit(*args, **kwargs):
    """Record changes to the repository."""
    # https://click.palletsprojects.com/en/7.x/utils/#launching-editors
    if kwargs["message"] is not None:
        commit_message = kwargs["message"]
    else:
        marker = get_commit_message_marker()
        commit_message = click.edit(marker)
        commit_message = commit_message.split(marker, 1)[0].rstrip("\n")

    if not commit_message:
        click.echo("Aborting commit due to empty commit message.")
    else:
        click.echo(f"[master 9d83964] {commit_message}")


@cli.command()
@click.argument("repository")
@click.argument("branch")
def push(repository, branch):
    """Update remote refs along with associated objects."""
    username = click.prompt("Username for 'https://github.com'")
    password = click.prompt(
        f"Password for 'https://{username}@github.com'", hide_input=True
    )

    click.echo(f"Pushing to '{repository}'...")
    files = list(range(0, 5))

    # https://click.palletsprojects.com/en/7.x/utils/#showing-progress-bars
    with click.progressbar(files) as bar:
        for file in bar:
            time.sleep(random.random())
