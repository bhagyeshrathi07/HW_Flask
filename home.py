from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
    name = 'Lisa'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
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
                <a href="https://www.google.com/">not google</a>
                <ul>    
                    {city_list}
                </ul>
            </body>
        </html>
        '''
#myapp_obj.run()