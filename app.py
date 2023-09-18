from flask import Flask, request, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)

def generate_graph(title, x_label, y_label, graph_type, data_points):
    plt.figure()
    plt.title(title, color='r', size=15, family='serif')
    plt.xlabel(x_label, color='g', size=15, family='serif')
    plt.ylabel(y_label, color='b', size=15, family='serif')
    plt.grid(ls='dotted')
    
    if graph_type == 'line':
        x_values = [float(point['x']) for point in data_points]
        y_values = [float(point['y']) for point in data_points]
        plt.plot(x_values, y_values, marker='o', ls='--', lw='2.5', label=y_label)
    elif graph_type == 'bar':
        x_values = [float(point['x']) for point in data_points]
        y_values = [float(point['y']) for point in data_points]
        plt.bar(x_values, y_values, color="orange", label=y_label)
    elif graph_type == 'pie':
        labels = [point['x'] for point in data_points]
        sizes = [float(point['y']) for point in data_points]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, shadow = True)
        
    plt.legend(loc='best')

    img_path = 'static/graph.png'
    plt.savefig(img_path, format='png')
    return img_path

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate-graph', methods=['POST'])
def generate_graph_route():
    graph_title = request.form.get('graph_title')
    lbl_x_axis = request.form.get('lbl_x_axis')
    lbl_y_axis = request.form.get('lbl_y_axis')
    graph_type = request.form.get('graph_type')

    data_points = []

    for key, value in request.form.items():
        if key.startswith('data_x_axis_') and key.replace('x_axis', 'y_axis') in request.form:
            x_value = value
            y_value = request.form[key.replace('x_axis', 'y_axis')]
            
            if x_value and y_value:
                data_points.append({'x': x_value, 'y': y_value})

    img_path = generate_graph(graph_title, lbl_x_axis, lbl_y_axis, graph_type, data_points)
    return render_template('index.html', graph_path=img_path, msg="\u2714 Graph Generated Successfully", data_points=data_points, labels=[lbl_x_axis,lbl_y_axis])

if __name__ == '__main__':
    app.run(debug=True)