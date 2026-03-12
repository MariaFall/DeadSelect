from rdflib import Graph, URIRef, Namespace
from rdflib.namespace import RDF, FOAF

all_heroes = [
    "Abrams", "Bebop", "Dynamo", "GreyTalon", "Haze", 
    "Infernus", "Ivy", "Kelvin", "Lash", "McGinnis", 
    "Mirage", "MoAndKrill", "Paradox", "Pocket", "Seven", 
    "Shiv", "Vindicta", "Viscous", "Warden", "Wraith", "Yamato"
]

g = Graph()


#namespace def for URIs
DDLCK = Namespace("http://example.org/deadlock/")
HERO = Namespace("http://example.org/deadlock/hero/")
ITEM = Namespace("http://example.org/deadlock/item/")
STAGE = Namespace("http://example.org/deadlock/stage/")
STATE = Namespace("http://example.org/deadlock/state/")

g.bind("ex", DDLCK)
g.bind("hero", HERO)
g.bind("item", ITEM)
g.bind("stage", STAGE)
g.bind("state", STATE)

count = 0
game_stages = ["EarlyGame", "MidGame", "LateGame"]
game_states = ["isBehind", "isAhead"]

#player x opponent combos
for player in all_heroes:
    for opponent in all_heroes:
        if player != opponent:
            player_uri = HERO[player]
            opponent_uri = HERO[opponent]
            
            matchup_id = f"Matchup_{player}_vs_{opponent}"
            matchup_node = DDLCK[matchup_id]
            #each node is a specific matchup
            g.add((matchup_node, RDF.type, DDLCK.Matchup))
            g.add((matchup_node, DDLCK.hasPlayer, player_uri))
            g.add((matchup_node, DDLCK.hasOpponent, opponent_uri))
            #stage x state combos
            for stage in game_stages:
                for state in game_states:
                    rec_id = f"Rec_{player}_{opponent}_{stage}_{state}"
                    rec_node = DDLCK[rec_id]
                    #add params for item selection
                    g.add((rec_node, RDF.type, DDLCK.Recommendation))
                    g.add((rec_node, DDLCK.forStage, STAGE[stage]))
                    g.add((rec_node, DDLCK.forState, STATE[state]))
                    g.add((rec_node, DDLCK.suggestsItem, ITEM[f"item_{count}"]))
                    g.add((matchup_node, DDLCK.hasRecommendation, rec_node))
                    count += 1

g.serialize(destination="deadlock_standardized.ttl", format="turtle")