import torch
from sentence_transformers import SentenceTransformer
from nltk.translate.bleu_score import sentence_bleu

def sbertSimilarity(input_ans, majority_ans):
    
    sentence_transformer_model = SentenceTransformer('bert-base-nli-mean-tokens')
    
    sentence_embeddings = sentence_transformer_model.encode(input_ans)
    sentence_embeddings2 = sentence_transformer_model.encode(majority_ans)
   
    cosine = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
    score = torch.mean(cosine(torch.tensor(sentence_embeddings), torch.tensor(sentence_embeddings2))).item()
    
    return score


def matching_score(input_ans, majority_ans, newList):
    i = j = 0

    matching = non_matching = 0
    while (i < len(input_ans) and j < len(majority_ans)):
        if (input_ans[i] == majority_ans[j]):
            matching += 1
            newList.append(input_ans[i])
        else:
            non_matching += 1
            newList.append(majority_ans[i])
        i += 1
        j += 1
    score = (matching / len(input_ans)) * 100
    # if matching >= non_matching:
    #     print( "Claim is true" + str(score))
    # else :
    #     return print("Claim is false" + str(score))
    return score
  

def sentence_bleu_score(input_ans, majority_ans):
    score = sentence_bleu([input_ans], majority_ans, weights=(1, 0, 0, 0))
    return score
