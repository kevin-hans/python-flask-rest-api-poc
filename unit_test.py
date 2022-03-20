import pytest
import json
  
# テスト対象APIコードのappをインポート
from app import app

def test_flask_N001():
    # テスト用コンフィグをtrueに設定
    app.config['TESTING'] = True
    # テスト対象API呼び出し用テストクライアント生成
    client = app.test_client()

    # テスト対象API実行
    response  = client.get('/json')
    body = response .get_json()

    # レスポンス結果と期待値の比較
    assert response.status_code == 200
    assert '日本語' == body['message']

def test_flask_N002():
    # テスト用コンフィグをtrueに設定
    app.config['TESTING'] = True
    # テスト対象API呼び出し用テストクライアント生成
    client = app.test_client()

    # テスト対象API実行
    response = client.get('/user/list')
    body = response.data

    # レスポンス結果と期待値の比較
    assert response.status_code == 200
    json_object = json.loads(response.data.decode('utf-8')) 
    assert 9 == len(json_object)