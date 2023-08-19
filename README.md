# Cat in Space Link Shortner
A link shortnered without a database. Written in Python and licensed under GPLv3.

## How does it work?
Everything is stored in a `links.txt` file in the following format:
```
slug+http://url
```

## How do I run it?
```sh
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install flask gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```
