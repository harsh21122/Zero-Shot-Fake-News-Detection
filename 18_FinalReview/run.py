from predict import predict

print("***************WELCOME TO FAKE NEWS DETECTION APP***************")
headline = input("Please enter the headline of the news article ----> ")
print("\n\n")
body = input("Please enter the body of the news article ----> ")
print("\n\n")

matching_score,sentence_bleu_score,sbertSimilarity = predict(head=headline,text=body)

if sbertSimilarity>0.75:
    print("Great! your news article is authentic")
else:
    print("Oops! your news article is fake.")