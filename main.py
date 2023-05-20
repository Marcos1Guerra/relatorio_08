from database import Database
from jogo_database import JogosDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.193.211.54:7687", "neo4j", "saps-health-church")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
partidas = JogosDatabase(db)

partidas.create_jogador("fulano", 21)
partidas.create_jogador("ciclano", 19)
partidas.create_jogador("betrano", 20)
partidas.create_jogador("luis", 1)
partidas.create_jogador("bia", 2)
partidas.create_jogador("ana", 3)

partidas.create_jogos("Partida01", " fulano ganhou", "fulano")
partidas.create_jogos("Partida02", " ciclano perdeu", "ciclano")

partidas.update_jogador("fulano", "alguem")

partidas.delete_jogador("alguem")

partidas.insert_jogador_jogos("betrano", "Partida01", " betrano perdeu")
partidas.insert_jogador_jogos("luis", "Partida02", "luis ganhou")
partidas.insert_jogador_jogos("ana", "Partida02", "ana perdeu")
partidas.insert_jogador_jogos("bia", "Partida01", "bia perdeu")

partidas.update_ganhador("Partida01", "ninguem ganhou")
partidas.update_ganhador("Partida02", "luis ganhou")

# Fechando a conexão
db.close()