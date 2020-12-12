# HVAC Design

**Effective Tool for HVAC Design Engineers**

This is an application which supports HVAC (_Heating, Ventilation, Air-Conditioning_) Design Engineers with every-day calculations. The current goal is to allow the following types of calculations:

- Pipe sizing,
- Valve sizing,
- Pipe pressure drop calculation.

More will be added in the future.

## Built with

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [jQuery](https://jquery.com/)

## Installation

```
$ git clone https://github.com/sid2021/hvac-design.git
$ cd hvac-design
```

If you want to use virtualenv (on Windows):

```
$ python -m venv venv
$ venv\scripts\activate
```

If you want to use virtualenv (on MacOS/Linux):

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Install dependencies, set FLASK-APP environment variable and run app (on Windows):

On Windows (powershell):

```
$ pip install -r requirements.txt
$ $env:FLASK_APP="hvacdesign.py"
$ flask run
```

On MacOS/Linux:

```
$ pip install -r requirements.txt
$ export FLASK_APP=hvacdesign.py
$ flask run
```
