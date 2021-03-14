from easymql.expressions import Expression


class TestConditionalExpression:
    @classmethod
    def setup_class(cls):
        cls.exp = Expression

    def test_cond(self):
        assert self.exp.parse('IF (true, "it\'s true", "it\'s false")') == {
            '$cond': {'else': "it's false", 'if': True, 'then': "it's true"}
        }

    def test_ifnull(self):
        assert self.exp.parse('IF_NULL(null, 0)') == {'$ifNull': [None, 0]}

    def test_switch(self):
        assert self.exp.parse(
            'CASE WHEN ADD(1,2) THEN "go" WHEN false THEN "stop" END'
        ) == {
            '$switch': {
                'branches': [
                    {'case': {'$add': [1, 2]}, 'then': 'go'},
                    {'case': False, 'then': 'stop'},
                ]
            }
        }

        assert self.exp.parse('CASE WHEN ADD(1,2) THEN "go" ELSE "stop" END') == {
            '$switch': {
                'branches': [{'case': {'$add': [1, 2]}, 'then': 'go'}],
                'default': 'stop',
            }
        }
