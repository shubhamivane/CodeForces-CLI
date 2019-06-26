import click
import getpass
from . import db
from .api.contest import upcoming_contest
from .api.contest import contest_history
from .api.user import user_profile
from .crawler.login import verify_credentials

@click.group()
def cli():
    """ CLI tool for Codeforces """
    click.echo('\t\t  ___   ____    ___   _      _____')
    click.echo('\t\t / __| |  __|  / __| | |    |_   _|')
    click.echo('\t\t| |    | |__  | |    | |      | |')
    click.echo('\t\t| |__  |  __| | |__  | |__   _| |_')
    click.echo('\t\t \___| |_|     \___| |____| |_____| ')
    click.echo('\n')

@cli.command()
def user():
    """ Prints the user information """
    flag, username = db.logged_in()
    if flag:
        user, error = user_profile(username)
        if not user is None:
            click.echo('-----------------------------------------------------------')
            click.echo('                      User Profile')
            click.echo('-----------------------------------------------------------')
            click.echo('\t Name                 : {0}'.format(user['name']))
            click.echo('\t Handle               : {0}'.format(user['handle']))
            click.echo('\t Max. Rating and Rank : {0}({1})'.format(user['maxRating'], user['maxRank']))
            click.echo('\t Rating and Rank      : {0}({1})'.format(user['rating'], user['rank']))
            click.echo('\t Country              : {0}'.format(user['country']))
            click.echo('\t Friends              : {0}'.format(user['friendOfCount']))
            click.echo('------------------------------------------------------------')
        else:
            click.echo(error)
    else:
        click.echo('\t\t Please login first')
        

@cli.command()
def login():
    """ Login to codeforces """
    flag, username = db.logged_in()
    if flag == False:
        print('Handle  : ', end='')
        username = input() 
        password = getpass.getpass()
        flag, error = db.login(username, password)
        if flag and len(error) == 0:
            click.echo('\t\t You are successfully logged in as {0}'.format(username))
        elif flag:
            print(flag)
            click.echo('\t\t Different credentials from database')
            click.echo('\t\t Verifying credentials on Codeforces')
            flag, error = verify_credentials(username, password)
            if flag:
                flag, error = db.update(username, password)
                if flag:
                    flag, error = db.login(username, password)
                    if flag:
                        click.echo('\t\t You are successfully logged in as {0}'.format(username))
                    else:
                        click.echo(error)
                else:
                    click.echo(error)
            else:
                click.echo('\t\t Couldn\'t verify credentials on Codeforces')
                click.echo(error)
        else:
            flag, error = verify_credentials(username, password)
            if flag:
                db.write(username, password)
                click.echo('\t\t You are successfully logged in as {0}'.format(username))
            else:
                click.echo(error)
    else:
        click.echo('\t\t You are logged in as {0}'.format(username))

@cli.command()
def logout():
    """ Logout from Codeforces """
    flag, error = db.logout()
    if flag:
        click.echo(error)
    else:
        click.echo(error)
