OAuth

Person -> localhost:8000/google/login

Your app redirects -> google -> person logs in to google (not your app)

Google -> verifies user, verifies your app -> localhost:8000/google/callback

Your app -> verifies google callback stuff -> starts user's Django session
