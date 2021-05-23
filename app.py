from flask import Flask, render_template, request,send_from_directory
import requests
import numpy as np
from model import score_prediction
from model import winner_prediction
import os
from cv2 import cv2
import pathlib
import glob

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app=Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
    
    return render_template('index.html')


@app.route('/score',methods=['GET', 'POST'])
def Score():
    if request.method == 'POST':
         venue = request.form['venue']
         bat = request.form['bat']
         bowl = request.form['bowl']
         over = float(request.form['over'])
         runs = int(request.form['runs'])
         wickets = int(request.form['wickets'])
         runs_last_5 = int(request.form['runsfive'])
         wickets_last_five = int(request.form['wicketsfive'])
         striker = int(request.form['sruns'])
         non_striker = int(request.form['nsruns'])
         final_score = score_prediction.predict_score(venue, bat, bowl, over, runs, wickets, runs_last_5, wickets_last_five, striker, non_striker)

         return render_template('score.html', prediction_score = "The final predicted score (range): {} to {}".format(final_score-10, final_score+5))

        
        

        
      

    return render_template('score.html')

@app.route('/winner',methods=['GET', 'POST'])
def Winner():
    if request.method == 'POST':
         venue = request.form['venue']
         bat = request.form['bat']
         bowl = request.form['bowl']
         toss_win = float(request.form['toss_win'])
         bat_first = int(request.form['bat_first'])
         
         final_winner = winner_prediction.predict_result(bat, bowl, toss_win, bat_first, venue)

         return render_template('winner.html', prediction_winner = final_winner)

        
        

        
      

    return render_template('winner.html')


if __name__=="__main__":
    app.run(debug=True)