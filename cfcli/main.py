import click
import getpass
import db

from crawler import login
from api import contest
from api import user

@click.group()
def cli():
    """ CLI tool for Codeforces """

@cli.command()
@click.option
def user():
    """ Prints the user information """
    flag, username = db.logged_in()
    if flag:
        

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
        else if flag:
            click.echo('Different credentials from database')
            click.echo('Verifying credentials on Codeforces')
            flag, error = login.verify_credentials(username, password)
            if flag:
                flag, error = db.update(username, password)
                if flag:
                    flag, error = db.login(username, password)
                    if flag:
                        click.echo('You are successfully logged in as {0}'.format(username)')
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
    
@cli.command()
def logout():
    flag, error = db.logout()
    click.echo('{}'.format(error))