from metrics import sbertSimilarity, matching_score, sentence_bleu_score
from ques_ans_pipeline import pipeline
from methods import take_text, query_search_text, getMajority, get_answers, importf, search_bing


# app = Flask(__name__)

# global lp
# lp = {}
ques_ans = {}
majority_l = {}
# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/predict',methods=['POST'])
def predict(head,text):
    # ll = [x for x in request.form.values()]
    # head = ll[0]
    # text = ll[1]
    # session["head"] = head
    # session['text'] = text
    # return redirect(url_for('ques_ans', text=text))

    # print(text)
    print("Generating links")
    link_list =  search_bing(head)
    if not link_list:
        print("Links are empty : ", link_list)
        return -1, -1, -1
#     link_list = take_text(head)
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
    lp=ques_ans_dict
    print("Generating answers with new links")
    query_search_text(link_list, only_question, ans_all, 2)
    dict_ans = []
    get_answers(ques_ans_dict, dict_ans)
    maj_list = getMajority(ans_all)
    # print(maj_list)
    finalList = []
    importf(dict_ans, maj_list)
    print("Evaluating")
    verdict = matching_score(dict_ans, maj_list, finalList)
    print("matching_score : ", verdict)
    verdict2 = sentence_bleu_score(dict_ans, maj_list)
    print("sentence_bleu_score : ", verdict2)
    verdict3 = sbertSimilarity(dict_ans, maj_list)
    print("sbertSimilarity : ", verdict3)

    # l = [score,ques_ans_dict,maj_list]
    # return redirect(url_for('ques_ans', score=l))
    # if request.method == 'POST':
    #     date = request.form.get('ques')
    #     return redirect(url_for('ques_ans', ques=date))
    # print(request.method)
    # if score >= 50:
    #     return render_template('index.html', prediction_text='This Article is Trustworthy with a S-Bert Score of {}'.format(score)
    # else:
    #     return render_template('index.html', prediction_text='This Article is Fake with a S-Bert Score of {}'.format(score))
    return verdict, verdict2,verdict3
    # print(request.method)
    # if request.method == 'POST':
    #     date = request.form.get('date')
    #     return redirect(url_for('booking', date=date))
#
# @app.route('/ques_ans/<score>')
# def ques_ans(score):
#     mylist = print_ques_ans()
#     print(request.method)
#     print(lp)
#     # head = session.get("head")
#     # text = session.get("text")
#     print(score)
#     r = score[1:6]
#     q = score[10:60]
#     return render_template('table.html', prediction_text = r, question_answer=q)





