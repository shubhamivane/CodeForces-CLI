import click
import getpass

from . import db
from .crawler import login
from api import contest
from api import user

@click.group()
def cli():
    """ CLI tool for Codeforces """
    contest_list, error = contest.upcoming_contest()
    if contest_list is None:
        click.echo(error)
    else:
        for contest in contest_list:
            click.echo('{0}\t\t\t{1}'.format(contest[0], contest[1]))


@cli.command()
def user():
    """ Prints the user information """
    flag, username = db.logged_in()
    if flag:
        user = user.user_profile(username)
        click.echo('-----------------------------------------------------------')
        click.echo('                      User Profile')
        click.echo('-----------------------------------------------------------')
        click.echo('\t Name                 : {0}'.format(user['name']))
        click.echo('\t Handle               : {0}'.format(user['handle']))
        click.echo('\t Max. Rating and Rank : {0}({1})'.format(user['maxRating']), user['maxRank'])
        click.echo('\t Rating and Rank      : {0}({1})'.format(user['rating'], user['rank']))
        click.echo('\t Country              : {0}'.format(user['country']))
        click.echo('\t Friends              : {0}'.format(user['friendOfCount']))
    else:
        click.echo('Please login first')
        

@cli.command()
def login():
    """ Login to codeforces """
    flag, username = db.logged_in()
    if flag == False:
        print('Handle   : ', end='')
        username = input() 
        password = getpass.getpass()
        flag, error = db.login(username, password)
        if flag and len(error) == 0:
            click.echo('You are successfully logged in as {0}'.format(username))
        elif flag:
            click.echo('Different credentials from database')
            click.echo('Verifying credentials on Codeforces')
            flag, error = login.verify_credentials(username, password)
            if flag:
                flag, error = db.update(username, password)
                if flag:
                    flag, error = db.login(username, password)
                    if flag:
                        click.echo('You are successfully logged in as {0}'.format(username))
                    else:
                        click.echo(error)
                else:
                    click.echo(error)
            else:
                click.echo('Couldn\'t verify credentials on Codeforces')
                click.echo(error)
        else:
            click.echo(error)
    else:
        click.echo('You are logged in as {0}'.format(username))

@cli.command
def logout():
    flag, error = db.logout()
    click.echo('{}'.format(error))
