from vaderSentiment_fr.vaderSentiment import SentimentIntensityAnalyzer
class AnalyserSentiment :
    def __init__(self) :
       self.data=[]

    def analyzeSentiment(self,tab_to_analyse):
        annalyser = SentimentIntensityAnalyzer()
        for line in tab_to_analyse :
            line_score = annalyser.polarity_scores(line)
            self.data.append(line_score["compound"])
        return self.data

    def analyzeSentiment2(self, tab_to_analyse):
        annalyser = SentimentIntensityAnalyzer()
        commentaire=["Commentaire"]
        line_score = annalyser.polarity_scores(commentaire)
        score=line_score["compound"]
        return score