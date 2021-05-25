import pickle
import numpy as np

svm = pickle.load(open('./weights/winner_svm.sav', 'rb'))


def predict_result(team1="Chennai Super Kings", team2="Royal Challengers Bangalore", team1_toss_win=1,team1_bat=1, venue="M Chinnaswamy Stadium"):

  temp_array = list()

  #team1
  if team1 == 'Chennai Super Kings':
    temp_array = temp_array + [0]  
  elif team1 == 'Deccan Chargers':
    temp_array = temp_array + [1]
  elif team1 == 'Delhi Daredevils':
    temp_array = temp_array + [2]
  elif team1 == 'Gujarat Lions':
    temp_array = temp_array + [3]
  elif team1 == 'Kings XI Punjab':
    temp_array = temp_array + [4]
  elif team1 == 'Kochi Tuskers Kerala':
    temp_array = temp_array + [5]
  elif team1 == 'Kolkata Knight Riders':
    temp_array = temp_array + [6]
  elif team1 == 'Mumbai Indians':
    temp_array = temp_array + [7]
  elif team1 == 'Pune Warriors':
    temp_array = temp_array + [8]
  elif team1 == 'Rajasthan Royals':
    temp_array = temp_array + [9]
  elif team1 == 'Rising Pune Supergiants':
    temp_array = temp_array + [10]
  elif team1 == 'Royal Challengers Bangalore':
    temp_array = temp_array + [11]
  elif team1 == 'Sunrisers Hyderabad':
    temp_array = temp_array + [12]


  #team2
  if team2 == 'Chennai Super Kings':
    temp_array = temp_array + [0]  
  elif team2 == 'Deccan Chargers':
    temp_array = temp_array + [1]
  elif team2 == 'Delhi Daredevils':
    temp_array = temp_array + [2]
  elif team2 == 'Gujarat Lions':
    temp_array = temp_array + [3]
  elif team2 == 'Kings XI Punjab':
    temp_array = temp_array + [4]
  elif team2 == 'Kochi Tuskers Kerala':
    temp_array = temp_array + [5]
  elif team2 == 'Kolkata Knight Riders':
    temp_array = temp_array + [6]
  elif team2 == 'Mumbai Indians':
    temp_array = temp_array + [7]
  elif team2 == 'Pune Warriors':
    temp_array = temp_array + [8]
  elif team2 == 'Rajasthan Royals':
    temp_array = temp_array + [9]
  elif team2 == 'Rising Pune Supergiants':
    temp_array = temp_array + [10]
  elif team2 == 'Royal Challengers Bangalore':
    temp_array = temp_array + [11]
  elif team2 == 'Sunrisers Hyderabad':
    temp_array = temp_array + [12]

  #toss decision, bat decision
  temp_array = temp_array + [team1_toss_win] + [team1_bat]


  #venue
  if venue == 'Barabati Stadium':
    temp_array = temp_array + [0]
  elif venue=='Brabourne Stadium':
    temp_array = temp_array + [1]
  elif venue=='Buffalo Park':
    temp_array = temp_array + [2]
  elif venue=='De Beers Diamond Oval':
    temp_array = temp_array + [3]
  elif venue=='Dr DY Patil Sports Academy':
    temp_array = temp_array + [4]
  elif venue=='Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
    temp_array = temp_array + [5]
  elif venue=='Dubai International Cricket Stadium':
    temp_array = temp_array + [6]
  elif venue=='Eden Gardens':
    temp_array = temp_array + [7]
  elif venue=='Feroz Shah Kotla':
    temp_array = temp_array + [8]
  elif venue=='Green Park':
    temp_array = temp_array + [9]
  elif venue=='Himachal Pradesh Cricket Association Stadium':
    temp_array = temp_array + [10]
  elif venue == 'Holkar Cricket Stadium':
    temp_array = temp_array + [11]
  elif venue=='JSCA International Stadium Complex':
    temp_array = temp_array + [12]
  elif venue=='Kingsmead':
    temp_array = temp_array + [13]
  elif venue=='M Chinnaswamy Stadium':
    temp_array = temp_array + [14]
  elif venue=='MA Chidambaram Stadium, Chepauk':
    temp_array = temp_array + [15]
  elif venue=='Maharashtra Cricket Association Stadium':
    temp_array = temp_array + [16]
  elif venue=='Nehru Stadium':
    temp_array = temp_array + [17]
  elif venue=='New Wanderers Stadium':
    temp_array = temp_array + [18]
  elif venue=='Newlands':
    temp_array = temp_array + [19]
  elif venue=='OUTsurance Oval':
    temp_array = temp_array + [20]
  elif venue=='Punjab Cricket Association IS Bindra Stadium, Mohali':
    temp_array = temp_array + [21]
  elif venue == 'Punjab Cricket Association Stadium, Mohali':
    temp_array = temp_array + [22]
  elif venue=='Rajiv Gandhi International Stadium, Uppal':
    temp_array = temp_array + [23]
  elif venue=='Sardar Patel Stadium, Motera':
    temp_array = temp_array + [24]
  elif venue=='Saurashtra Cricket Association Stadium':
    temp_array = temp_array + [25]
  elif venue=='Sawai Mansingh Stadium':
    temp_array = temp_array + [26]
  elif venue=='Shaheed Veer Narayan Singh International Stadium':
    temp_array = temp_array + [27]
  elif venue=='Sharjah Cricket Stadium':
    temp_array = temp_array + [28]
  elif venue=='Sheikh Zayed Stadium':
    temp_array = temp_array + [29]
  elif venue=='St George\'s Park':
    temp_array = temp_array + [30]
  elif venue=='Subrata Roy Sahara Stadium':
    temp_array = temp_array + [31]
  elif venue=='SuperSport Park':
    temp_array = temp_array + [32]
  elif venue=='Vidarbha Cricket Association Stadium, Jamtha':
    temp_array = temp_array + [33]
  elif venue=='Wankhede Stadium':
    temp_array = temp_array + [34]

  final_arr = [temp_array]
  pred_result = svm.predict(final_arr)
  if pred_result[0] == 0:
    return team2
  else:
    return team1


