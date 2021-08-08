# Data Types

Data types are categorised into [Primary](#Primary) and [Composite](#Composite).

# Primary

## Boolean

Boolean consists of `true` or `false`

----

## Date

Dates are constructed using `D"<ISO8601 datetime>"` format. See below for detailed syntax.

### Syntax

```EasyMQL
D"YYYY[-MM[-DD]][(T| )HH:MM[:SS[.sss]][timezone]]"
where,
    timezone = (Z|offset)
    offset   = (+|-)HH[[:]MM]
```

### Examples

```EasyMQL
D"2021"
D"2021-01"
D"2021-01-01"
D"2021-01-01T12:14"
D"2021-01-01 12:14"
D"2021-01-01T12:14:00"
D"2021-01-01T12:14:00Z"
D"2021-01-01T12:14:00-05"
D"2021-01-01T12:14:00+05:30"
D"2021-01-01T12:14:00+0530"
D"2021-01-15T12:30:59.932-12:00"
```

----

## Number

Number consists of both integers and decimals. Scientific notation is also supported.

### Examples

```EasyMQL
123
+123
-123
123.4 
-.123 
+0.123
-123.1e1
123.1E1
```

----

## Null

Null values are represented by `null`.

----

## String

Strings are delimited only by `"`. They can span across multiple lines. Use `\` for escaping.

### Examples

```EasyMQL
"hello"
"hello \"world\""
"multi
line"
```

----

# Composite

## Array

Arrays are a sequence of expressions delimited by `[` and `]` and separated by `,`.

### Syntax

```EasyMQL
[<expression1>, <expression2>, ...]
```

### Examples

```EasyMQL
[]
[1,2,3, null, "hello", {"count": 1}]
```

----

## Object

Objects consist of a sequence of key-value pairs. Keys are always string literals and values can be any expression.

### Syntax

```EasyMQL
{
    "<key1>": <expression1>,
    "<key2>": <expression2>,
    .
    .
}
```

### Examples

```EasyMQL
{"name": "home.html", "size": 1024}
{"nested": {"empty": {}}}
{
    "day": EXTRACT(DAY_OF_YEAR, date),
    "year": EXTRACT(YEAR, date)
}
```

----
