from flask import Flask,request,render_template
import fastFood

app = Flask (__name__)
cabecera = ['Nombre']
datos = [['Juan', 24, 'Madrid'], ['Maria', 31, 'Barcelona'], ['Pedro', 27, 'Valencia']]
@app.route("/")
def index():
    show_form=True
    show_table=False
    return render_template("index.html",show_form=show_form,show_table=show_table)


@app.route("/fastfood",methods=['GET'])
def fastfood():
    value= request.args.get('restaurant')
    show_form=False
    show_table=True
    get_info = fastFood.Mcdonalds()
    return render_template("index.html",show_form=show_form,show_table=show_table,headings=get_info[0],data=get_info[1])


if __name__ == "__main__":
    app.run(debug=True,port=5000)