# from flask.cli import FlaskGroup
# from flask_migrate import Migrate,MigrateCommand
# from website import create_app, db

# app = create_app()
# cli = FlaskGroup(create_app=create_app)


# migrate = Migrate(app, db)
# cli.add_command('db', MigrateCommand)

# if __name__ == '__main__':
#     cli()

# Tikiti/manage.py

from flask.cli import FlaskGroup
from flask_migrate import Migrate, upgrade
from website import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)

# Attach Flask-Migrate commands to Flask CLI
migrate = Migrate(app, db)

if __name__ == '__main__':
    cli()

