
## happy path all info 1               
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* length
  - utter_length
* thanks
  - utter_thanks
  
  
## happy path all info 2               
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* length
  - utter_length
* speaker
  - utter_speaker
* thanks
  - utter_thanks    
  

## happy path all info 3               
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* speaker
  - utter_speaker
* length
  - utter_length
* thanks
  - utter_thanks  


## happy path no relevant audience            
* greet              
  - utter_greet
* recommend_session
  - utter_ask_relevant_audience
* inform{"relevant_audience":"Data Scientists"}
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* length
  - utter_length
* speaker
  - utter_speaker
* thanks
  - utter_thanks



## multi-intent story1              
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* speaker+length
  - utter_length
  - utter_speaker
* thanks
  - utter_thanks
  
## multi-intent story2              
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* speaker+length
  - utter_length
  - utter_speaker
* abstract
  - utter_abstract
* thanks
  - utter_thanks
  
