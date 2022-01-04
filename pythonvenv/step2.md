# dependancy checking

`pip install pip-tools`{{execute}}

`pip install pip`{{execute}}

`pip install pipdeptree`{{execute}}

`pipdeptree -h`{{execute}}

`pip-compile -h`{{execute}}

# downloading and installing

setup new folder and requirements.txt

`cd ~`{{execute}}

`mkdir dwn; cd dwn`{{execute}}

```
numpy>=1.8.2,<2.0.0
matplotlib>=1.3.1,<2.0.0
scipy>=0.14.0,<1.0.0
astroML>=0.2,<1.0
scikit-learn>=0.14.1,<1.0.0
rpy2>=2.4.3,<3.0.0
```

`pip install --download=/tmp -r requirements.txt`{{execute}}

`pip install --user --no-index --find-links=/tmp -r requirements.txt`{{execute}}


pulled from: https://stackoverflow.com/questions/32302379/could-not-find-a-version-that-satisfies-the-requirement-package