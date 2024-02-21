# iBotsDashBoard

Dashboard built for data game analysis based on [loganalyzer](https://github.com/opusymcomp/loganalyzer3), a log analysis tool.

Others functions:
- work with rcssserver CSVSaver fuctions (TODO);
- work with our (iBots) internal data extractor, based on json files (TODO).


## Run locally:

Clone the proeject:
```console
git clone https://github.com/ibotsuft/iBotsDashboard.git
```

Enter the project's directory:
```console
cd iBotsDashboard
```

Create a virtual enviroment:
```console
python -m venv venv/
```

Activate the virtual enviroment:
```console
.\venv\Scripts\Activate.ps1
```

Install dependencies:
```console
pip install -r requirements.txt
```

Start the server:
```console
streamlit run Home.py
```