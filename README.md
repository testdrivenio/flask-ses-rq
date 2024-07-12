# Sending confirmation Emails with Flask, Redis Queue, and Amazon SES

Send confirmation emails to newly registered users with Flask, Redis Queue, and Amazon SES

### Want to learn how to build this?

Check out the [article](https://testdriven.io/sending-confirmation-emails-with-flask-rq-and-ses).

## Want to use this project?

1. Fork/Clone

1. [Sign up](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sign-up-for-aws.html) for AWS (if necessary), [verify](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) an email for [SES](https://aws.amazon.com/ses/), and update the following environment variables for the `worker` service in _docker-compose.yml_:

   ```yaml
   - SES_REGION=us-east-2
   - SES_EMAIL_SOURCE=your_email
   - AWS_ACCESS_KEY_ID=your_access_key_id
   - AWS_SECRET_ACCESS_KEY=your_secret_access_key
   ```

1. Spin up the containers and update the database:

   ```sh
   $ docker compose up -d --build
   $ docker compose run users python manage.py create_db
   ```

1. Open your browser to http://localhost:5003 to view the app.
