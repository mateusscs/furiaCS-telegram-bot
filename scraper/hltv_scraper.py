from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

def get_lineup_furia():
    driver.get("https://www.hltv.org/team/8297/furia")
    player_elements = driver.find_elements(By.CLASS_NAME, "playerFlagName")
    player_names = []
    for player in player_elements:
        name = player.text
        player_names.append(name)
    return player_names

def get_last_matches_furia():
    driver.get("https://www.hltv.org/team/8297/furia#tab-matchesBox")
    events_elements = driver.find_elements(By.CLASS_NAME, "event-header-cell")
    games_elements = driver.find_elements(By.CLASS_NAME, "team-row")
    games_names = []
    events_names = []
    max_tournament = 2
    j = 0
    for i in range(min(max_tournament, len(events_elements))):
         event = events_elements[i].text
         events_names.append(event) 
         print(f"Evento: {event}")
         while j < len(games_elements):
            games = games_elements[j].text
            games_names.append(games)
            j = j + 1
            print(f"Jogo: {games}")
       
        
    return events_names, games_names
    

def get_ranking_furia():
    driver.get("https://www.hltv.org/team/8297/furia")
    team_ranking = driver.find_element(By.CLASS_NAME, "profile-team-stat-50-50")
    ranking_stats =team_ranking.text
    
    return ranking_stats
