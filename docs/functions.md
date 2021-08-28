# Functions

Functions in EasyMQL correspond to [Aggregation Pipeline Operators](https://docs.mongodb.com/manual/reference/operator/aggregation/) in MQL.

# Arithmetic Functions

## ABS

Returns the absolute value of a number.

Link to MongoDB [$abs](https://docs.mongodb.com/manual/reference/operator/aggregation/abs).

### Syntax

```EasyMQL
ABS(number)
```

----

## ADD

Adds numbers to return the sum, or adds numbers and a date to return a new date. If adding numbers and a date, treats the numbers as milliseconds. Accepts any number of argument expressions, but at most, one expression can resolve to a date.

Link to MongoDB [$add](https://docs.mongodb.com/manual/reference/operator/aggregation/add).

### Syntax

```EasyMQL
ADD(expression1, expression2, ...)
```

> [!TIP]
> Alternatively, you can use `+` operator.

----

## CEIL

Returns the smallest integer greater than or equal to the specified number.

Link to MongoDB [$ceil](https://docs.mongodb.com/manual/reference/operator/aggregation/ceil).

### Syntax

```EasyMQL
CEIL(number)
```

----

## DIVIDE

Returns the result of dividing the first number by the second. Accepts two argument expressions.

Link to MongoDB [$divide](https://docs.mongodb.com/manual/reference/operator/aggregation/divide).

### Syntax

```EasyMQL
DIVIDE(expression1, expression2)
```

> [!TIP]
> Alternatively, you can use `/` operator.

----

## EXP

Raises e to the specified exponent.

Link to MongoDB [$exp](https://docs.mongodb.com/manual/reference/operator/aggregation/exp).

### Syntax

```EasyMQL
EXP(exponent)
```

----

## FLOOR

Returns the largest integer less than or equal to the specified number.

Link to MongoDB [$floor](https://docs.mongodb.com/manual/reference/operator/aggregation/floor).

### Syntax

```EasyMQL
FLOOR(number)
```

----

## LN

Calculates the natural log of a number.

Link to MongoDB [$ln](https://docs.mongodb.com/manual/reference/operator/aggregation/ln).

### Syntax

```EasyMQL
LN(number)
```

----

## LOG

Calculates the log of a number in the specified base.

Link to MongoDB [$log](https://docs.mongodb.com/manual/reference/operator/aggregation/log).

### Syntax

```EasyMQL
LOG(number, base)
```

----

## LOG10

Calculates the log base 10 of a number.

Link to MongoDB [$log10](https://docs.mongodb.com/manual/reference/operator/aggregation/log10).

### Syntax

```EasyMQL
LOG10(number)
```

----

## MOD

Returns the remainder of the first number divided by the second. Accepts two argument expressions.

Link to MongoDB [$mod](https://docs.mongodb.com/manual/reference/operator/aggregation/mod).

### Syntax

```EasyMQL
MOD(expression1, expression2)
```

> [!TIP]
> Alternatively, you can use `%` operator.

----

## MULTIPLY

Multiplies numbers to return the product. Accepts any number of argument expressions.

Link to MongoDB [$multiply](https://docs.mongodb.com/manual/reference/operator/aggregation/multiply).

### Syntax

```EasyMQL
MULTIPLY(expression1, expression2, ...)
```

> [!TIP]
> Alternatively, you can use `*` operator.

----

## POW

Raises a number to the specified exponent.

Link to MongoDB [$pow](https://docs.mongodb.com/manual/reference/operator/aggregation/pow).

### Syntax

```EasyMQL
POW(number, exponent)
```

----

## ROUND

Rounds a number to to a whole integer or to a specified decimal place.

Link to MongoDB [$round](https://docs.mongodb.com/manual/reference/operator/aggregation/round).

### Syntax

```EasyMQL
ROUND(number, place)
```

----

## SQRT

Calculates the square root.

Link to MongoDB [$sqrt](https://docs.mongodb.com/manual/reference/operator/aggregation/sqrt).

### Syntax

```EasyMQL
SQRT(number)
```

----

## SUBTRACT

Returns the result of subtracting the second value from the first. If the two values are numbers, return the difference. If the two values are dates, return the difference in milliseconds. If the two values are a date and a number in milliseconds, return the resulting date. Accepts two argument expressions. If the two values are a date and a number, specify the date argument first as it is not meaningful to subtract a date from a number.

Link to MongoDB [$subtract](https://docs.mongodb.com/manual/reference/operator/aggregation/subtract).

### Syntax

```EasyMQL
SUBTRACT(expression1, expression2)
```

> [!TIP]
> Alternatively, you can use `-` operator.

----

## TRUNC

Truncates a number to a whole integer or to a specified decimal place.

Link to MongoDB [$trunc](https://docs.mongodb.com/manual/reference/operator/aggregation/trunc).

### Syntax

```EasyMQL
TRUNC(number, place)
```

----

# Array Functions

## ARRAY_ELEM_AT

Returns the element at the specified array index.

Link to MongoDB [$arrayElemAt](https://docs.mongodb.com/manual/reference/operator/aggregation/arrayElemAt).

### Syntax

```EasyMQL
ARRAY_ELEM_AT(array, idx)
```

----

## ARRAY_TO_OBJECT

Converts an array of key value pairs to a document.

Link to MongoDB [$arrayToObject](https://docs.mongodb.com/manual/reference/operator/aggregation/arrayToObject).

### Syntax

```EasyMQL
ARRAY_TO_OBJECT(expression)
```

----

## ARRAY_CONCAT

Concatenates arrays to return the concatenated array.

Link to MongoDB [$concatArrays](https://docs.mongodb.com/manual/reference/operator/aggregation/concatArrays).

### Syntax

```EasyMQL
ARRAY_CONCAT(array1, array2, ...)
```

----

## FILTER

Selects a subset of the array to return an array with only the elements that match the filter condition.

Link to MongoDB [$filter](https://docs.mongodb.com/manual/reference/operator/aggregation/filter).

### Syntax

```EasyMQL
FILTER(input, as, cond)
```

----

## FIRST

Returns the first array element. Distinct from [FIRST](#first-1) accumulator.

Link to MongoDB [$first](https://docs.mongodb.com/manual/reference/operator/aggregation/first).

### Syntax

```EasyMQL
FIRST(expression)
```

----

## IN

Returns a boolean indicating whether a specified value is in an array.

Link to MongoDB [$in](https://docs.mongodb.com/manual/reference/operator/aggregation/in).

### Syntax

```EasyMQL
IN(expression, array expression)
```

----

## INDEX_OF_ARRAY

Searches an array for an occurrence of a specified value and returns the array index of the first occurrence. If the substring is not found, returns -1.

Link to MongoDB [$indexOfArray](https://docs.mongodb.com/manual/reference/operator/aggregation/indexOfArray).

### Syntax

```EasyMQL
INDEX_OF_ARRAY(array expression, search expression, start, end)
```

----

## IS_ARRAY

Determines if the operand is an array. Returns a boolean.

Link to MongoDB [$isArray](https://docs.mongodb.com/manual/reference/operator/aggregation/isArray).

### Syntax

```EasyMQL
IS_ARRAY(expression)
```

----

## LAST

Returns the last array element. Distinct from [LAST](#last-1) accumulator.

Link to MongoDB [$last](https://docs.mongodb.com/manual/reference/operator/aggregation/last).

### Syntax

```EasyMQL
LAST(expression)
```

----

## MAP

Applies a subexpression to each element of an array and returns the array of resulting values in order.

Link to MongoDB [$map](https://docs.mongodb.com/manual/reference/operator/aggregation/map).

### Syntax

```EasyMQL
MAP(input, as, in)
```

----

## OBJECT_TO_ARRAY

Converts a document to an array of documents representing key-value pairs.

Link to MongoDB [$objectToArray](https://docs.mongodb.com/manual/reference/operator/aggregation/objectToArray).

### Syntax

```EasyMQL
OBJECT_TO_ARRAY(object)
```

----

## RANGE

Outputs an array containing a sequence of integers according to user-defined inputs.

Link to MongoDB [$range](https://docs.mongodb.com/manual/reference/operator/aggregation/range).

### Syntax

```EasyMQL
RANGE(start, end, non-zero step)
```

----

## REDUCE

Applies an expression to each element in an array and combines them into a single value.

Link to MongoDB [$reduce](https://docs.mongodb.com/manual/reference/operator/aggregation/reduce).

### Syntax

```EasyMQL
REDUCE(input, initialValue, in)
```

----

## REVERSE_ARRAY

Returns an array with the elements in reverse order.

Link to MongoDB [$reverseArray](https://docs.mongodb.com/manual/reference/operator/aggregation/reverseArray).

### Syntax

```EasyMQL
REVERSE_ARRAY(array expression)
```

----

## SIZE

Returns the number of elements in the array. Accepts a single expression as argument.

Link to MongoDB [$size](https://docs.mongodb.com/manual/reference/operator/aggregation/size).

### Syntax

```EasyMQL
SIZE(expression)
```

----

## SLICE

Returns a subset of an array.

Link to MongoDB [$slice](https://docs.mongodb.com/manual/reference/operator/aggregation/slice).

### Syntax

```EasyMQL
SLICE(array, n) or SLICE(array, position, n)
```

----

## ZIP

Merge two arrays together.

Link to MongoDB [$zip](https://docs.mongodb.com/manual/reference/operator/aggregation/zip).

### Syntax

```EasyMQL
ZIP(inputs, useLongestLength, defaults)
```

----

# Conditional Functions

## IF

A ternary operator that evaluates one expression, and depending on the result, returns the value of one of the other two expressions. Accepts either three expressions in an ordered list or three named parameters.

Link to MongoDB [$cond](https://docs.mongodb.com/manual/reference/operator/aggregation/cond).

### Syntax

```EasyMQL
IF(if, then, else)
```

### Example

```EasyMQL
IF(qty >= 250, 30, 20)
```

----

## IF_NULL

Returns either the non-null result of the first expression or the result of the second expression if the first expression results in a null result. Null result encompasses instances of undefined values or missing fields. Accepts two expressions as arguments. The result of the second expression can be null.

Link to MongoDB [$ifNull](https://docs.mongodb.com/manual/reference/operator/aggregation/ifNull).

### Syntax

```EasyMQL
IF_NULL(expression, replacement-expression-if-null)
```

### Example

```EasyMQL
IF_NULL(description, "Unspecified")
```

----

## CASE

Evaluates a series of case expressions. When it finds an expression which evaluates to `true`, CASE executes a specified expression and breaks out of the control flow.

Link to MongoDB [$switch](https://docs.mongodb.com/manual/reference/operator/aggregation/switch).

### Syntax

```EasyMQL
CASE
    WHEN expression THEN expression
    [ ... ]
    [ ELSE expression ]
END
```

### Example

```EasyMQL
CASE
    WHEN 0 = 5  THEN "equals"
    WHEN 0 > 5  THEN "greater than"
    WHEN 0 < 5  THEN "less than"
END
```

----

# Data Size Functions

## BINARY_SIZE

Returns the size of a given string or binary data value’s content in bytes.

Link to MongoDB [$binarySize](https://docs.mongodb.com/manual/reference/operator/aggregation/binarySize).

### Syntax

```EasyMQL
BINARY_SIZE(string or binData)
```

### Example

```EasyMQL
BINARY_SIZE("Hello World!")
```

----

## BSON_SIZE

Returns the size in bytes of a given document (i.e. bsontype Object) when encoded as BSON.

Link to MongoDB [$bsonSize](https://docs.mongodb.com/manual/reference/operator/aggregation/bsonSize).

### Syntax

```EasyMQL
BSON_SIZE(object)
```

----

# Date Functions

## DATE

Constructs a BSON Date object given the date’s constituent parts. To use constituent date fields in [ISO week date](https://en.wikipedia.org/wiki/ISO_week_date) format, see [ISO_WEEK_DATE](#ISO_WEEK_DATE).

Link to MongoDB [$dateFromParts](https://docs.mongodb.com/manual/reference/operator/aggregation/dateFromParts).

### Syntax

```EasyMQL
DATE(year, month, day, hour, minute, second, millisecond, timezone)
```

### Example

```EasyMQL
DATE(2000, 11, 24, 12, 30, 56, 456, "+0530")
```

----
 
## ISO_WEEK_DATE

Constructs a BSON Date object given the date’s constituent parts in [ISO week date](https://en.wikipedia.org/wiki/ISO_week_date) format.

Link to MongoDB [$dateFromParts](https://docs.mongodb.com/manual/reference/operator/aggregation/dateFromParts).

### Syntax

```EasyMQL
ISO_WEEK_DATE(isoWeekYear, isoWeek, isoDayOfWeek, hour, minute, second, millisecond, timezone)
```

### Example

```EasyMQL
ISO_WEEK_DATE(2000, 11, 6, 12, 30, 56, 456, "+0530")
```

----

## PARSE_DATE

Converts a date/time string to a date object.

Link to MongoDB [$dateFromString](https://docs.mongodb.com/manual/reference/operator/aggregation/dateFromString).

### Syntax

```EasyMQL
PARSE_DATE(dateString, format[, timezone])
```

### Example

```EasyMQL
PARSE_DATE("2017-02-08T12:10:40.787Z", "%Y-%m-%dT%H:%M:%S.%LZ", "America/New_York")
```

----

## FORMAT_DATE

Returns the date as a formatted string.

Link to MongoDB [$dateToString](https://docs.mongodb.com/manual/reference/operator/aggregation/dateToString).

### Syntax

```EasyMQL
FORMAT_DATE(date, format[, timezone])
```

### Example

```EasyMQL
FORMAT_DATE(D"2020-01-15T12:30:59.932-12:00", "%Y-%m-%dT%H:%M:%S.%LZ", "America/New_York")
```

----

## EXTRACT

Returns the value of a given date part. The part must be one of the following,
- `MILLISECOND`  
- `SECOND`  
- `MINUTE`
- `HOUR`
- `DAY_OF_WEEK`
- `ISO_DAY_OF_WEEK`
- `DAY_OF_MONTH`
- `DAY_OF_YEAR`
- `WEEK`
- `ISO_WEEK`
- `MONTH`
- `YEAR`
- `ISO_YEAR`

Link to MongoDB [$dayOfMonth](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$dayOfMonth](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$dayOfWeek](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$dayOfYear](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$hour](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$isoDayOfWeek](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$isoWeek](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$isoWeekYear](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$millisecond](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$minute](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$month](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$second](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$week](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth),
[$year](https://docs.mongodb.com/manual/reference/operator/aggregation/dayOfMonth).

### Syntax

```EasyMQL
EXTRACT(part, date, timezone)
```

### Example

```EasyMQL
EXTRACT(MILLISECOND, D"2020-01-15T12:30:59.932-12:00")
EXTRACT(DAY_OF_WEEK, D"2020-01-15T12:30:59.932Z")
```

----

# Miscellaneous Functions

## RAND

Returns a random float between 0 and 1.

Link to MongoDB [$rand](https://docs.mongodb.com/manual/reference/operator/aggregation/rand).

### Syntax

```EasyMQL
RAND()
```

----

## SAMPLE_RATE

Randomly select documents at a given rate. Although the exact number of documents selected varies on each run, the quantity chosen approximates the sample rate expressed as a percentage of the total number of documents.

Link to MongoDB [$sampleRate](https://docs.mongodb.com/manual/reference/operator/aggregation/sampleRate).

### Syntax

```EasyMQL
SAMPLE_RATE(non-negative float)
```

----

# Object Functions 

## MERGE_OBJECTS

Combines multiple documents into a single document.

Link to MongoDB [$mergeObjects](https://docs.mongodb.com/manual/reference/operator/aggregation/mergeObjects).

### Syntax

```EasyMQL
MERGE_OBJECTS(document) OR MERGE_OBJECTS(document1, document2, ...)
```

----

## OBJECT_TO_ARRAY

Converts a document to an array of documents representing key-value pairs.

Link to MongoDB [$objectToArray](https://docs.mongodb.com/manual/reference/operator/aggregation/objectToArray).

### Syntax

```EasyMQL
OBJECT_TO_ARRAY(object)
```

----

# Set Functions

## ALL

Returns `true` if no element of a set evaluates to `false`, otherwise, returns `false`. Accepts a single argument expression.

Link to MongoDB [$allElementsTrue](https://docs.mongodb.com/manual/reference/operator/aggregation/allElementsTrue).

### Syntax

```EasyMQL
ALL(expression)
```

----

## ANY

Returns `true` if any elements of a set evaluate to `true`; otherwise, returns `false`. Accepts a single argument expression.

Link to MongoDB [$anyElementTrue](https://docs.mongodb.com/manual/reference/operator/aggregation/anyElementTrue).

### Syntax

```EasyMQL
ANY(expression)
```

----

## SET_DIFFERENCE

Returns a set with elements that appear in the first set but not in the second set; i.e. performs a relative complement of the second set relative to the first. Accepts exactly two argument expressions.

Link to MongoDB [$setDifference](https://docs.mongodb.com/manual/reference/operator/aggregation/setDifference).

### Syntax

```EasyMQL
SET_DIFFERENCE(expression1, expression2)
```

----

## SET_EQUALS

Returns `true` if the input sets have the same distinct elements. Accepts two or more argument expressions.

Link to MongoDB [$setEquals](https://docs.mongodb.com/manual/reference/operator/aggregation/setEquals).

### Syntax

```EasyMQL
SET_EQUALS(expression1, expression2, ...)
```

----

## SET_INTERSECTION

Returns a set with elements that appear in all of the input sets. Accepts any number of argument expressions.

Link to MongoDB [$setIntersection](https://docs.mongodb.com/manual/reference/operator/aggregation/setIntersection).

### Syntax

```EasyMQL
SET_INTERSECTION(array1, array2, ...)
```

----

## SET_IS_SUBSET

Returns `true` if all elements of the first set appear in the second set, including when the first set equals the second set; i.e. not a strict subset. Accepts exactly two argument expressions.

Link to MongoDB [$setIsSubset](https://docs.mongodb.com/manual/reference/operator/aggregation/setIsSubset).

### Syntax

```EasyMQL
SET_IS_SUBSET(expression1, expression2)
```

----

## SET_UNION

Returns a set with elements that appear in any of the input sets.

Link to MongoDB [$setUnion](https://docs.mongodb.com/manual/reference/operator/aggregation/setUnion).

### Syntax

```EasyMQL
SET_UNION(expression1, expression2, ...)
```

----

# String Functions

## CONCAT

Concatenates any number of strings.

Link to MongoDB [$concat](https://docs.mongodb.com/manual/reference/operator/aggregation/concat).

### Syntax

```EasyMQL
CONCAT(expression1, expression2, ...)
```

----

## INDEX_OF_BYTES

Searches a string for an occurrence of a substring and returns the UTF-8 byte index of the first occurrence. If the substring is not found, returns -1.

Link to MongoDB [$indexOfBytes](https://docs.mongodb.com/manual/reference/operator/aggregation/indexOfBytes).

### Syntax

```EasyMQL
INDEX_OF_BYTES(string expression, substring expression, start, end)
```

----

## INDEX_OF_CP

Searches a string for an occurrence of a substring and returns the UTF-8 code point index of the first occurrence. If the substring is not found, returns -1

Link to MongoDB [$indexOfCP](https://docs.mongodb.com/manual/reference/operator/aggregation/indexOfCP).

### Syntax

```EasyMQL
INDEX_OF_CP(string expression, substring expression, start, end)
```

----

## LTRIM

Removes whitespace or the specified characters from the beginning of a string.

Link to MongoDB [$ltrim](https://docs.mongodb.com/manual/reference/operator/aggregation/ltrim).

### Syntax

```EasyMQL
LTRIM(input, chars)
```

----

## REGEX_FIND

Applies a regular expression (regex) to a string and returns information on the first matched substring.

Link to MongoDB [$regexFind](https://docs.mongodb.com/manual/reference/operator/aggregation/regexFind).

### Syntax

```EasyMQL
REGEX_FIND(input, regex, options)
```

----

## REGEX_FIND_ALL

Applies a regular expression (regex) to a string and returns information on the all matched substrings.

Link to MongoDB [$regexFindAll](https://docs.mongodb.com/manual/reference/operator/aggregation/regexFindAll).

### Syntax

```EasyMQL
REGEX_FIND_ALL(input, regex, options)
```

----

## REGEX_MATCH

Applies a regular expression (regex) to a string and returns a boolean that indicates if a match is found or not.

Link to MongoDB [$regexMatch](https://docs.mongodb.com/manual/reference/operator/aggregation/regexMatch).

### Syntax

```EasyMQL
REGEX_MATCH(input, regex, options)
```

----

## REPLACE

Replaces the first instance of a matched string in a given input.

Link to MongoDB [$replaceOne](https://docs.mongodb.com/manual/reference/operator/aggregation/replaceOne).

### Syntax

```EasyMQL
REPLACE(input, find, replacement)
```

----

## REPLACE_ALL

Replaces all instances of a matched string in a given input.

Link to MongoDB [$replaceAll](https://docs.mongodb.com/manual/reference/operator/aggregation/replaceAll).

### Syntax

```EasyMQL
REPLACE_ALL(input, find, replacement)
```

----

## RTRIM

Removes whitespace or the specified characters from the end of a string.

Link to MongoDB [$rtrim](https://docs.mongodb.com/manual/reference/operator/aggregation/rtrim).

### Syntax

```EasyMQL
RTRIM(input, chars)
```

----

## SPLIT

Splits a string into substrings based on a delimiter. Returns an array of substrings. If the delimiter is not found within the string, returns an array containing the original string.

Link to MongoDB [$split](https://docs.mongodb.com/manual/reference/operator/aggregation/split).

### Syntax

```EasyMQL
SPLIT(string expression, delimiter)
```

----

## STR_LEN_BYTES

Returns the number of UTF-8 encoded bytes in a string.

Link to MongoDB [$strLenBytes](https://docs.mongodb.com/manual/reference/operator/aggregation/strLenBytes).

### Syntax

```EasyMQL
STR_LEN_BYTES(string expression)
```

----

## STR_LEN

Returns the number of UTF-8 code points in a string.

Link to MongoDB [$strLenCP](https://docs.mongodb.com/manual/reference/operator/aggregation/strLenCP).

### Syntax

```EasyMQL
STR_LEN(string expression)
```

----

## STR_CASE_CMP

Performs case-insensitive string comparison and returns: 0 if two strings are equivalent, 1 if the first string is greater than the second, and -1 if the first string is less than the second.

Link to MongoDB [$strcasecmp](https://docs.mongodb.com/manual/reference/operator/aggregation/strcasecmp).

### Syntax

```EasyMQL
STR_CASE_CMP(expression1, expression2)
```

----

## SUBSTR

Deprecated. Use [SUBSTR_BYTES](#SUBSTR_BYTES) or [SUBSTR_CP](#SUBSTR_CP).

Link to MongoDB [$substr](https://docs.mongodb.com/manual/reference/operator/aggregation/substr).

### Syntax

```EasyMQL
SUBSTR(string, start, length)
```

----

## SUBSTR_BYTES

Returns the substring of a string. Starts with the character at the specified UTF-8 byte index (zero-based) in the string and continues for the specified number of bytes.

Link to MongoDB [$substrBytes](https://docs.mongodb.com/manual/reference/operator/aggregation/substrBytes).

### Syntax

```EasyMQL
SUBSTR_BYTES(string, byte index, byte count)
```

----

## SUBSTR_CP

Returns the substring of a string. Starts with the character at the specified UTF-8 code point (CP) index (zero-based) in the string and continues for the number of code points specified.

Link to MongoDB [$substrCP](https://docs.mongodb.com/manual/reference/operator/aggregation/substrCP).

### Syntax

```EasyMQL
SUBSTR_CP(string expression, code point index, code point count)
```

----

## TO_LOWER

Converts a string to lowercase. Accepts a single argument expression.

Link to MongoDB [$toLower](https://docs.mongodb.com/manual/reference/operator/aggregation/toLower).

### Syntax

```EasyMQL
TO_LOWER(expression)
```

----

## TRIM

Removes whitespace or the specified characters from the beginning and end of a string.

Link to MongoDB [$trim](https://docs.mongodb.com/manual/reference/operator/aggregation/trim).

### Syntax

```EasyMQL
TRIM(input, chars)
```

----

## TO_UPPER

Converts a string to uppercase. Accepts a single argument expression.

Link to MongoDB [$toUpper](https://docs.mongodb.com/manual/reference/operator/aggregation/toUpper).

### Syntax

```EasyMQL
TO_UPPER(expression)
```

----

# Trigonometry Functions

## SIN

Returns the sine of a value that is measured in radians.

Link to MongoDB [$sin](https://docs.mongodb.com/manual/reference/operator/aggregation/sin).

### Syntax

```EasyMQL
SIN(expression)
```

----

## COS

Returns the cosine of a value that is measured in radians.

Link to MongoDB [$cos](https://docs.mongodb.com/manual/reference/operator/aggregation/cos).

### Syntax

```EasyMQL
COS(expression)
```

----

## TAN

Returns the tangent of a value that is measured in radians.

Link to MongoDB [$tan](https://docs.mongodb.com/manual/reference/operator/aggregation/tan).

### Syntax

```EasyMQL
TAN(expression)
```

----

## ASIN

Returns the inverse sin (arc sine) of a value in radians.

Link to MongoDB [$asin](https://docs.mongodb.com/manual/reference/operator/aggregation/asin).

### Syntax

```EasyMQL
ASIN(expression)
```

----

## ACOS

Returns the inverse cosine (arc cosine) of a value in radians.

Link to MongoDB [$acos](https://docs.mongodb.com/manual/reference/operator/aggregation/acos).

### Syntax

```EasyMQL
ACOS(expression)
```

----

## ATAN

Returns the inverse tangent (arc tangent) of a value in radians.

Link to MongoDB [$atan](https://docs.mongodb.com/manual/reference/operator/aggregation/atan).

### Syntax

```EasyMQL
ATAN(expression)
```

----

## ATAN2

Returns the inverse tangent (arc tangent) of y / x in radians, where y and x are the first and second values passed to the expression respectively.

Link to MongoDB [$atan2](https://docs.mongodb.com/manual/reference/operator/aggregation/atan2).

### Syntax

```EasyMQL
ATAN2(expression1, expression2)
```

----

## ASINH

Returns the inverse hyperbolic sine (hyperbolic arc sine) of a value in radians.

Link to MongoDB [$asinh](https://docs.mongodb.com/manual/reference/operator/aggregation/asinh).

### Syntax

```EasyMQL
ASINH(expression)
```

----

## ACONH

Returns the inverse hyperbolic cosine (hyperbolic arc cosine) of a value in radians.

Link to MongoDB [$acosh](https://docs.mongodb.com/manual/reference/operator/aggregation/acosh).

### Syntax

```EasyMQL
ACONH(expression)
```

----

## ATANH

Returns the inverse hyperbolic tangent (hyperbolic arc tangent) of a value in radians.

Link to MongoDB [$atanh](https://docs.mongodb.com/manual/reference/operator/aggregation/atanh).

### Syntax

```EasyMQL
ATANH(expression)
```

----

## DEGREES_TO_RADIANS

Converts a value from degrees to radians.

Link to MongoDB [$degreesToRadians](https://docs.mongodb.com/manual/reference/operator/aggregation/degreesToRadians).

### Syntax

```EasyMQL
DEGREES_TO_RADIANS(expression)
```

----

## RADIANS_TO_DEGREES

Converts a value from radians to degrees.

Link to MongoDB [$radiansToDegrees](https://docs.mongodb.com/manual/reference/operator/aggregation/radiansToDegrees).

### Syntax

```EasyMQL
RADIANS_TO_DEGREES(expression)
```

----

# Type Functions

## CONVERT

Converts a value to a specified type.

Link to MongoDB [$convert](https://docs.mongodb.com/manual/reference/operator/aggregation/convert).

### Syntax

```EasyMQL
CONVERT(input, to, onError, onNull)
```

----

## IS_NUMBER

Returns boolean `true` if the specified expression resolves to an integer, decimal, double, or long.
Returns boolean `false` if the expression resolves to any other BSON type, null, or a missing field.

Link to MongoDB [$isNumber](https://docs.mongodb.com/manual/reference/operator/aggregation/isNumber).

### Syntax

```EasyMQL
IS_NUMBER(expression)
```

----

## TO_BOOL

Converts value to a boolean.

Link to MongoDB [$toBool](https://docs.mongodb.com/manual/reference/operator/aggregation/toBool).

### Syntax

```EasyMQL
TO_BOOL(expression)
```

----

## TO_DATE

Converts value to a Date.

Link to MongoDB [$toDate](https://docs.mongodb.com/manual/reference/operator/aggregation/toDate).

### Syntax

```EasyMQL
TO_DATE(expression)
```

----

## TO_DECIMAL

Converts value to a Decimal128.

Link to MongoDB [$toDecimal](https://docs.mongodb.com/manual/reference/operator/aggregation/toDecimal).

### Syntax

```EasyMQL
TO_DECIMAL(expression)
```

----

## TO_DOUBLE

Converts value to a double.

Link to MongoDB [$toDouble](https://docs.mongodb.com/manual/reference/operator/aggregation/toDouble).

### Syntax

```EasyMQL
TO_DOUBLE(expression)
```

----

## TO_INT

Converts value to an integer.

Link to MongoDB [$toInt](https://docs.mongodb.com/manual/reference/operator/aggregation/toInt).

### Syntax

```EasyMQL
TO_INT(expression)
```

----

## TO_LONG

Converts value to a long.

Link to MongoDB [$toLong](https://docs.mongodb.com/manual/reference/operator/aggregation/toLong).

### Syntax

```EasyMQL
TO_LONG(expression)
```

----

## TO_OBJECT_ID

Converts value to an ObjectId.

Link to MongoDB [$toObjectId](https://docs.mongodb.com/manual/reference/operator/aggregation/toObjectId).

### Syntax

```EasyMQL
TO_OBJECT_ID(expression)
```

----

## TO_STRING

Converts value to a string.

Link to MongoDB [$toString](https://docs.mongodb.com/manual/reference/operator/aggregation/toString).

### Syntax

```EasyMQL
TO_STRING(expression)
```

----

## TYPE

Return the BSON data type of the field.

Link to MongoDB [$type](https://docs.mongodb.com/manual/reference/operator/aggregation/type).

### Syntax

```EasyMQL
TYPE(expression)
```

----

# Accumulators (in&nbsp;[GROUP BY](stages#group-by) Stage)

## ADD_TO_SET

Returns an array of unique expression values for each group. Order of the array elements is undefined.

Link to MongoDB [$addToSet](https://docs.mongodb.com/manual/reference/operator/aggregation/addToSet).

### Syntax

```EasyMQL
ADD_TO_SET(expression)
```

----

## AVG

Returns an average of numerical values. Ignores non-numeric values.

Link to MongoDB [$avg](https://docs.mongodb.com/manual/reference/operator/aggregation/avg).

### Syntax

```EasyMQL
AVG(expression)
```

----

## FIRST

Returns a value from the first document for each group. Order is only defined if the documents are in a defined order.
Distinct from the [FIRST](#first) array operator.

Link to MongoDB [$first](https://docs.mongodb.com/manual/reference/operator/aggregation/first).

### Syntax

```EasyMQL
FIRST(expression)
```

----

## LAST

Returns a value from the last document for each group. Order is only defined if the documents are in a defined order.
Distinct from the [LAST](#last) array operator.

Link to MongoDB [$last](https://docs.mongodb.com/manual/reference/operator/aggregation/last).

### Syntax

```EasyMQL
LAST(expression)
```

----

## MAX

Returns the highest expression value for each group.

Link to MongoDB [$max](https://docs.mongodb.com/manual/reference/operator/aggregation/max).

### Syntax

```EasyMQL
MAX(expression)
```

----

## MERGE_OBJECTS

Returns a document created by combining the input documents for each group.

Link to MongoDB [$mergeObjects](https://docs.mongodb.com/manual/reference/operator/aggregation/mergeObjects).

### Syntax

```EasyMQL
MERGE_OBJECTS(document)
```

----

## MIN

Returns the lowest expression value for each group.

Link to MongoDB [$min](https://docs.mongodb.com/manual/reference/operator/aggregation/min).

### Syntax

```EasyMQL
MIN(expression)
```

----

## PUSH

Returns an array of expression values for each group.

Link to MongoDB [$push](https://docs.mongodb.com/manual/reference/operator/aggregation/push).

### Syntax

```EasyMQL
PUSH(expression)
```

### Example

```EasyMQL
PUSH({ "item": item, "quantity": quantity })
```

----

## STD_DEV_POP

Returns the population standard deviation of the input values.

Link to MongoDB [$stdDevPop](https://docs.mongodb.com/manual/reference/operator/aggregation/stdDevPop).

### Syntax

```EasyMQL
STD_DEV_POP(expression)
```

----

## STD_DEV_SAMP

Returns the sample standard deviation of the input values.

Link to MongoDB [$stdDevSamp](https://docs.mongodb.com/manual/reference/operator/aggregation/stdDevSamp).

### Syntax

```EasyMQL
STD_DEV_SAMP(expression)
```

----

## SUM

Returns a sum of numerical values. Ignores non-numeric values.

Link to MongoDB [$sum](https://docs.mongodb.com/manual/reference/operator/aggregation/sum).

### Syntax

```EasyMQL
SUM(expression)
```

### Example

```EasyMQL
SUM(price * quantity)
```

----

# Accumulators (in Other Stages)

## AVG

Returns an average of the specified expression or list of expressions for each document. Ignores non-numeric values.

Link to MongoDB [$avg](https://docs.mongodb.com/manual/reference/operator/aggregation/avg).

### Syntax

```EasyMQL
AVG(expression1, expression2, ...)
```

----

## MAX

Returns the maximum of the specified expression or list of expressions for each document

Link to MongoDB [$max](https://docs.mongodb.com/manual/reference/operator/aggregation/max).

### Syntax

```EasyMQL
MAX(expression1, expression2, ...)
```

----

## MIN

Returns the minimum of the specified expression or list of expressions for each document

Link to MongoDB [$min](https://docs.mongodb.com/manual/reference/operator/aggregation/min).

### Syntax

```EasyMQL
MIN(expression1, expression2, ...)
```

----

## STD_DEV_POP

Returns the population standard deviation of the input values.

Link to MongoDB [$stdDevPop](https://docs.mongodb.com/manual/reference/operator/aggregation/stdDevPop).

### Syntax

```EasyMQL
STD_DEV_POP(expression1, expression2, ...)
```

----

## STD_DEV_SAMP

Returns the sample standard deviation of the input values.

Link to MongoDB [$stdDevSamp](https://docs.mongodb.com/manual/reference/operator/aggregation/stdDevSamp).

### Syntax

```EasyMQL
STD_DEV_SAMP(expression1, expression2, ...)
```

----

## SUM

Returns a sum of numerical values. Ignores non-numeric values.

Link to MongoDB [$sum](https://docs.mongodb.com/manual/reference/operator/aggregation/sum).

### Syntax

```EasyMQL
SUM(expression1, expression2, ...)
```

----
