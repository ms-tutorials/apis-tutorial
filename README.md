# Intro To APIs

### Set up project

- Create a `.secrets` folder and add a `creds.json` file in the folder
- Add your TMDB api key in the `creds.json` file, i.e: 

```bash
echo '{ "key": "API KEY"}' >> creds.json #Replace API KEY with actual key
```

- Create a virtual environment `python -m venv venv`

- Activate the virtual environment:
   `source venv/bin/activate` #Linux
    `source venv/Scripts/activate` #Windows

- install dependencies `pip install -r requirements.txt`

### Run Project

- Run the `run.py` file