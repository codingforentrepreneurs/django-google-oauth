# Google Login on Django from Scratch

This is a sample Django app that allows you to login with Google using OAuth2.

## Usage


Create an example Django project

```bash
mkdir -p path/to/my/project

# mac/linux
python3.12 -m venv venv
source venv/bin/activate

# windows
c:\Python312\python.exe -m venv venv
.\venv\Scripts\activate


pip install django

mkdir -p src
cd src # should now be workin in path/to/my/project/src
django-admin startproject cfehome .
```

After that, we need to clone this repo and copy the `googler` app to our project.


```bash
cd ~/desktop
git clone https://github.com/codingforentrepreneurs/django-google-oauth
cd django-google-oauth
cp -r googler/ path/to/my/project/src/googler/
```


Add the following to your `cfehome/settings.py`

```python
GOOGLE_CLIENT_ID= os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_SECRET_KEY= os.environ.get('GOOGLE_SECRET_KEY')

INSTALLED_APPS = [
    'googler',
]
```

in `cfehome/urls.py`

```python
path('google/', include('googler.urls')),
```

To get `GOOGLE_CLIENT_ID` and `GOOGLE_SECRET_KEY`, you need to:

- Create a project in the Google Cloud Console (one for Development and one for Production)
- Navigate to "Google Auth Platform"
- Create Client ID and Client Secret for the project
- Add the callback url to `http://localhost:8000/google/callback/` (matches the url configuration in the `googler` app)


