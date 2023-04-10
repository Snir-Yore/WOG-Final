from flask import Flask , render_template_string

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open('scores.txt', 'r') as f:
            score = f.read().strip()
            return f'''
                <html>
                <head>
                <title>Scores Game</title>
                </head>
                <body>
                <h1>The score is <div id="Score">{score}</div></h1>
                </body>
                </html>
            '''
    except Exception as e:
        return f'''
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1><div id="score" style="color:red">{e}</div></h1>
            </body>
            </html>
        '''

# if __name__ == '__main__':
app.run()
