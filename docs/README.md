# EasyMQL

> *An easy-to-use query language for MongoDB.*

EasyMQL is an **Easy**-to-use **M**ongoDB **Q**uery **L**anguage.
It solves the pain points in writing bson based mongoDB queries
(the official **MQL**). For instance, you don't have to use `{` and `}`
around all the constructs. In the case of operators, you use only `+`
instead of `$add`, `-` instead of `$subtract` and so on. No more confusion
between fields & field paths and when to prefix `$` & when not to.

Also, few constructs are similar to those in SQL so that if you're familiar
with SQL you don't have to learn another syntax for the same purpose; for
example, `CASE`, `EXTRACT`, `IF`, `IF_NULL`, operators, etc. In some ways
it looks like SQL but not exactly.

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

EasyMQL has also got a nice little-weight Query Composer for writing queries.
See [Query Composer](http://localhost:3000/#/howtouse?id=_1-query-composer) section for more.

See [reference](basics.md) section for language syntax/semantics.

> [!NOTE|label:Licensing Notice]
> - Part of this documentation (short descriptions and examples of [operators](operator.md) and [stages](stages.md))
>   is a derivative of [aggregation-pipeline-operators](https://docs.mongodb.com/manual/reference/operator/aggregation/)
>   and [aggregation-pipeline-stages](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/) by
>   [MongoDB](https://docs.mongodb.com/), used under [CC BY](https://creativecommons.org/licenses/by-nc-sa/3.0/).
>
> - This documentation is licensed under [CC BY](https://creativecommons.org/licenses/by-nc-sa/3.0/).
>
> - The EasyMQL package is licensed under [MIT](https://github.com/vivek-shrikhande/easy-mql/blob/main/LICENSE).