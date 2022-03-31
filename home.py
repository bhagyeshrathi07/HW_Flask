from flask import Flask

myobj = Flask(__name__)

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route("/")
def home():
    city_list = ''
    for city in city_names:
        city_list += f'<li>{city}</li>'
    return f'''
        <html>
            <head>
                <title>HomePage</title>
            </head>
            <body>
                <h1>Welcome {name}! </h1>
                <a href="www.google.com">not google</a>
                <ul>    
                    {city_list}
                </ul>
            </body>
        </html>
        '''
#myapp_obj.run()