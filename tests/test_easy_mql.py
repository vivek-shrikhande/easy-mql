from easymql import EasyMQL


class TestEasyMQL:
    @classmethod
    def setup_class(cls):
        cls.emql = EasyMQL()

    # keep adding the queries here
    def test_parser(self):
        assert (
            self.emql.parse(
                '''
                PROJECT +title,
                        +author.first,
                        +author.last,
                        IF (author.middle = "",
                            $REMOVE,
                            author.middle) AS author.middle;
                '''
            )
            == [
                {
                    '$project': {
                        'title': 1,
                        'author.first': 1,
                        'author.last': 1,
                        'author.middle': {
                            '$cond': {
                                'if': {'$eq': ['$author.middle', '']},
                                'then': '$$REMOVE',
                                'else': '$author.middle',
                            }
                        },
                    }
                }
            ]
        )
        assert self.emql.parse(
            '''
            GROUP BY item
            PROJECT SUM ( price * quantity ) AS totalSaleAmount;
            MATCH totalSaleAmount >= 100;
            '''
        ) == [
            {
                '$group': {
                    '_id': '$item',
                    'totalSaleAmount': {'$sum': {'$multiply': ['$price', '$quantity']}},
                }
            },
            {'$match': {'$expr': {'$gte': ['$totalSaleAmount', 100]}}},
        ]
