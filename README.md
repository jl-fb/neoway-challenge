# Neoway Challenge

This is a webcrawler with de proporse to get CEP (Código de Endereçamento Postal) from de _Correios_ API.
<br>
<br>

# Run

To run this project you'll need to have [docker](https://docs.docker.com/get-docker/) installed.

First build the project:

```bash
$ docker build -t [--my-app-name] .
```

- _[--my-app-name]_ in case will be **_neoway-challenge_**

Then run the <a href="#obs">image</a>:<br>

```bash
$ docker run -it --name neoway-challenge neoway-challenge
```

<p id="obs"><strong>Obs</strong>: If you get some error like: "pull access denied repository does not exist or may require docker login". Try to run the command:</p>

```bash
$ docker run -it --name neoway-challenge python
```

Then you can repeat the `$ docker run -it --name my-app-name my-app-name` command.
<br>
<br>

# Usage

Once you have success in build and run the container. Run this command:

```
docker exec -it neoway-challenge /bin/sh
```

you'll see something like that

```bash
/src #
```

Then just type

```bash
python main.py
```

That's will run the application and make the post requests to the _Correios API_ and then, create's a file for each UF containing the information **id**, **localidade**, **faixaCep**, **situação**, **tipoFaixa**.

To read the information, you can just type

```bash
cat [UF]_result.jsonl
```

**Ex:** AL.result.jsonl

There are some of this files in the repo already. Just as samples.

# Disclaimer

Since it's the first time I make a project in _python_ and for some others reasons(time, mostly), I don't develop any test files. I'm apologize for that!
Also, I don't really made the application save all the UFs data. For exemple: If we have an error retriving AL's data, the application will catch this exeption but continues fetching from others UFs
