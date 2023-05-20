class JogosDatabase:
    def __init__(self, database):
        self.db = database

    def create_jogador(self, name, pontuacao):
        query = "CREATE (:Player {name: $name, pontuacao: $pontuacao})"
        parameters = {"name": name, "pontuacao": pontuacao}
        self.db.execute_query(query, parameters)

    def create_jogos(self, id, resultado, j1):
        query = "MATCH (p:Player {name: $j1}) CREATE (:Match {id: $id})<-[:PARTICIPA]-(p)"
        parameters = {"id": id, "resultado": resultado, "j1": j1}
        self.db.execute_query(query, parameters)

    def get_jogador(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_jogos(self):
        query = "MATCH (m:Match)<-[:PARTICIPA]-(p:Player) RETURN a.resultado AS resultado, p.name AS j1"
        results = self.db.execute_query(query)
        return [(result["resultado"], result["j1"]) for result in results]

    def update_jogador(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def insert_jogador_jogos(self, j1, id, resultado):
        query = "MATCH (a:Player {name: $j1}) MATCH (b:Match {id: $id}) CREATE (a)-[:PARTICIPA]->(b) SET b.resultado = $resultado"
        parameters = {"j1": j1, "id": id, "resultado": resultado}
        self.db.execute_query(query, parameters)

    def delete_jogador(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update_ganhador(self, id, new_name):
        query = "MATCH (m:Match{id: $id}) SET m.resultado = $new_name"
        parameters = {"id": id, "new_name": new_name}
        self.db.execute_query(query, parameters)

