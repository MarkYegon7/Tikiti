from website import create_app,create_database,db
#from website.models import add_user

if __name__ == '__main__':

    app = create_app()
    create_database(app)
    # add_user(email='email',username='username',password='password')
    app.run(debug=True)