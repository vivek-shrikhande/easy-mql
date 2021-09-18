
Basic language semantics
- An EasyMQL query corresponds to an aggregation pipeline in MQL.

- EasyMQL query consists of one or more stages. Each stage ends
  with a `;`

  ```EasyMQL
  MATCH language = "English";  # Stage 1
  LIMIT 10;                    # Stage 2
  ```

- **Comments**  
  Comments are python style i.e. start with `#`

- All the language constructs in EasyMQL are **strictly upper cased**. This increases readability.
  ```EasyMQL
  LIMIT 10;                    # Correct
  limit 10;                    # Wrong
  ```

- **Field names**  
  Use single quotes to access the field names. Optionally, you can skip
  them if the field name consists of only `a-z`, `A-Z`, `0-9` and `_`.
  Unlike MQL, `$` prefix is not used.
  ```EasyMQL
  MATCH animal.type = "Dog";     # Correct
  MATCH 'animal.type' = "Dog";   # Correct
  MATCH "animal.type" = "Dog";   # Wrong. Double quotes are used only for strings.
  ```