'''
Utils for explore schema
'''

from typing import Dict, List, Tuple

from tenable.errors import RequestValidationError
from tenable.io.v3.base.schema.explore.search import SortSchema


def generate_sort_data(kw: Dict, is_with_prop: bool = True) -> List[Dict]:
    schema = SortSchema()
    sort_data = []
    data = kw.get('sort')
    if isinstance(data, List):
        for tup in data:
            if isinstance(tup, Tuple) and len(tup) == 2:
                property = tup[0]
                order = tup[1]
                data_validate = dict(property=property, order=order)
                data_validate = schema.load(data_validate)
                if is_with_prop:
                    sort_data.append(schema.dump(data_validate))
                else:
                    sort_data.append({property: order})
            else:
                raise RequestValidationError(
                    'Sort', '[("field_name_1", "asc"),'
                            ' ("field_name_2", "desc")]'
                )
    else:
        sort_data = []

    return sort_data
