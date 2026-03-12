# Deadlock Knowledge Graph

A semantic data engineering project that builds and queries a knowledge graph for the game Deadlock. 

## Features
* **Semantic Ontology:** Uses standard RDF triples to map complex game relationships through dedicated Matchup and Recommendation nodes.
* **Automated Graph Generation:** Procedurally generates a `.ttl` DB of matchups.
* **SPARQL Integration:** Includes utility functions to execute SPARQL queries against the local graph to retrieve item reocmmendations

## Tech Stack
* Python
* `rdflib` 
* SPARQL 

## Project Structure
* `make_db.py`: DB generation script.
* `rdf_utils.py`:  Querying utilities required to load the ttl file into memory and execute SPARQL.
