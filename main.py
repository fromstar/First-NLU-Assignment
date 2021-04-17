import spacy
import networkx

#EX-1
def shortest_path(sentence):

    nlp = spacy.load("en_core_web_sm");
    doc = nlp(sentence)
    # Load spacy's dependency tree into a networkx graph
    edges = []
    for token in doc:
        for child in token.children:
            edges.append(('{0}'.format(token.lower_), '{0}'.format(child.lower_)))

    graph = nx.Graph(edges)

    root = doc[:].root.text
    for it in doc:
      token = it.text
      print(networkx.shortest_path(graph, root, token))

#EX-2
def get_subtree(sentence, root_subtree):

  nlp = spacy.load("en_core_web_sm");
  doc = nlp(sentence)
  span = doc[:]
  subtrees = []
  list_span=span.text.split()
  for token in span:
    subtrees.append(list(token.subtree))
    
  return subtrees

#EX-3
def exist_subtree(sentence, tokens_list):

  nlp = spacy.load("en_core_web_sm");
  doc = nlp(sentence)
  span = doc[:]
  span_list = span.text.split()

  #to be sure if the given list could form a subtree, as the first thing I try to create a subtree using as a root the first
  #element of the list. If I can't I instantly know that the list doesn't form a subtree.
  try:
    index = span_list.index(tokens_list[0])
    subtree = doc[index].subtree
  except:
    return False
  else:
    list_subtree = list(subtree)

    #if the number of elements of the subtree is different from the number of elements of the list I know that the list doesn't
    #form a subtree
    if len(list_subtree) != len(tokens_list):
      return False

    index = 0
    #checking if all elements of the given list are equal to the elements of the subtree. If not i can interrupt the function.
    for token in list_subtree:
      if token.text != tokens_list[index]:
        return False
      index+=1
    return True

#EX-4
def head_span(sentence):
  nlp = spacy.load("en_core_web_sm");
  doc = nlp(sentence)
  span = doc[:]
  return span.root.text

#EX-5
def get_span(sentence):
  nlp = spacy.load("en_core_web_sm");
  doc = nlp(sentence)
  span = doc[:]
  #index 0: subject, index 1: direct object, index 2: indirect object
  token_list = [[],[],[]]

  for token in doc:
    if(token.dep_ == 'nsubj'):
     token_list[0].append(token.text)
    elif(token.dep_ == 'dobj'):
      token_list[1].append(token.text)
    elif(token.dep_ == 'iobj'):
      token_list[2].append(token.text)
  return token_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sentence = 'i saw the man with a telescope.'
    print('sentence: ' + sentence)

    token = 'about'
    tokens_list = ['from', 'italy']
    print("\nEx. 1")
    shortest_path(sentence)
    print("\nEx. 2")
    print(get_subtree(sentence, token))
    print("\nEx. 3")
    if exist_subtree(sentence, tokens_list):
      print("The given list FORMS a subtree")
    else:
      print("The given list DOESN\'T FORM a subtree")
    print("\nEx. 4")
    print(head_span(sentence))
    print("\nEx. 5")
    print(get_span(sentence))
