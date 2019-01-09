from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import operator

def homepage(request):
	return render(request, "home.html", {'name':'This Is Manish'})

def count(request):
	data=request.GET['fulltextarea']
	# print(data)
	word_lists=data.split()
	# print(word_lists)
	word_length=len(word_lists)
	# print(word_length)

	word_dict={}
	for word in word_lists:
		if word in word_dict:
			# increase the vbalue by 1
			word_dict[word]+=1
		else:
			# add to this in word dictionary
			word_dict[word]=1

	sorted_list=sorted(word_dict.items(),  key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':data, 'words':word_length, 'worddictionary':sorted_list})



def about(request):
	return render(request, 'about.html')



def contact(request):
	return render(request,'contact.html')