from app import create_app

# Import create_app in run.py in order to be
# able to run app.

app = create_app()


if __name__ == '__main__':
    app.run()
