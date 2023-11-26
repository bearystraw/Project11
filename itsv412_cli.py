import click
import requests

API_BASE_URL = "http://34.174.1.18"

@click.group()
def cli():
    """Command Line Interface for interacting with the API."""
    pass

@click.command()
@click.argument('string')
def md5(string):
    """Get MD5 hash of a string."""
    response = requests.get(f"{API_BASE_URL}/md5/{string}")
    click.echo(response.json())

@click.command()
@click.argument('n', type=int)
def factorial(n):
    """Calculate factorial of a number."""
    response = requests.get(f"{API_BASE_URL}/factorial/{n}")
    click.echo(response.json())

@click.command()
@click.argument('n', type=int)
def fibonacci(n):
    """Get Fibonacci sequence up to a number."""
    response = requests.get(f"{API_BASE_URL}/fibonacci/{n}")
    click.echo(response.json())

@click.command()
@click.argument('n', type=int)
def is_prime(n):
    """Check if a number is prime."""
    response = requests.get(f"{API_BASE_URL}/is-prime/{n}")
    click.echo(response.json())

@click.command()
@click.argument('message')
def slack_alert(message):
    """Send a message to Slack."""
    response = requests.get(f"{API_BASE_URL}/slack-alert/{message}")
    click.echo(response.json())

@click.command()
@click.argument('action', type=click.Choice(['create', 'read', 'update', 'delete']))
@click.option('--key', '-k', required=True)
@click.option('--value', '-v')
def keyval(action, key, value):
    """Perform a key-value operation."""
    url = f"{API_BASE_URL}/keyval/{key}" if action in ['read', 'delete'] else f"{API_BASE_URL}/keyval"
    method = {'create': 'post', 'read': 'get', 'update': 'put', 'delete': 'delete'}[action]
    json_data = {'storage-key': key, 'storage-val': value} if action in ['create', 'update'] else None

    response = requests.request(method, url, json=json_data)
    click.echo(response.json())

cli.add_command(md5)
cli.add_command(factorial)
cli.add_command(fibonacci)
cli.add_command(is_prime)
cli.add_command(slack_alert)
cli.add_command(keyval)

if __name__ == '__main__':
    cli()

