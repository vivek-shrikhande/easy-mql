from easymql.pipeline import Pipeline


class TestPipeline:
    def test_comments(self):
        # Single line comment
        assert Pipeline.parse(
            '''
            # filter by region
            MATCH region = "West";
            '''
        ) == {'$match': {'$expr': {'$eq': ['$region', 'West']}}}
        # Multiline line comment
        assert Pipeline.parse(
            '''
            # filter
            # by region
            MATCH region = "West";
            '''
        ) == {'$match': {'$expr': {'$eq': ['$region', 'West']}}}
        # Quick comments
        assert Pipeline.parse(
            '''
            MATCH region = "West";  # filter by region
            '''
        ) == {'$match': {'$expr': {'$eq': ['$region', 'West']}}}
        assert Pipeline.parse(
            '''
            MATCH price > 1000 +  # base price
            18 / 100;  # tax
            '''
        ) == {
            '$match': {
                '$expr': {'$gt': ['$price', {'$add': [1000, {'$divide': [18, 100]}]}]}
            }
        }
        # All mixed
        assert Pipeline.parse(
            r'''
            MATCH (name = "hello \"#world" # comment
            # full line comment
            AND (age = 10
            + # 2
            2)
            AND
            (SUBTRACT(5,
            4
            ))); COUNT
             AS doc_count;
            '''
        ) == [
            {
                '$match': {
                    '$expr': {
                        '$and': [
                            {'$eq': ['$name', 'hello "#world']},
                            {'$eq': ['$age', {'$add': [10, 2]}]},
                            {'$subtract': [5, 4]},
                        ]
                    }
                }
            },
            {'$count': 'doc_count'},
        ]
