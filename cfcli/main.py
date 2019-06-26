import click
import getpass
import db

@click.group()
def cli():
    """ CLI tool for Codeforces """

@cli.command()
@click.option
def user():
    """ Prints the user information """
    

@cli.command()
def login():
    """ Login to codeforces """
    try:
        flag, username = db.logged_in()
        if flag == False:
            print('Handle   : ', end='')
            username = input() 
            password = getpass.getpass()
            flag, message = db.login(username, password)
            if flag and len(message) == 0:
                click.echo('You are successfully logged in as {0}'.format(username))
            else if flag:
                
    except Exception as error:
        click.echo('{0}'.format(error))

@cli.command()
def logout():
    flag, error = db.logout()
    click.echo('{}'.format(error))