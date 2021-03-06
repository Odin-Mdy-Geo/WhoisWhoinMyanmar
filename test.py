
import unittest 
from main import app


class Blueprint_Test(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
	#Test for home directory 
	def test_homepage(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code,200)
	#Test directory for about
	def test_about(self):	
		response = self.app.get("/about")
		self.assertEqual(response.status_code,200)
	#Test directory for contact 
	def test_contact(self):
		response = self.app.get("/contact")
		self.assertEqual(response.status_code,200)
	#Test for bns_leader blueprint 
	def test_bns_leader(self):
		response = self.app.get("/bns")
		self.assertEqual(response.status_code,301)
	#Test for cdt_parties blueprint 
	def test_cdt_parties(self):
		response = self.app.get("/cdt")
		self.assertEqual(response.status_code,301)
	#Test for cele blueprint 
	def test_cele(self):		
		response = self.app.get("/cele")
		self.assertEqual(response.status_code,301)
	#Test for mb_pmt blueprint 
	def test_mb_pmt(self):
		response = self.app.get("/mb")
		self.assertEqual(response.status_code,301)
	#Test for modern_figures blueprint 
	def test_modern_figures(self):
		response = self.app.get("/modern_figures")
		self.assertEqual(response.status_code,301)


if __name__ == '__main__':
	unittest.main()
