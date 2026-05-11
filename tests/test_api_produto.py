
def post_get_e_put_produto(client):
    response = client.post("/produtos", json={"codigo":1, "valor":30.0, "tipo":2, "desconto_percentual": 0.0})
    assert response.status_code == 200
    assert response.json()["codigo"]==1

    response2 = client.get("/produtos/1")
    assert response2.status_code == 200
    assert response2.json()["valor"]==30.0

    response3 = client.put("/produtos/1/40.5")
    assert response3.status_code == 200
    assert response3.json()["valor"]==40.5

def test_get_produto_inexistente(client):
    response = client.get("/produtos/000")
    assert response.status_code == 404

def test_put_produto_atualizar(client):
    response = client.post("/produtos", json={"codigo":1, "valor":30.0, "tipo":2, "desconto_percentual": 0.0})
    assert response.json()["valor"]= 15.0
    assert response.value.detail == "{"alterou": true}"