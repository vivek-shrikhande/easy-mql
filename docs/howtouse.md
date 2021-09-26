# How to use

EasyMQL doesn't directly work with mongoDB like the official
mongoDB query language (MQL) does. Instead, it just converts your EasyMQL
query to MQL query. You can use it in the following 2 different ways.

## 1. Query Composer
You can use the query composer to write queries and get the corresponding MQL which you can then use in your code.

### Installation

#### Docker

1. Pull the docker image

    ```sh
    docker pull easy-mql-composer
    ```

2. Run the container

    ```sh
    docker run -p 5000:5000 easy-mql-composer
    ```

Set `HOST` and `PORT` environment variables to override default host `0.0.0.0` and port `5000` values respectively.

#### Standalone

1. Clone the repository or simply download

    ```sh
    # Clone
    git clone https://github.com/PrashantSakre/easy-mql-webtool.git

    # -- OR --
    # Download zip file from github and unzip it using the following command
    unzip <zip file path>
    ```

2. Install and run entry file

    ```sh
    cd easy-mql-webtool
    pip3 install -r requirements.txt
    python3 run.py
    ```

Set `HOST` and `PORT` environment variables to override default host `0.0.0.0` and port `5000` values respectively.

### Usage

Watch this **~80 seconds** video on how to use the composer.

[easymql](usagevideo.html ':include')

----

## 2. Programmatically using Python package
You can use the EasyMQL python package programmatically in your python application.


### Installation

```sh
pip install easy-mql
```

### Usage

```python
from easymql import EasyMQL

...

    # create EasyMQL object.
    emql = EasyMQL()

    # Parse the EasyMQL query and get corresponding MQL query
    try:
        mql_pipeline = emql.parse('MATCH language = "English";')

    except EasyMQLSyntaxError as e:
        # Handle the Syntax Error
        pass

    # Value in mql_pipeline variable in our case will be
    # [
    #     {
    #         "$match": {
    #             "$expr": {
    #                 "$eq": [ "$language", "English" ]
    #             }
    #         }
    #     }
    # ]


    # Use the pymongo client to query
    db.langs.aggregate(pipeline=mql_pipeline)

...
```
