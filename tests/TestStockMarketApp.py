import unittest
import json
from app import app, HttpStatus, trades


class TestStockMarketApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    def test_dividend_yield(self):
        data = {"stock_symbol": "ALE", "price": 100}
        response = self.app.post('/dividend_yield', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, HttpStatus.OK)
        self.assertEqual(result["dividend_yield"], 0.23)

    def test_pe_ratio(self):
        data = {"stock_symbol": "GIN", "price": 200}
        response = self.app.post('/pe_ratio', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, HttpStatus.OK)
        self.assertEqual(result["pe_ratio"], 25)

    def test_record_trade(self):
        data = {"stock_symbol": "JOE", "quantity": 100, "indicator": "buy", "price": 150}
        response = self.app.post('/record_trade', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, HttpStatus.OK)
        self.assertEqual(result["message"], "Trade recorded successfully!")


    def test_volume_weighted_stock_price(self):
        data = {"stock_symbol": "POP", "quantity": 100, "indicator": "buy", "price": 150}
        self.app.post('/record_trade', data=json.dumps(data), content_type='application/json')

        data = {"stock_symbol": "POP", "price": 150}
        response = self.app.post('/volume_weighted_stock_price', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, HttpStatus.OK)
        self.assertEqual(result["volume_weighted_stock_price"], 170)

    def test_gbce_all_share_index(self):
        data = {"stock_symbol": "POP", "quantity": 100, "indicator": "buy", "price": 150}
        self.app.post('/record_trade', data=json.dumps(data), content_type='application/json')

        data = {"stock_symbol": "POP", "quantity": 50, "indicator": "buy", "price": 250}
        self.app.post('/record_trade', data=json.dumps(data), content_type='application/json')

        response = self.app.get('/gbce_all_share_index')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, HttpStatus.OK)
        self.assertAlmostEqual(result["gbce_all_share_index"], 193.65)

if __name__ == '__main__':
    unittest.main()
