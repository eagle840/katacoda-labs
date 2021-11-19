apt install nano

 

root@babbbc922312:/temp1911# cat main.py



```
def main():

        print("hello")

 

if __name__ == "__main__":

        main()
```

instead, copy this:   
https://click.palletsprojects.com/en/8.0.x/commands/#custom-multi-commands


   34  which python3

   35  ln -s /usr/bin/python3 /usr/bin/python

install:


https://click.palletsprojects.com/en/8.0.x/commands/#custom-multi-commands


   36  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

 

poetry -h

 

python3 -m main

 

poetry new click

 

cd to ./click/click

 

poetry add click