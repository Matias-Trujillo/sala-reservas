from app.api import app

def test_reserva_exitosa():
    cliente = app.test_client()
    resp = cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert resp.status_code == 201

def test_reserva_duplicada():
    cliente = app.test_client()
    # Primera vez debe funcionar
    cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    # Segunda vez debe fallar
    resp = cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert resp.status_code == 409
