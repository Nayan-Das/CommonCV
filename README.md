# Common CV

## Code

I have used python 3, Flask, SQLite,simple JSON for this project.
To run the project go to the project folder and run -
```sh
python app.py
```
All the data are returned in JSON format.

## Task
#### 1- First step is to ingest this file in a sqlite database.

The ingested SQLite DB file is gsoc.db 
#### 2- Write an endpoint to return these posts, by default it should be in chronological order. By way of a query string in the URL, these posts may also be ordered by view count or score.

The REST API to call this functionality is-
```sh
http://127.0.0.1:5000/getData?orderBY=<score/count>

```
![Alt text](./orderBy.png?raw=true "Optional Title")

#### 3- Write an endpoint to search these posts. Again, by way of a query string, filter the posts based on the presence of the search term, either in the title or body of the post.

The REST API to call this functionality is-
```sh
http://127.0.0.1:5000/searchData?searchBy=<search striing>

```
![Alt text](./searchBy.png?raw=true "Optional Title")
