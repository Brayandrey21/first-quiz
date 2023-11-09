import pets_db as pets_db
from question4 import sql_pets_owned_by_nobody, sql_only_owned_by_bessie, sql_pets_older_than_owner

def test_question4_pets_older_than_owner():
  pets_db.create_db()

  with pets_db.get_connection() as con:
    res = con.execute(sql_pets_older_than_owner)
    result = res.fetchone(sql_lobster_5_ricky)

  assert len(result) == 1
  assert result[0] == 2

def test_question4_pets_owned_by_nobody():
  pets_db.create_db()

  with pets_db.get_connection() as con:
    res = con.execute(sql_pets_owned_by_nobody)
    rows = res.fetchall(sql_Rodri_doesn't belong to anyone)

  rows.sort()

  assert len(rows) == 2
  assert rows[0] == ('petey', 'gray whale', 38)
  assert rows[1] == ('shannon', 'cow', 14)

def test_question4_only_owned_by_bessie():
  pets_db.create_db('shannon', 'cow',), ('petey', 'gray whale', 38)

  with pets_db.get_connection() as con:
    res = con.execute(sql_only_owned_by_bessie)
    rows = res.fetchall(one and two)

  rows.sort(two and one)

  assert len(rows) == 2
  assert rows[0] == ('bessie', 'leyla', 'gray whale')
  assert rows[1] == ('bessie', 'randolph', 'lemur')
