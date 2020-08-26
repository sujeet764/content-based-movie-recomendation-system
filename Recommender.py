import pickle
import random

class Recommender_engine():
    def __init__(self):
        self.title = None
        
    def hollywood(self,title):
        with open("hollywood/sigmoid_kernel.pickle","rb") as f:
            sig = pickle.load(f)
        
        with open("hollywood/indices.pickle","rb") as f:
            indices = pickle.load(f)
    
        with open("hollywood/movie_title.pickle","rb") as f:
            movies_df = pickle.load(f)
        
        try:
            self.title = title
            title1 = self.title.strip().lower()
            idx = indices[title1]
            sig_score = list(enumerate(sig[idx]))
            sig_score = sorted(sig_score, key=lambda x: x[1], reverse=True)
            
            sig_score = sig_score[1:20]
            random.shuffle(sig_score)
            sig_score = sig_score[0:10]
            
            movie_indices = [i[0] for i in sig_score]
            value = movies_df.iloc[movie_indices]
            value = value.reset_index(drop = True)
            value.index = value.index+1
            return value
        except:        
            return "$"
        
    def bollywood(self,title):    
        with open('bollywood/bolly_sigmoid_kernel.pickle','rb') as f:
            sig = pickle.load(f)
        
        with open('bollywood/bolly_indices.pickle','rb') as f:
            indices = pickle.load(f)
        
        with open('bollywood/bolly_movie_title.pickle','rb') as f:
            movies_df = pickle.load(f)    
    
    
        try:
            self.title = title
            title1 = self.title.strip().lower()
            idx = indices[title1]
            sim_score = list(enumerate(sig[idx]))
            sim_score = sorted(sim_score, key =lambda x:x[1],reverse=True)
            
            sim_score = sim_score[1:20]
            random.shuffle(sim_score)
            sim_score = sim_score[0:10]
            
            movie_indices = [i[0] for i in sim_score]
            value = movies_df['original_title'].iloc[movie_indices]
            value.reset_index(drop = True, inplace = True)
            value.index = value.index+1
            return value
        except:
            return "@"
    
    def book_recommend(self,title):    
        with open('books/book_sig.pickle','rb') as f:
            sig = pickle.load(f)
        
        with open('books/book_indices.pickle','rb') as f:
            indices = pickle.load(f)
        
        with open('books/book_title.pickle','rb') as f:
            book_title = pickle.load(f)    
        try:
            self.title = title
            title= title.strip().lower()
            idx = indices[title]
            sig_score = list(enumerate(sig[idx]))
            sig_score = sorted(sig_score,key=lambda x : x[1], reverse=True)
            
            sig_score = sig_score[1:20]
            random.shuffle(sig_score)
            sig_score = sig_score[0:10]
            
            book_indices = [i[0] for i in sig_score]
            value = book_title['Title'].iloc[book_indices]
            value.reset_index(drop = True,inplace = True)
            value.index = value.index+1
            return value
        except:
            return "$"
    
    def song_recommend(self,title):
        with open('song/song_sig.pickle','rb') as f:
            sig = pickle.load(f)
        
        with open('song/song_indices.pickle','rb') as f:
            indices = pickle.load(f)
        
        with open('song/song_title.pickle','rb') as f:
            song_title = pickle.load(f)  
            
        try:
            self.title = title.strip().lower()
            idx = indices[self.title]
            sig_score = list(enumerate(sig[idx]))
            sig_score = sorted(sig_score, key=lambda x:x[1], reverse = True)
            
            sig_score = sig_score[1:20]
            random.shuffle(sig_score)
            sig_score = sig_score[0:10]
            
            song_indices = [i[0] for i in sig_score]
            value = song_title['song'].iloc[song_indices]
            value.reset_index(drop = True, inplace = True )
            value.index = value.index+1
            return value
        except:
            return "$"
    
        
    
