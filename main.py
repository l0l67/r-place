from flask import *

app = Flask(__name__)


gridSize = 25

colors = [
    '#820080',
    '#CF6EE4',
    '#0000EA',
    '#0083C7',
    '#00D3DD',
    '#02BE01',
    '#94E044',
    '#E5D900',
    '#A06A42',
    '#E59500',
    '#E50000',
    '#FFA7D1',
    '#222222',
    '#888888',
    '#E4E4E4',
    '#FFFFFF'
]
currentColor = colors[0]
grid = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global grid, colors, currentColor, gridSize
        
    if request.method == 'POST':
        value = request.form
        print(value)
        
        if 'color' in value:
            currentColor = value['color']

    return render_template('index.html', grid=grid, gridSize=gridSize)

@app.route('/placePixel', methods=['POST'])
def placePixel():
    global grid, gridSize, currentColor
    
    grid[int(request.form.get('place'))][2] = currentColor
            
    return render_template('index.html', grid=grid, gridSize=gridSize)

@app.route('/grid')
def getGrid():
    global grid, gridSize
    return render_template('grid.html', grid=grid, gridSize=gridSize)

@app.route('/colors')
def getColors():
    global colors, currentColor
    return render_template('colors.html', colors=colors, currentColor=currentColor)
    
    
    
def createGrid():
    global grid, gridSize
    
    y,index = 0,0
    while y < gridSize:
        x = 0
        while x < gridSize:
            grid.append([x +1,y +1, 'white', index])
            x += 1
            index += 1
        y += 1

if __name__ == '__main__':
    createGrid()
    app.run()