import google.generativeai as genai
from flask import Flask,redirect,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/display',methods=['POST','GET'])
def final():
    if request.method == 'POST':
        try:
            a= request.form['prompt']
            if a!='':
                                
                genai.configure(api_key='AIzaSyBPzooRQeTKBK3qd41aZlkNXpoptp_xmG8')
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(a)

                text=''
                for chunk in response.text:
                    text +=chunk.text.replace('**','')

                return render_template('index.html',use=text.replace('*',''))
            return render_template('index.html', use='Enter prompt u foul..')
        except  Exception as e:
            return e
            
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)#,host='192.168.96.190'