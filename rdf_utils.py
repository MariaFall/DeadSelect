from rdflib import Graph, Namespace

def obtain_semantic_g():
    g_heroes = Graph()
    g_heroes.parse("deadlock_standardized.ttl", format="turtle")
    return g_heroes

def obtain_full_result(friend_name, enemy_name, g_heroes):
    #def namespace
    friend_uri = Namespace("http://example.org/deadlock/hero/")[friend_name]
    enemy_uri = Namespace("http://example.org/deadlock/hero/")[enemy_name]

    query = """
    PREFIX ex: <http://example.org/deadlock/>
    
    SELECT ?stage ?state ?item
    WHERE {
        ?matchup ex:hasPlayer ?target_friend ;
                 ex:hasOpponent ?target_enemy ;
                 ex:hasRecommendation ?rec .
                 
        ?rec ex:forStage ?stage ;
             ex:forState ?state ;
             ex:suggestsItem ?item .
    }
    """
    
    results = g_heroes.query(query, initBindings={
        'target_friend': friend_uri,
        'target_enemy': enemy_uri
    })
    
    return results

def obtain_items(friend_name, enemy_name, curr_state, curr_stage, g_heroes):

    #namespace uri inis
    friend_uri = Namespace("http://example.org/deadlock/hero/")[friend_name]
    enemy_uri = Namespace("http://example.org/deadlock/hero/")[enemy_name]
    stage_uri = Namespace("http://example.org/deadlock/stage/")[curr_stage]
    state_uri = Namespace("http://example.org/deadlock/state/")[curr_state]

    query = """
    PREFIX ex: <http://example.org/deadlock/>
    
    SELECT ?item
    WHERE {
        ?matchup ex:hasPlayer ?target_friend ;
                 ex:hasOpponent ?target_enemy ;
                 ex:hasRecommendation ?rec .
                 
        ?rec ex:forStage ?target_stage ;
             ex:forState ?target_state ;
             ex:suggestsItem ?item .
    }
    """
    
    items_res = g_heroes.query(query, initBindings={
        'target_friend': friend_uri,
        'target_enemy': enemy_uri,
        'target_stage': stage_uri,
        'target_state': state_uri
    })
    
    return items_res