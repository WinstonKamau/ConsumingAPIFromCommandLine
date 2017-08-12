'''A module that returns a string describing the longitudinal and latitudinal
position of a satellite'''
import click
import requests


@click.command()
def cli():
    '''A method that returns the current latitudinal and longitudinal position
    of the space satellite'''
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    click.echo("The satellite is now at longitude %s and latitude %s"
               %(data["iss_position"]["longitude"], data["iss_position"]["latitude"]))
