stopword_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers','herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which','who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been','being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if','or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into','through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off','over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all','any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own','same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't",'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',"mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't",'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def cleaning(input_string, stopword_list):
  seperators = [" ","-","_","+",",","#",".",";","!","?",":","^"]
  for sep in seperators:
    cleaned_str = input_string.replace(sep, '|')
    input_string = cleaned_str
  cleaned_str = cleaned_str.split('|')
  cleaned_str = list(filter(None, cleaned_str))
  num_cleaned_str = []
  for obj in cleaned_str:
    for char in obj:
      if char in ['0','1','2','3','4','5','6','7','8','9']:
        #print('number')
        obj = obj.replace(char, '')
    if obj not in stopword_list:
      num_cleaned_str.append(obj)
  return num_cleaned_str

input_string = 'he998l8lo,  shan lorenz  th-is   is an +inputstring!'

out = cleaning(input_string, stopword_list)
print(out)