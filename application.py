from flask import Flask,request,render_template

from src.pipeline.predict_pipeline import CustomData,Predictpipeline

application=Flask(__name__)
app=application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predicteddata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(message=request.form.get('message'),)

        pred_df=data.get_data_as_frame()
        print(pred_df)
        predict_pipeline=Predictpipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0")