> ```MQL
> [
>     {
>         '$group': {
>             '_id': '$item',
>             'totalSaleAmount': {'$sum': {'$multiply': ['$price', '$quantity']}},
>         }
>     },
>     {'$match': {'$expr': {'$gte': ['$totalSaleAmount', 100]}}},
> ]
> ```
> 
> ```EasyMQL
> GROUP BY item
>     PROJECT SUM ( price * quantity ) AS totalSaleAmount;
> MATCH totalSaleAmount >= 100;
> ```



