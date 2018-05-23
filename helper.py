"""
    helper.py - Helper functions
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/23/18
"""

def use_schema(data):
    """
    Convert data to the a custom schema.
    The output will have this format:
        [
            {
                'id': <int>,
                'timestamp': <unix_time>.
                'data': {
                    'temperature': {
                        'value': <float>,
                        'unit': <string>
                    },
                    'humidity': {
                        'value': <float>,
                        'unit': <string>
                    }
                }
            },
            ...
        ]

    Params:
        data <list>: List of database object.
    
    Return:
        List of dictionary.
    """
    result = []

    for item in data:
        scheme = {
            'id': item[0],
            'timestamp': item[4],
            'data': {
                'temperature': {
                    'value': item[1],
                    'unit': item[2]
                },
                'humidity': {
                    'value': item[3],
                    'unit': '%'
                }
            }
        }

        result.append(scheme)

    return result
