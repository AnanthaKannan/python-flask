def response(data, http):
    if http == 'POST':
        return {
            "data": data,
            "status":200,
            "message": 'Suceesfully inserted.'
        }
    elif http == 'PUT':
        return {
                "data": data,
                "status":200,
                "message": 'Suceesfully Updated.'
            }
    elif http == 'DELETE':
        return {
                "data": data,
                "status":200,
                "message": 'Suceesfully Deleted.'
            }
    elif http == 'GET':
        return {
                "data": data,
                "status":200,
                "message": 'Suceesfully Data Fetched.'
            }