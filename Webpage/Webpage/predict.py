from metrics import sbertSimilarity, matching_score, sentence_bleu_score
from ques_ans_pipeline import pipeline
from methods import take_text, query_search_text, getMajority, get_answers, importf, search_bing


ques_ans = {}
majority_l = {}


def predict(head, text):
    print("Generating links")
    # link_list = search_bing(head)
    link_list = take_text(head)
    if not link_list:
        print("Links are empty : ", link_list)
        return -1, -1, -1
    print(link_list)
    nlp = pipeline("multitask-qa-qg")
    print("Generating question-answers")
    question_ans = nlp(text)
    only_question = []
    ques_ans_dict = {}
    ans_all = []
    print("question_ans : ", question_ans)
    for dictionary in question_ans:
        ques_ans_dict[dictionary['question']] = dictionary['answer']
    only_question = list(ques_ans_dict.keys())
    lp = ques_ans_dict
    print("Generating answers with new links")
    query_search_text(link_list, only_question, ans_all, 2)
    dict_ans = []
    get_answers(ques_ans_dict, dict_ans)
    maj_list = getMajority(ans_all)
    finalList = []
    importf(dict_ans, maj_list)
    print("Evaluating")
    verdict = matching_score(dict_ans, maj_list, finalList)
    print("matching_score : ", verdict)
    verdict2 = sentence_bleu_score(dict_ans, maj_list)
    print("sentence_bleu_score : ", verdict2)
    verdict3 = sbertSimilarity(dict_ans, maj_list)
    print("sbertSimilarity : ", verdict3)

    return verdict, verdict2, verdict3
