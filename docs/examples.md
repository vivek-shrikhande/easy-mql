# Examples

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

> ```MQL
> [
>    { $match: { _id: 1 } },
>    { $addFields: { homework: { $concatArrays: [ "$homework", [ 7 ] ] } } }
> ]
> ```
>
> ```EasyMQL
> MATCH _id = 1;
> ADD FIELDS
>     ARRAY_CONCAT(homework, [7]) AS homework;
> ```

> ```MQL
> [
>   {
>     $match: {
>       score: {
>         $gt: 80
>       }
>     }
>   },
>   {
>     $count: "passing_scores"
>   }
> ]
> ```
>
> ```EasyMQL
> MATCH score > 80;
> COUNT AS passing_scores;
> ```

> ```MQL
> [ { $project : { "author.first" : 0, "lastModified" : 0 } } ]
> ```
>
> ```EasyMQL
> PROJECT -author.first, -lastModified;
> ```

> ```MQL
> [
>     {
>         $replaceRoot: {
>             newRoot: {
>                 $mergeObjects: [
>                     { dogs: 0, cats: 0, birds: 0, fish: 0 },
>                     "$pets"
>                 ]
>             }
>         }
>     }
> ]
> ```
>
> ```EasyMQL
> REPLACE ROOT
>     MERGE_OBJECTS({ "dogs": 0, "cats": 0, "birds": 0, "fish": 0 }, pets)
> ```
