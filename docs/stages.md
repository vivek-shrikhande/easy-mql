# Stages


## ADD FIELDS

Adds new fields to documents. Similar to [PROJECT](#project), ADD FIELDS reshapes each document in the stream; specifically, by adding new fields to output documents that contain both the existing fields from the input documents and the newly added fields.
[SET](#set) is an alias for ADD FIELDS.

Link to MongoDB [$addFields](https://docs.mongodb.com/manual/reference/operator/aggregation/addFields).


### Syntax

```EASY-MQL
ADD FIELDS expression1 AS field_name1, ..., expressionN AS field_nameN;
```

### Example

```EASY-MQL
ADD FIELDS SUM(homework) AS totalHomework, SUM(quiz) AS totalQuiz;
```
----

## BUCKET BY

Categorizes incoming documents into groups, called buckets, based on a specified expression and bucket boundaries.

Link to MongoDB [$bucket](https://docs.mongodb.com/manual/reference/operator/aggregation/bucket).


### Syntax

```EASY-MQL
BUCKET BY expression BOUNDARIES array [ DEFAULT string ] [ PROJECT accumulator_expression AS field_name ] ;

where,
accumulator_expression = ADD_TO_SET(expression)
                         | AVG(expression)
                         | FIRST(expression)
                         | LAST(expression)
                         | MAX(expression)
                         | MERGE_OBJECTS(expression)
                         | MIN(expression)
                         | PUSH(expression)
                         | STD_DEV_POP(expression)
                         | STD_DEV_SAMP(expression)
                         | SUM(expression)
```

### Example

```EASY-MQL
BUCKET BY year_born
BOUNDARIES [1840 + 5, 1850, 1860, 1870, 1880]
DEFAULT "Other"
PROJECT SUM(1) AS count,
        PUSH({
            "name": CONCAT(first_name, " ", last_name),
            "year_born": year_born
        }) AS artists;
```
----

## COUNT AS

Returns a count of the number of documents at this stage of the aggregation pipeline.

Link to MongoDB [$count](https://docs.mongodb.com/manual/reference/operator/aggregation/count).


### Syntax

```EASY-MQL
COUNT AS field_name;
```

### Example

```EASY-MQL
COUNT AS 'doc count';
COUNT AS doc_count;
```
----

## FACET

Processes multiple aggregation pipelines within a single stage on the same set of input documents. Enables the creation of multi-faceted aggregations capable of characterizing data across multiple dimensions, or facets, in a single stage.

Link to MongoDB [$facet](https://docs.mongodb.com/manual/reference/operator/aggregation/facet).


### Syntax

```EASY-MQL
FACET ( pipline1 ) AS field_name1, ..., ( piplineN ) AS field_nameN;
```

### Example

```EASY-MQL
FACET
(
    UNWIND tags;
    SORT BY COUNT tags;
) AS categorizedByTags,
(
    MATCH price > 10;
    BUCKET BY price
    BOUNDARIES [10, 150, 200, 300, 400]
    DEFAULT "Other"
    PROJECT SUM(1) AS count,
            PUSH(title) AS titles;
) AS categorizedByPrice;
```
----

## GROUP BY

Groups input documents by a specified identifier expression and applies the accumulator expression(s), if specified, to each group. Consumes all input documents and outputs one document per each distinct group. The output documents only contain the identifier field and, if specified, accumulated fields.

Link to MongoDB [$group](https://docs.mongodb.com/manual/reference/operator/aggregation/group).


### Syntax

```EASY-MQL
GROUP BY expression PROJECT group_exp AS field_name1, ..., group_exp AS field_nameN;

group_exp = ADD_TO_SET(expression)
            | AVG(expression)
            | FIRST(expression)
            | LAST(expression)
            | MAX(expression)
            | MERGE_OBJECTS(expression)
            | MIN(expression)
            | PUSH(expression)
            | STD_DEV_POP(expression)
            | STD_DEV_SAMP(expression)
            | SUM(expression)
```

### Example

```EASY-MQL
GROUP BY item PROJECT SUM(1) AS count, SUM(price * quantity) AS totalSaleAmount;
```
----

## LIMIT

Passes the first n documents unmodified to the pipeline where n is the specified limit. For each input document, outputs either one document (for the first n documents) or zero documents (after the first n documents).

Link to MongoDB [$limit](https://docs.mongodb.com/manual/reference/operator/aggregation/limit).


### Syntax

```EASY-MQL
LIMIT positive_integer;
```

### Example

```EASY-MQL
LIMIT 5;
```
----

## LOOKUP

Performs a left outer join to another collection in the same database to filter in documents from the "joined" collection for processing.

Link to MongoDB [$lookup](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup).


### Syntax

```EASY-MQL
LOOKUP collection_name ON local_field = foreign_field AS field_name;
```

### Example

```EASY-MQL
LOOKUP inventory ON 'item' = 'sku' AS 'inventories';
```
----

## MATCH

Filters the document stream to allow only matching documents to pass unmodified into the next pipeline stage. MATCH uses standard MongoDB queries. For each input document, outputs either one document (a match) or zero documents (no match).

Link to MongoDB [$match](https://docs.mongodb.com/manual/reference/operator/aggregation/match).


### Syntax

```EASY-MQL
MATCH expression;
```

### Example

```EASY-MQL
MATCH score > 20 OR score < 90;
```
----

## MERGE INTO

Writes the resulting documents of the aggregation pipeline to a collection. The stage can incorporate (insert new documents, merge documents, replace documents, keep existing documents, fail the operation, process documents with a custom update pipeline) the results into an output collection. To use the MERGE stage, it must be the last stage in the pipeline.
New in version 4.2.

Link to MongoDB [$merge](https://docs.mongodb.com/manual/reference/operator/aggregation/merge).


### Syntax

```EASY-MQL
MERGE INTO [ [ DB db_name ] COLL collection_name ]
[ ON field1, field2, ..., fieldN ]
[ WHEN MATCHED THEN
    REPLACE
    | KEEP
    | MERGE
    | FAIL
    | ( pipeline ) ]
[ WHEN NOT MATCHED THEN
    INSERT
    | DISCARD
    | FAIL ];

where pipeline can only consist of the following stages:
    ADD FIELDS and its alias SET
    PROJECT and its alias UNSET
    REPLACE ROOT and its alias REPLACE WITH
```

### Example

```EASY-MQL
MERGE INTO DB voting COLL monthlytotals
ON _id, month
WHEN MATCHED THEN
    (
        ADD FIELDS thumbsup + '$new.thumbsup' AS thumbsup,
                   thumbsdown + '$new.thumbsdown' AS thumbsdown;
        SET thumbsup + '$new.thumbsup' AS thumbsup,
                   thumbsdown + '$new.thumbsdown' AS thumbsdown;
    )
WHEN NOT MATCHED THEN
    INSERT
;
```
----

## OUTPUT TO

Writes the resulting documents of the aggregation pipeline to a collection. To use the OUT stage, it must be the last stage in the pipeline.

Link to MongoDB [$out](https://docs.mongodb.com/manual/reference/operator/aggregation/out).


### Syntax

```EASY-MQL
OUTPUT TO [ [ DB db_name ] COLL collection_name ];
```

### Example

```EASY-MQL
OUTPUT TO DB reporting COLL author;
```
----

## PROJECT

Reshapes each document in the stream, such as by adding new fields or removing existing fields. For each input document, outputs one document.
See also [UNSET](#unset) for removing existing fields.

Link to MongoDB [$project](https://docs.mongodb.com/manual/reference/operator/aggregation/project).


### Syntax

```EASY-MQL
PROJECT element1, ..., <elementN;

where,
element = field
        | +field
        | -field
        | expression AS field_name
```

### Example

```EASY-MQL
PROJECT title, -publisher, +age, author.first AS first_name;
```
----

## REDACT

Reshapes each document in the stream by restricting the content for each document based on information stored in the documents themselves. Incorporates the functionality of [PROJECT](#project) and [MATCH](#match). Can be used to implement field level redaction. For each input document, outputs either one or zero documents.

Link to MongoDB [$redact](https://docs.mongodb.com/manual/reference/operator/aggregation/redact).


### Syntax

```EASY-MQL
REDACT expression;
```

### Example

```EASY-MQL
REDACT IF ( SIZE ( SET_INTERSECTION ( tags, [ "STLW", "G" ] ) ) > 0, "$$DESCEND", "$$PRUNE" );
```
----

## REPLACE ROOT

Replaces a document with the specified embedded document. The operation replaces all existing fields in the input document, including the _id field. Specify a document embedded in the input document to promote the embedded document to the top level.
[REPLACE WITH](#replace-with) is an alias for $replaceRoot stage.

Link to MongoDB [$replaceRoot](https://docs.mongodb.com/manual/reference/operator/aggregation/replaceRoot).


### Syntax

```EASY-MQL
REPLACE ROOT expression;
```

### Example

```EASY-MQL
REPLACE ROOT MERGE_OBJECTS({"_id": _id, "first":"", "last":""}, name);
```
----

## REPLACE WITH

Replaces a document with the specified embedded document. The operation replaces all existing fields in the input document, including the _id field. Specify a document embedded in the input document to promote the embedded document to the top level.
[REPLACE WITH](#replace-with) is an alias for REPLACE ROOT stage.

Link to MongoDB [$replaceWith](https://docs.mongodb.com/manual/reference/operator/aggregation/replaceWith).


### Syntax

```EASY-MQL
REPLACE WITH expression;
```

### Example

```EASY-MQL
REPLACE WITH MERGE_OBJECTS({"_id": _id, "first":"", "last":""}, name);
```
----

## SAMPLE

Randomly selects the specified number of documents from its input.

Link to MongoDB [$sample](https://docs.mongodb.com/manual/reference/operator/aggregation/sample).


### Syntax

```EASY-MQL
SAMPLE positive_integer;
```

### Example

```EASY-MQL
SAMPLE 3;
```
----

## SET

Adds new fields to documents. Similar to [PROJECT](#project), SET reshapes each document in the stream; specifically, by adding new fields to output documents that contain both the existing fields from the input documents and the newly added fields.
[SET](#set) is an alias for ADD FIELDS stage.

Link to MongoDB [$set](https://docs.mongodb.com/manual/reference/operator/aggregation/set).


### Syntax

```EASY-MQL
SET expression1 AS field_name1, ..., expressionN AS field_nameN;
```

### Example

```EASY-MQL
SET SUM(homework) AS totalHomework, SUM(quiz) AS totalQuiz;
```
----

## SKIP/OFFSET

Skips the first n documents where n is the specified skip number and passes the remaining documents unmodified to the pipeline. For each input document, outputs either zero documents (for the first n documents) or one document (if after the first n documents).

Link to MongoDB [$skip](https://docs.mongodb.com/manual/reference/operator/aggregation/skip).


### Syntax

```EASY-MQL
(SKIP | OFFSET) positive_integer;
```

### Example

```EASY-MQL
SKIP 5;
OFFSET 5;
```
----

## SORT/ORDER BY

Reorders the document stream by a specified sort key. Only the order changes; the documents remain unmodified. For each input document, outputs one document.

Link to MongoDB [$sort](https://docs.mongodb.com/manual/reference/operator/aggregation/sort).


### Syntax

```EASY-MQL
(SORT | ORDER) BY field1 sort_order, ..., fieldN sort_order;
where sort_order = DESC | ASC
```

### Example

```EASY-MQL
SORT BY age DESC, posts ASC;
```
----

## SORT BY COUNT

Groups incoming documents based on the value of a specified expression, then computes the count of documents in each distinct group.

Link to MongoDB [$sortByCount](https://docs.mongodb.com/manual/reference/operator/aggregation/sortByCount).


### Syntax

```EASY-MQL
SORT BY COUNT expression;
```

### Example

```EASY-MQL
SORT BY COUNT tags;
```
----

## UNION WITH

Performs a union of two collections; i.e. combines pipeline results from two collections into a single result set.
New in version 4.4.

Link to MongoDB [$unionWith](https://docs.mongodb.com/manual/reference/operator/aggregation/unionWith).


### Syntax

```EASY-MQL
UNION WITH collection_name [ WITH PIPELINE (
    stage1;
    stage2;
    ...
) ];
```

### Example

```EASY-MQL
UNION WITH warehouses WITH PIPELINE ( PROJECT +state, -_id; );
```
----

## UNSET

Removes/excludes fields from documents.
UNSET is an alias for [PROJECT](#project) stage that removes fields.

Link to MongoDB [$unset](https://docs.mongodb.com/manual/reference/operator/aggregation/unset).


### Syntax

```EASY-MQL
UNSET field1, field2, ..., fieldN;
```

### Example

```EASY-MQL
UNSET author, name;
```
----

## UNWIND

Deconstructs an array field from the input documents to output a document for each element. Each output document replaces the array with an element value. For each input document, outputs n documents where n is the number of array elements and can be zero for an empty array.

Link to MongoDB [$unwind](https://docs.mongodb.com/manual/reference/operator/aggregation/unwind).


### Syntax

```EASY-MQL
UNWIND field_path ARRAY INDEX AS field_name PRESERVE NULL EMPTY ARRAYS (true | false);
```

### Example

```EASY-MQL
UNWIND sizes ARRAY INDEX AS arrayIndex PRESERVE NULL EMPTY ARRAYS true;
```
----