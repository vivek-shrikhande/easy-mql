# EasyMQL

> *A text based query language for MongoDB.*

EasyMQL is an **Easy**-to-use **M**ongoDB **Q**uery **L**anguage.
It is text based which means you don't have to use `{` and `}` at all
the places like you do in bson based queries (the official **MQL**).
EasyMQL also eases the use of operators. You use only `+` instead of `$add`,
`-` instead of `$subtract` and so on. Also, few constructs are similar
those in SQL so that if you're familiar with SQL you don't have to learn
another syntax for the same purpose; for example, `CASE`, `EXTRACT`, `IF`,
`IF_NULL`, operators, etc. In some ways it looks like SQL but not exactly.

Here are a couple of examples of MQL, and their corresponding EasyMQL queries,

> ```MQL
> {
>     '$match': {
>         '$expr': {
>             '$gt': ['$price', {'$add': [1000, {'$divide': [18, 100]}]}]
>         }
>     }
> }
> ```
> 
> ```EasyMQL
> MATCH price > 1000 + 18 / 100;     # base price = 1000 and tax = 18%
> ```

> ```MQL
> {
>     '$project': {
>         'title': 1,
>         'author.first': 1,
>         'author.last': 1,
>         'author.middle': {
>             '$cond': {
>                 'if': {'$eq': ['$author.middle', '']},
>                 'then': '$$REMOVE',
>                 'else': '$author.middle',
>             }
>         },
>     }
> }
> ```
> 
> ```EasyMQL
> PROJECT +title,
>         +author.first,
>         +author.last,
>         IF (author.middle = "",
>             $REMOVE,
>             author.middle) AS author.middle;
> ```

See [examples](examples.md) section for more.

EasyMQL has also got a nice little Query Composer for you to write queries.
See Getting Started section for more

> [!NOTE|label:Licensing Notice]
> - Part of this documentation (short descriptions and examples of [operators](operator.md) and [stages](stages.md))
>   is a derivative of [aggregation-pipeline-operators](https://docs.mongodb.com/manual/reference/operator/aggregation/)
>   and [aggregation-pipeline-stages](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/) by
>   [MongoDB](https://docs.mongodb.com/), used under [CC BY](https://creativecommons.org/licenses/by-nc-sa/3.0/).
> 
> - This documentation is licensed under [CC BY](https://creativecommons.org/licenses/by-nc-sa/3.0/).