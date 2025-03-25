from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - start offering your skills online!",
    "Online Tutoring – Teach a subject you’re good at via platforms like Wyzant or Preply",
    "Print-on-Demand Business – Sell custom designs on t-shirts, mugs, and more through platforms like Redbubble or Printful.",
    "Affiliate Marketing – Promote products online and earn commissions through affiliate programs like Amazon Associates.",
    "Dropshipping – Sell products online without holding inventory by using suppliers from platforms like Shopify and AliExpress.",
    "Content Creation – Start a YouTube channel, blog, or podcast around a niche you enjoy.",
    "Selling Digital Products – Create and sell printables, e-books, or templates on Etsy or Gumroad.",
    "Virtual Assistant Services – Help businesses with admin tasks like email management and scheduling.",
    "Stock Photography – Sell your photos to stock websites like Shutterstock or Adobe Stock.",
    "Handmade Crafts – Sell handmade jewelry, candles, or home decor on Etsy or at craft fairs.",
    "Pet Sitting/Dog Walking – Earn money by caring for pets through Rover or Wag.",
]

money_quotes = [
   "The secret to getting ahead is getting started. – Mark Twain",
   "The more you learn, the more you earn. – Warren Buffett",
   "Don’t work for money; make money work for you. – Robert Kiyosaki",
   "Opportunities come to those who create them. – Chris Grosser",
   "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
   "It’s not your salary that makes you rich, it’s your spending habits. – Charles A. Jaffe",
   "An investment in knowledge pays the best interest. – Benjamin Franklin",
]

@app.get("/side_hustles")
def get_side_hustles():
    """return a random side hustle ideas"""
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """returns a random money quotes"""
    return {"money_quote": random.choice(money_quotes)}