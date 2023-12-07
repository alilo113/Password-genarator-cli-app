import click
import random

@click.command()
@click.option("--np", "--new_password", default=12, help="Length of the new password")
def generate_password(np):
    characters = ["a", "b", "c", "d", "e", "F", "G", "H", "I", "J", "@", "#", "!", "1", "2", "3", "4", "5"]
    password_length = int(np) if np else click.prompt('The password length')

    generate_password = ''.join(random.choice(characters) for _ in range(password_length))
    click.echo(f'Your password is: {generate_password}')

if __name__ == '__main__':
    generate_password()