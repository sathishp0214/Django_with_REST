d={
    "count": 3,
    "next": 'null',
    "previous": 'null',
    "results": [
        {
            "url": "http://127.0.0.1:8000/users/3/",
            "username": "sundar",
            "email": "sundar@gmail.com",
            "groups": [
                "http://127.0.0.1:8000/groups/1/"
            ]
        },
        {
            "url": "http://127.0.0.1:8000/users/2/",
            "username": "babu",
            "email": "babu@gmail.com",
            "groups": []
        },
        {
            "url": "http://127.0.0.1:8000/users/1/",
            "username": "sathish",
            "email": "sathishp0214@gmail.com",
            "groups": []
        }
    ]
}


print type(d["results"])

for i in d["results"]:
    print type(i)