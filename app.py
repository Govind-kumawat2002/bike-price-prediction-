from flask import Flask , render_template,url_for,request # class flask in flask with function 
import joblib
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="bike_price"
)
if mydb.is_connected():
    print('you are connected')
else:
    print('sorry unable to connect')
    mycur = mydb.cursor()
# query = "create table student (stud_id int, student_name varchar(25),student_class varchar(10))"
query2 = "INSERT INTO users values(%s,%s,%s,%s,%s)"

















model =joblib.load("model.lb")
app = Flask(__name__)

@app.route('/') # home route 
def home():
    return render_template('index.html')
@app.route('/project')
def project():
    return render_template('project.html')
# @app.route('/style')
# def style():
#     return render_template('style.css')
@app.route('/about')
def about():
    return render_template('about.html')

    
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/predict',methods =['GET','POST'])
def predict():
    if request.method == 'POST':
        brand_name =request.form['brand_name']
        owner_name = int(request.form['owner'])
        age = int(request.form['age'])
        power = int(request.form['power'])
        kms_driven = int(request.form['kms_driven'])
        brand_labal = {'TVS': 0,
                                'Royal Enfield': 1,
                                'Triumph': 2,
                                'Yamaha': 3,
                                'Honda': 4,
                                'Hero': 5,
                                'Bajaj': 6,
                                'Suzuki': 7,
                                'Benelli': 8,
                                'KTM': 9,
                                'Mahindra': 10,
                                'Kawasaki': 11,
                                'Ducati': 12,
                                'Hyosung': 13,
                                'Harley': 14,
                                'Jawa': 15,
                                'BMW': 16,
                                'Indian': 17,
                                'Rajdoot': 18,
                                'LML': 19,
                                'Yezdi': 20,
                                'MV': 21,
                                'Ideal': 22}
        brand_name=brand_labal[brand_name]
        lst = [[owner_name,brand_name,kms_driven,age,power]]  #owner	brand	price	kms_driven	age	power
        pred = model.predict(lst)
        pred = pred[0]
        pred = round(pred,2)

        return render_template("project.html",prediction=str(pred))
if __name__ == "__main__":
    app.run(debug= True)









   
 
   
   
   
    
                      