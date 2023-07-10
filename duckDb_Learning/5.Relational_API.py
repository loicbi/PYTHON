import duckdb
rel = duckdb.sql('SELECT * FROM range(1000000000000) myTable(ippppd)')
rel.limit(10, 5).order('ippppd desc').show()

rel = duckdb.sql('SELECT * FROM range(1000000) tbl(id)')
rel.aggregate('id % 2 AS g, sum(id), min(id), max(id)')
rel = duckdb.sql('SELECT sum(id), min(id), max(id) FROM range(1000000) tbl(id)')
rel.show()


rel = duckdb.sql('SELECT * FROM range(10) myTable(valueField)')
rel2 = duckdb.sql('SELECT * FROM range(2) myTable(valueField)')
rel.except_(rel2).show()
rel.filter('valueField = 1 or valueField = 2 ').show()

# intersect
r1 = duckdb.sql('SELECT * FROM range(10) tbl(id)')
r2 = duckdb.sql('SELECT * FROM range(5) tbl(id)')
r1.intersect(r2).show()

# join
rel1 = duckdb.sql('SELECT * FROM range(5) tbl(id)').set_alias('r1')
rel2 = duckdb.sql('SELECT * FROM range(10, 15) tbl(id)').set_alias('r2')
rel1.join(rel2, 'r1.id + 10 = r2.id').show()






