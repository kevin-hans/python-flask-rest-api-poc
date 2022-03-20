
import json
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):
    skippedColumnNamelist = ["query", "query_class", "registry"]

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and x not in self.skippedColumnNamelist  ]:
                data = obj.__getattribute__(field)

                if data is None:
                  continue

                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                  pass
                    # fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
