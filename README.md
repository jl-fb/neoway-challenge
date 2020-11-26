# Neoway Challenge

This is a webcrawler with de proporse to get CEP (Código de Endereçamento Postal) from de _Correios_ API.
<br>
<br>

# Run

To run this project you'll need to have [docker](https://docs.docker.com/get-docker/) installed.

First build the project:

```bash
$ docker build -t --my-app-name .
```

Then run the <a href="#obs">image</a>:<br>

```bash
$ docker run -it --name my-app-name my-app-name /bin/sh
```

<p id="obs"><strong>Obs</strong>: If you get some error like: "pull access denied repository does not exist or may require docker login". Try to run the command:</p>

```bash
$ docker run -it --name my-app-name python
```

Then ypu can repeat the `$ docker run -it --name my-app-name my-app-name /bin/sh ` command.
<br>
<br>

# Usage

Once you have success in build and run the container you'll see something like that

```bash
/src #
```

Then just type

```bash
python main.py
```

thats create a file `result.txt`. Just open the file ou type

```bash
cat result.txt
```
