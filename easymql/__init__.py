from easymql.pipeline import Pipeline, encode


class EasyMQL:
    def parse(self, query_string):
        return encode(Pipeline.parse(query_string, explode=False))
