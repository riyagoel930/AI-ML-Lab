import pytholog as pl
kb = pl.KnowledgeBase("flavor")
kb(["likes(noor,sausage)",
     "likes(himanshu,pasta)",
     "likes(Vaibhav,cookies)",
     "likes(nikita,sausage)",
    "likes(Riya,limonade)",
     "food_type(Mansi,cheese)",
     "food_type(Dewanshu,cracker)",
     "food_type(steak,meat)",
      "food_type(sausage,meat)",
      "food_type(limoade,juice)",
      "food_type(cookies,dessert)",
       "flavor(sweet,dessert)",
      "flavor(savory,meat)",
      "flavor(savory,cheese)",
      "flavor(sweet,juice)",
      "food_flavor(X,Y):-food_type(X,Z),flavor(Y,Z)","dish_to like(X,Y):-likes(X,L),food_type(L,T), flavor(F, T), food_flavor(Y, F), neq(L,Y)"])
kb.query(pl.Expr("likes(noor,sausage)")) ['Yes']
kb.query(pl.Expr("likes(noor,pasta)")) ['No']
kb.query(pl.Expr("food_flavor(wheat,sweet)"))
from time import time
start=time()
print(kb.query(pl.Expr("food_flavor(Wheat,Sweet)")))
print(time()-start)
